const axios = require('axios');
const xlsx = require('xlsx');
const { callGPT } = require('./gptClient'); // The function you provided
// require('dotenv').config(); // To load API key from .env

// Load the "within_domains.xlsx" file
const inputFilePath = './out/testing-papers-v2.xlsx';
const workbook = xlsx.readFile(inputFilePath);
const sheetName = workbook.SheetNames[0];
const data = xlsx.utils.sheet_to_json(workbook.Sheets[sheetName], {
    header: 1,
}); // Convert sheet to JSON

// Function to fetch abstract based on domain
async function fetchAbstract(url) {
    try {
        const domain = new URL(url).href;

        if (domain.includes('link.springer.com')) {
            // Example for Springer
            const response = await axios.get(url);
            const abstractMatch = response.data.match(
                /<div class="c-article-section__content"[^>]*id="Abs1-content"[^>]*>\s*<p>(.*?)<\/p>/
            );
            return abstractMatch ? abstractMatch[1] : 'Abstract not found';

        } else if (domain.includes('sciencedirect.com')) {
            // Fetch HTML content from the URL
            const response = await axios.get(url);

            // Match the abstract section using a regular expression
            const abstractMatch = response.data.match(
                /<div[^>]*class="abstract author"[^>]*>\s*<h2[^>]*>Abstract<\/h2>\s*<div[^>]*id="abs0010"[^>]*>(.*?)<\/div>\s*<\/div>/s
            );

            if (abstractMatch) {
                let abstract = abstractMatch[1];
                abstract = abstract.replace(/<[^>]+>/g, ''); // Remove HTML tags
                abstract = abstract.replace(/&nbsp;/g, ' ').replace(/&amp;/g, '&'); // Decode HTML entities
                return abstract.trim();
            }

            return 'Abstract not found';
        } else if (domain.includes('ieee.org')) {
            // Example for Taylor & Francis
            const response = await axios.get(url);
            const abstractMatch = response.data.match(
                /<div[^>]*class="u-mb-1"[^>]*>\s*<h2[^>]*> Abstract:<\/h2>\s*<div[^>]*>(.*?)<\/div>\s*<\/div>/
            );
            return abstractMatch ? abstractMatch[1] : 'Abstract not found';
        } else if(domain.includes('dl.acm.org')) {
            const response = await axios.get(url);

            // Match the abstract section using a regular expression
            const abstractMatch = response.data.match(
                /<section[^>]*id="abstract"[^>]*>\s*<h2[^>]*>Abstract<\/h2>\s*<div[^>]*role="paragraph"[^>]*>(.*?)<\/div>\s*<\/section>/
            );

            // Return the extracted abstract text or a default message if not found
            return abstractMatch ? abstractMatch[1].trim() : 'Abstract not found';
        } else if (domain.includes('mdpi.com')) {
            // Fetch HTML content from the URL
            const response = await axios.get(url);

            // Match the abstract section using a regular expression
            const abstractMatch = response.data.match(
                /<section[^>]*class="html-abstract"[^>]*>\s*<h2[^>]*>Abstract<\/h2>\s*<div[^>]*class="html-p"[^>]*>(.*?)<\/div>\s*<\/section>/s
            );

            // Clean the abstract text: remove HTML tags and decode HTML entities
            if (abstractMatch) {
                let abstract = abstractMatch[1];
                abstract = abstract.replace(/<[^>]+>/g, ''); // Remove HTML tags
                abstract = abstract.replace(/&nbsp;/g, ' ').replace(/&amp;/g, '&'); // Decode HTML entities
                return abstract.trim();
            }

            return 'Abstract not found';
        }
        else if (domain.includes('arxiv.org')) {
            // Fetch HTML content from the URL
            const response = await axios.get(url);

            // Match the abstract section using a regular expression
            const abstractMatch = response.data.match(
                /<blockquote[^>]*class="abstract mathjax"[^>]*>\s*<span[^>]*class="descriptor"[^>]*>Abstract:<\/span>(.*?)<\/blockquote>/s
            );

            // Clean the abstract text: remove HTML tags and decode HTML entities
            if (abstractMatch) {
                let abstract = abstractMatch[1];
                abstract = abstract.replace(/<[^>]+>/g, ''); // Remove HTML tags
                abstract = abstract.replace(/&nbsp;/g, ' ').replace(/&amp;/g, '&'); // Decode HTML entities
                return abstract.trim();
            }

            return 'Abstract not found';
        } else  if (domain.includes('tandfonline.com')) { // Replace with the actual domain
            // Fetch HTML content from the URL
            const response = await axios.get(url);

            // Match the abstract section using a regular expression
            const abstractMatch = response.data.match(
                /<div[^>]*class="hlFld-Abstract"[^>]*>\s*<h2[^>]*id="abstract"[^>]*>ABSTRACT<\/h2>\s*<p[^>]*>(.*?)<\/p>\s*<\/div>/s
            );

            // Clean the abstract text: remove HTML tags and decode HTML entities
            if (abstractMatch) {
                let abstract = abstractMatch[1];
                abstract = abstract.replace(/<[^>]+>/g, ''); // Remove HTML tags
                abstract = abstract.replace(/&nbsp;/g, ' ').replace(/&amp;/g, '&'); // Decode HTML entities
                return abstract.trim();
            }

            return 'Abstract not found';
        } else if (domain.includes('ieeexplore.ieee.org')) {
            // Fetch HTML content from the URL
            const response = await axios.get(url);

            // Match the abstract section using a regular expression
            const abstractMatch = response.data.match(
                /<div[^>]*class="u-mb-1"[^>]*>\s*<h2[^>]*> Abstract:<\/h2>\s*<div[^>]*xplmathjax[^>]*>(.*?)<\/div>\s*<\/div>/s
            );

            // Clean the abstract text: remove HTML tags and decode HTML entities
            if (abstractMatch) {
                let abstract = abstractMatch[1];
                abstract = abstract.replace(/<[^>]+>/g, ''); // Remove HTML tags
                abstract = abstract.replace(/&nbsp;/g, ' ').replace(/&amp;/g, '&'); // Decode HTML entities
                return abstract.trim();
            }

            return 'Abstract not found';
        }
        else {
            return 'Domain not supported for abstract extraction';
        }
    } catch (error) {
        console.error(`Error fetching abstract for URL ${url}:`, error.message);
        return 'Error fetching abstract';
    }
}

// Main processing function
async function processPapers() {
    const results = [];

    for (const row of data) {
        const [ Title, Year, URL ] = row;
        if (!URL) continue; // Skip rows without a URL

        console.log(`Processing: ${Title}`);
        const abstract = await fetchAbstract(URL); // Fetch abstract based on URL
        // let gptOutput = '';

        // try {
        //     if (abstract !== 'Abstract not found' && abstract !== 'Error fetching abstract') {
        //         gptOutput = await callGPT(`Summarize this abstract: ${abstract}`, 'gpt-4o');
        //     }
        // } catch (error) {
        //     console.error(`Error calling GPT for URL ${URL}:`, error.message);
        // }

        // Store results
        results.push({
            Title,
            Year,
            URL,
            Abstract: abstract,
            // GPT_Summary: gptOutput,
        });
    }

    // Write results to a new Excel file
    const outputWorkbook = xlsx.utils.book_new();
    const outputSheet = xlsx.utils.json_to_sheet(results);
    xlsx.utils.book_append_sheet(outputWorkbook, outputSheet, 'Processed Papers');
    xlsx.writeFile(outputWorkbook, './out/processed_papers.xlsx');

    console.log('Processing complete. Results saved to "processed_papers.xlsx".');
}

// Start processing
processPapers();
