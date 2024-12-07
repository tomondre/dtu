// index.js

require('dotenv').config();
const fs = require('fs-extra');
const path = require('path');
const axios = require('axios');
const pdfParse = require('pdf-parse');
const Ajv = require('ajv');

// ==================== Configuration ====================

// Load OpenAI API key from environment variables
const OPENAI_API_KEY = process.env.OPENAI_API_KEY;

if (!OPENAI_API_KEY) {
    console.error("Error: OPENAI_API_KEY is not set in the .env file.");
    process.exit(1);
}

// Folder containing PDFs
const PDF_FOLDER = path.join(__dirname, 'papers'); // Ensure this path is correct

// Output JSON file
const OUTPUT_JSON = path.join(__dirname, 'out', 'extracted_insights.json');

// Backup settings
const BACKUP_INTERVAL = 5; // Save every 5 entries

// JSON Schema for Validation
const schema = {
    type: "object",
    properties: {
        paperName: { type: "string" },
        bibliographicReference: { type: "string" },
        insights: {
            type: "array",
            items: {
                type: "object",
                properties: {
                    insight: { type: "string" },
                    explanation: { type: "string" },
                    grouping: { type: "string" }
                },
                required: ["insight", "explanation", "grouping"],
                additionalProperties: false
            }
        }
    },
    required: ["paperName", "bibliographicReference", "insights"],
    additionalProperties: false
};

const ajv = new Ajv();
const validate = ajv.compile(schema);

// =========================================================

// Function to extract text from a PDF file
async function extractTextFromPDF(pdfPath) {
    try {
        const dataBuffer = await fs.readFile(pdfPath);
        const data = await pdfParse(dataBuffer);
        return data.text;
    } catch (error) {
        console.error(`Error reading ${pdfPath}: ${error.message}`);
        return '';
    }
}

