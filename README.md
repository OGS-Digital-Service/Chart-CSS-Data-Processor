# Chart-CSS-Data-Processor
To format, pre-process, and generate viz using chartCSS as the display tool.


## Data Processor: Relative Value Generator
This script processes JSON datasets to calculate "relative values." It identifies the largest numerical value in a given dataset and uses it as a denominator to create a scaled fraction (0.0 to 1.0) for every other entry.

### Features
- Automatic Max Detection: No need to flag the largest value; the script finds it for you.
- Robust Cleaning: Handles commas, currency symbols, and non-numeric strings (e.g., "N/A") without crashing.
- Non-Destructive: Creates a new file instead of overwriting your source data. Adds -formatted to the json file in the same directory it was processed from.
- Zero-Safe: Includes checks to prevent ZeroDivisionError if the data is empty or invalid.

### Installation
Ensure you have Python 3.x installed on your system. No external libraries are required.

### Usage
Run the script from your terminal or command prompt by passing the path to your JSON file as an argument:
python3 <path to python file>.py <path to json file>.json