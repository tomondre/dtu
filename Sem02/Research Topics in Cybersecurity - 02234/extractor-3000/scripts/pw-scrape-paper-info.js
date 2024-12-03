const playwright = require('playwright');
const xlsx = require('xlsx');

// Load the Excel file
const inputFilePath = './out/testing-papers-v2.xlsx';
const workbook = xlsx.readFile(inputFilePath);
const sheetName = workbook.SheetNames[0];
const data = xlsx.utils.sheet_to_json(workbook.Sheets[sheetName], {
    header: 1,
}); // Convert sheet to JSON

async function getElementText(page, selector) {
    const element = await page.$(selector);
    if (element) {
        const text = await element.innerText();
        return text.trim();
    } else {
        return 'Abstract not found';
    }
}

async function fetchAbstract(page, url) {
    try {
        const domain = new URL(url).hostname;

        await page.goto(url, { waitUntil: 'networkidle' });

        if (domain.includes('link.springer.com')) {
            // Springer
            return await getElementText(page, 'div.c-article-section__content#Abs1-content');

        } else if (domain.includes('sciencedirect.com')) {
            // ScienceDirect
            return await getElementText(page, 'div.abstract author');

        } else if (domain.includes('dl.acm.org')) {
            // ACM Digital Library
            return await getElementText(page, 'section#abstract > div');

        } else if (domain.includes('mdpi.com')) {
            // MDPI
            return await getElementText(page, 'section.html-abstract > div');
        } else if (domain.includes('arxiv.org')) {
            // arXiv
            return await getElementText(page, 'blockquote.abstract');
        } else if (domain.includes('ieeexplore.ieee.org')) {
            // IEEE Xplore
            return await getElementText(page, 'div.abstract-text');

        } else {
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

    const browser = await playwright.chromium.launch({ headless: true });
    const context = await browser.newContext();

    for (const row of data) {
        const [ Title, Year, URL ] = row;
        if (!URL) continue; // Skip rows without a URL

        console.log(`Processing: ${Title}`);
        const page = await context.newPage();
        const abstract = await fetchAbstract(page, URL); // Fetch abstract based on URL
        await page.close();

        // Store results
        results.push({
            Title,
            Year,
            URL,
            Abstract: abstract,
        });
    }

    await browser.close();

    // Write results to a new Excel file
    const outputWorkbook = xlsx.utils.book_new();
    const outputSheet = xlsx.utils.json_to_sheet(results);
    xlsx.utils.book_append_sheet(outputWorkbook, outputSheet, 'Processed Papers');
    xlsx.writeFile(outputWorkbook, './out/processed_papers.xlsx');

    console.log('Processing complete. Results saved to "processed_papers.xlsx".');
}

// Start processing
processPapers();
