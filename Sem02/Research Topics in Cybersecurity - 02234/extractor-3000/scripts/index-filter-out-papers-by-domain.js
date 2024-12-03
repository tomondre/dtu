const xlsx = require('xlsx');
const url = require('url');
// const fs = require('fs');

// List of allowed domains
const allowedDomains = [
  "ieeexplore.ieee.org",
  "link.springer.com",
  "sciencedirect.com",
  "dl.acm.org",
  "tandfonline.com",
  "mdpi.com",
  "arxiv.org"
];

// Load the input Excel file
const inputFilePath = './out/papers.xlsx';
const workbook = xlsx.readFile(inputFilePath);

// Get the first sheet
const sheetName = workbook.SheetNames[0];
const sheet = workbook.Sheets[sheetName];

// Convert the sheet to JSON (with default column indexes since no header is present)
const data = xlsx.utils.sheet_to_json(sheet, { header: 1 }); // Returns data as an array of arrays

// Separate papers based on the domain
const withinDomains = [];
const outsideDomains = [];

// Iterate through rows
data.forEach((row) => {
  // Assume the columns are:
  // Column 0: Title, Column 1: Year, Column 2: URL
  const paperUrl = row[2]; // The URL is in the 3rd column (index 2)

  if (paperUrl) {
    try {
      const parsedUrl = url.parse(paperUrl);
      if (allowedDomains.includes(parsedUrl.hostname)) {
        withinDomains.push({
          Title: row[0],
          Year: row[1],
          URL: row[2]
        });
      } else {
        outsideDomains.push({
          Title: row[0],
          Year: row[1],
          URL: row[2]
        });
      }
    } catch (err) {
      // If URL is invalid, treat it as outside domain
      outsideDomains.push({
        Title: row[0],
        Year: row[1],
        URL: row[2]
      });
    }
  } else {
    // Rows without a URL go to the outsideDomains
    outsideDomains.push({
      Title: row[0],
      Year: row[1],
      URL: row[2]
    });
  }
});

// Write the results to new Excel files
const writeExcelFile = (filename, jsonData) => {
  const worksheet = xlsx.utils.json_to_sheet(jsonData);
  const newWorkbook = xlsx.utils.book_new();
  xlsx.utils.book_append_sheet(newWorkbook, worksheet, "Sheet1");
  xlsx.writeFile(newWorkbook, filename);
};

// Output files
writeExcelFile("./out/within_domains.xlsx", withinDomains);
writeExcelFile("./out/outside_domains.xlsx", outsideDomains);

console.log("Processing complete. Results saved to 'within_domains.xlsx' and 'outside_domains.xlsx'.");

