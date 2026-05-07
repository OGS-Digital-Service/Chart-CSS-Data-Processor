import json
import sys
import os

def safe_clean_val(item):
    """
    Strips non-numeric characters and converts to float.
    Returns 0.0 if the value is invalid or missing.
    """
    try:
        raw_val = item.get('value', '0')
        if not isinstance(raw_val, str):
            raw_val = str(raw_val)
        # Remove commas and any other non-digit chars except decimal points
        clean_str = "".join(c for c in raw_val if c.isdigit() or c == ".")
        return float(clean_str) if clean_str else 0.0
    except (ValueError, TypeError, AttributeError):
        return 0.0

def process_file(input_path):
    # 1. Validate file existence
    if not os.path.exists(input_path):
        print(f"Error: The file '{input_path}' was not found.")
        return

    # 2. Load the data
    try:
        with open(input_path, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print(f"Error: '{input_path}' is not a valid JSON file.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    # 3. Find the maximum value for the denominator
    numeric_values = [safe_clean_val(item) for item in data]
    denominator = max(numeric_values) if numeric_values else 0

    # 4. Generate the new dataset
    new_dataset = []
    for item in data:
        current_num = safe_clean_val(item)
        relative = round(current_num / denominator, 4) if denominator > 0 else 0.0
        
        # Build new object with the relative_value appended
        new_dataset.append({
            **item,
            "relative_value": relative
        })

    # 5. Generate output path
    # Split the path into (directory + filename) and extension
    file_root, file_ext = os.path.splitext(input_path)
    output_path = f"{file_root}-formatted{file_ext}"

    # 6. Save the file
    try:
        with open(output_path, "w") as f:
            json.dump(new_dataset, f, indent=4)
        print(f"Success! Processed data saved to: {output_path}")
    except Exception as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python processor.py <path_to_json_file>")
    else:
        process_file(sys.argv[1])