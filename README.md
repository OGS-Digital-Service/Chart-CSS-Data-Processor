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

### JSON Graph-Value Formatter
A user-friendly Python script that interactively prepares a JSON dataset for graphing. It scans your data structure, prompts you to select which field you want to plot, and dynamically appends a standardized "graphValue" key to every data point. This makes it incredibly easy to pipe your data straight into charting libraries (like Chart.js, D3.js, or matplotlib) without changing your frontend code.

Features
Auto-Detects Fields: Automatically inspects your JSON structure and lists all available keys for you.

Interactive CLI Menu: Select your target graphing metric via a simple numbered menu—no risk of typos.

Preserves Original Data: Saves the formatted data to a new file (*_formatted.json), keeping your source data completely safe.

Flexible Structure Support: Works seamlessly with datasets formatted as a list of objects or a dictionary of nested objects.

Prerequisites
Python 3.x installed on your system.

No external dependencies or libraries required (uses Python's standard built-in json and os modules).

How to Use
1. Prepare Your Data
Ensure your JSON file is structured either as an array of objects or a dictionary of objects. For example (weather_data.json):

JSON
[
  { "date": "2026-05-24", "temperature": 22, "humidity": 60 },
  { "date": "2026-05-25", "temperature": 25, "humidity": 55 },
  { "date": "2026-05-26", "temperature": 21, "humidity": 65 }
]
2. Run the Script
Open your terminal or command prompt, navigate to the folder containing the script, and execute it:

Bash
python3 _formatData.py
3. Follow the Prompts
Enter the path to your JSON file when prompted.

Choose your metric from the generated menu by typing its corresponding number.

Example Terminal Interaction:

Plaintext
Enter the path to your JSON file (e.g., data.json): weather_data.json

--- Available Fields for Graphing ---
[1] date
[2] temperature
[3] humidity

Select the number (1-3) you want to use as 'graphValue': 2

Selected field: 'temperature'

Successfully updated 3 data points!
Formatted dataset saved to: weather_data_formatted.json
Expected Output
The script generates a new file. Following the example above, weather_data_formatted.json will look like this:

JSON
[
  { "date": "2026-05-24", "temperature": 22, "humidity": 60, "graphValue": 22 },
  { "date": "2026-05-25", "temperature": 25, "humidity": 55, "graphValue": 25 },
  { "date": "2026-05-26", "temperature": 21, "humidity": 65, "graphValue": 21 }
]
Now, your graphing utility can always look for the explicit "graphValue" key regardless of what underlying metric you decided to analyze!