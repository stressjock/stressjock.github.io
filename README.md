# stressjock.github.io
## matcomp_HTML_ST

## IMPORTANT ##
## The output of the program matcomp_HTML_ST is provided for informational purposes only and must not be used for any serious, commercial, or safety-critical undertaking. The input data has not been validated or verified, and the user ## assumes all risks associated with its use.
## IMPORTANT ##

This is a single-page web application designed in the LCARS (Star Trek) style, intended for uploading, selecting, and comparing material data from a CSV file. The CSV file consists of materials data from MMPDS and is found under the folder "assets".

1. External Resources and Core Setup
Title: Nemesis Blue Standard

CSV Parser: Includes the PapaParse JavaScript library (papaparse@5.4.1/papaparse.min.js) for reading CSV files directly in the browser.

Styling: All styling is embedded within a <style> block.

It uses numerous CSS variables (e.g., --cool, --tangerine, --evening) to define the LCARS color palette and dimensions for bars, panels, and text.

Uses the Antonio font (locally sourced from an assets/ folder, which is outside this HTML file).

Audio: Defines six separate audio files (audio1 through audio6) for sound effects on button clicks.

2. Layout (LCARS Interface)
The page uses a flexible layout consisting of a fixed-width Left Frame (Sidebar) and an expanding Right Frame (Main Content Area).

Top Section (.right-frame-top):
Banner: Displays STARFLEET MATERIAL DATA and the project ID.

Data Cascade: A visually animated section of randomly highlighting numbers (.data-cascade-wrapper).

Navigation Bar: Contains four circular button links (MMPDS, DATA, SPEC, COMPARE).

Status Bar (New): A dedicated section for status messages.

Displays a dynamic Stardate Clock calculated by JavaScript.

Displays the status message: FEDERATION WIDE AREA NETWORK: STATUS OPTIMAL.

Elbow/Bar Segment: A stylized row of colored bars below the banner.

Left Sidebar (.left-frame):
Contains the ship name button (USS Abot NCC-2C01) and several stacked, stylized buttons/panels for status and navigation (e.g., CMDR-VISVANATHA, CAPTAIN-Moosavian).

3. Main Application Functionality
The application logic is controlled by the embedded JavaScript, divided into three main steps:

Step 1: Initialize Dataset
An <input type="file" id="csv-file"> allows the user to upload a CSV file.

The script uses PapaParse to read the data, requiring the CSV to contain columns named 'Basis' and 'Ref' to correctly identify the numerical data properties.

The status changes from WAITING FOR INPUT... to DATASET LOADED. READY. upon success.

Step 2: Select Materials (Controls Area)
Once data is loaded, this section becomes visible.

It generates two <select> dropdown menus (sel-ref and sel-comp) populated with all unique material entries found in the CSV.

Materials are identified using a combined key: ID:X • Material (Basis) – C:Condition • F:Form • T:Thickness.

The INITIATE COMPARISON button calls the runComparison() function.

Step 3: Analysis Output (Results Area)
The runComparison() function:

Retrieves the data rows for the two selected materials (A and B).

Iterates through all identified numerical properties.

Calculates the Percentage Delta between Material B and Material A: ((Value B - Value A) / Value A) * 100.

Renders a table (comparison-table) showing the Property, Value A, Value B, and the color-coded Delta (Green for positive change, Red for negative change).

4. Key JavaScript Functions
generateStardate(): Calculates a dynamic Star Date (formula: (Current Year - 2020) × 1000 + (DayOfYear / 365.25) × 1000).

updateDataCascade(): Randomly applies a highlight class to the scrolling numbers to create a flickering effect.

buildModel(): Processes the raw CSV data into an easily searchable format keyed by the material identifier string.

runComparison(): Performs the core material property comparison and renders the results table.