// Function to get insights from GPT
async function getInsightsFromGPT(paperContent, paperName) {
    // Construct the prompt
    const prompt = `
You are an expert literature analyst specializing in OT Cybersecurity. Your task is to extract key insights from an academic paper based on its entire content. Follow the instructions below to ensure the extracted information is precise, well-cited, and organized for further analysis.

**Input:**
- **Paper Content:** "${paperContent}"

**Tasks:**

1. **Identify Key Insights:**
   - Extract the **5 most important insights** mentioned in the paper, ensuring that each insight is directly supported by information in the paper's content.
   - Each **Insight Statement** must be a **specific citation** from the paper's body.

2. **Organize Extracted Information:**
   - For each insight, provide the following structured information:
     - **Insight Statement:** A specific citation from the paper that encapsulates the insight.
     - **Explanation:** A brief explanation or context elaborating on the insight, based on the paper's content.
     - **Bibliographic Reference:** A bibliographic entry suitable for a ".bib" file (e.g., "@article{AuthorYear, title={...}, author={...}, journal={...}, year={...}}").
     - **Logical Grouping:** Assign each insight to a logical group based on its content. The grouping should be specific enough to facilitate meaningful analysis but broad enough to encompass related insights.

**Output Format:**

Return the extracted information in the following JSON structure:

{
    "paperName": "Name of the paper",
    "bibliographicReference": "@article{AuthorYear, title={...}, author={...}, journal={...}, year={...}}",
    "insights": [
        {
            "insight": "Specific citation from the paper body encapsulating the insight.",
            "explanation": "Detailed explanation with concrete information from the paper.",
            "grouping": "Logical grouping name"
        },
        // Repeat for each insight (total of 5)
    ]
}

**Guidelines:**

- **Relevance:** Ensure that each insight directly relates to key points in the paper.
- **Specificity:** Each Insight Statement should be a direct quote or a precise paraphrase from the paper's body.
- **Consistency:** Use a consistent bibliographic reference format throughout.
- **Logical Grouping:** Examples of groupings could include themes like "AI in Cybersecurity," "Risk Assessment Models," "Policy Frameworks," etc.
- **Validation:** Ensure that the JSON structure is strictly followed for seamless integration into your analysis pipeline.
`;

    try {
        const response = await axios.post('https://api.openai.com/v1/chat/completions', {
            model: 'o1-mini',
            messages: [
                { role: 'user', content: prompt }
            ],
            // Temperature is removed as per user request
        }, {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${OPENAI_API_KEY}`
            }
        });

        let content = response.data.choices[0].message.content;
        content = content.replace('```json', '');
        content = content.replace('```', '');

        // Attempt to parse JSON; handle potential errors gracefully
        let insightsJson;
        try {
            insightsJson = JSON.parse(content);
        } catch (parseError) {
            console.error(`Error parsing JSON response for ${paperName}: ${parseError.message}`);
            console.error(`GPT Response: ${content}`);
            return null;
        }

        // Validate JSON structure
        if (!validate(insightsJson)) {
            console.error(`Invalid JSON structure for ${paperName}:`, validate.errors);
            console.error(`GPT Response: ${content}`);
            return null;
        }

        return insightsJson;
    } catch (error) {
        console.error(`Error communicating with OpenAI API for ${paperName}: ${error.message}`);
        return null;
    }
}

// Main function
async function main() {
    // Initialize or load existing data
    let data = [];
    if (await fs.pathExists(OUTPUT_JSON)) {
        try {
            const existingData = await fs.readFile(OUTPUT_JSON, 'utf-8');
            data = JSON.parse(existingData);
        } catch (error) {
            console.error(`Error reading existing JSON file: ${error.message}`);
            // If JSON is malformed, start fresh
            data = [];
        }
    }

    // Get list of PDF files
    let pdfFiles = [];
    try {
        const files = await fs.readdir(PDF_FOLDER);
        pdfFiles = files.filter(file => path.extname(file).toLowerCase() === '.pdf');
    } catch (error) {
        console.error(`Error reading PDF folder: ${error.message}`);
        process.exit(1);
    }

    console.log(`Found ${pdfFiles.length} PDF file(s) in ${PDF_FOLDER}.\n`);

    let processed = 0;
    let total = pdfFiles.length;

    for (const [index, file] of pdfFiles.entries()) {
        const pdfName = file;
        const paperName = path.basename(file, path.extname(file)); // Derive paper name from filename

        // Check if already processed
        if (data.some(entry => entry.paperName === paperName)) {
            console.log(`Skipping already processed PDF (${index + 1}/${total}): ${pdfName}\n`);
            continue;
        }

        const pdfPath = path.join(PDF_FOLDER, file);
        const text = await extractTextFromPDF(pdfPath);

        if (!text.trim()) {
            console.log(`No text found in (${index + 1}/${total}): ${pdfName}. Skipping.\n`);
            continue;
        }

        console.log(`Processing (${index + 1}/${total}): ${pdfName}`);

        const insights = await getInsightsFromGPT(text, paperName);
        if (insights === null) {
            console.log(`Failed to get insights for (${index + 1}/${total}): ${pdfName}. Skipping.\n`);
            continue;
        }

        // Append to data
        data.push({
            paperName,
            bibliographicReference: insights.bibliographicReference,
            insights: insights.insights || [],
            paperTitle: insights.paperName
        });

        processed += 1;

        // Backup periodically
        if (processed % BACKUP_INTERVAL === 0) {
            try {
                await fs.writeJson(OUTPUT_JSON, data, { spaces: 4, encoding: 'utf-8' });
                console.log(`Backup saved after processing ${processed} PDFs.\n`);
            } catch (error) {
                console.error(`Error saving backup JSON: ${error.message}\n`);
            }
        }

        // Respect rate limits
        await new Promise(resolve => setTimeout(resolve, 1000)); // 1 second delay
    }

    // Final save
    try {
        await fs.writeJson(OUTPUT_JSON, data, { spaces: 4, encoding: 'utf-8' });
        console.log(`Processing complete. Total PDFs processed: ${processed}`);
        console.log(`Results saved to ${OUTPUT_JSON}.\n`);
    } catch (error) {
        console.error(`Error saving final JSON file: ${error.message}`);
    }
}

main();
