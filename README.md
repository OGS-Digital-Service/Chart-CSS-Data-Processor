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


### Data formatter

### SON Graph-Value Formatter
A user-friendly Python script that interactively prepares a JSON dataset for graphing and data tables. It scans your data structure, prompts you to select your target plotting metric, and asks for an identifying label field. It then dynamically appends standardized "graphValue" and "rowHeader" keys to every data point.

This streamlines your data pipeline, making it incredibly easy to feed your records straight into frontend charts, dashboards, or tables without changing your UI code.

Features
Dual-Field Selection: Choose both a numeric metric for plotting (graphValue) and a descriptive label for identification (rowHeader).

Auto-Detects Fields: Automatically inspects your JSON structure and lists all available keys for you.

Interactive CLI Menu: Select your target properties via a simple numbered menu—no risk of typos.

Preserves Original Data: Saves the formatted data to a new file (*_formatted.json), keeping your source data completely safe.

Flexible Structure Support: Works seamlessly with datasets formatted as a list of objects or a dictionary of nested objects.

Prerequisites
Python 3.x installed on your system.

No external dependencies or libraries required (uses Python's standard built-in json and os modules).

How to Use
1. Prepare Your Data
Ensure your JSON file is structured either as an array of objects or a dictionary of objects. For example (analytics.json):

JSON
[
  { "timestamp": "2026-05-24", "clicks": 1420, "conversions": 52 },
  { "timestamp": "2026-05-25", "clicks": 1850, "conversions": 89 },
  { "timestamp": "2026-05-26", "clicks": 1210, "conversions": 41 }
]
2. Run the Script
Open your terminal or command prompt, navigate to the folder containing the script, and execute it:

Bash
python formatter.py
3. Follow the Prompts
Enter the path to your JSON file when prompted.

Choose your graph value (typically a numeric field) from the generated menu by typing its corresponding number.

Choose your row header (typically a date, ID, or name field) from the same menu.