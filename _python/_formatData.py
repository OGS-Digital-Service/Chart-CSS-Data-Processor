import json
import os


def load_json_data(file_path):
    """Loads JSON data from a given file path."""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
        return None
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON. Please check the file format.")
        return None


def get_available_keys(data):
    """Extracts unique keys from the dataset to present as options."""
    if isinstance(data, list) and len(data) > 0:
        if isinstance(data[0], dict):
            return list(data[0].keys())
    elif isinstance(data, dict):
        first_val = next(iter(data.values()))
        if isinstance(first_val, dict):
            return list(first_val.keys())
    return []


def format_dataset(data, target_key, header_key):
    """Adds 'graphValue' and 'rowHeader' keys to each data point based on selections."""
    modified_count = 0

    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                if target_key in item:
                    item["graphValue"] = item[target_key]
                if header_key in item:
                    item["rowHeader"] = item[header_key]
                modified_count += 1

    elif isinstance(data, dict):
        for key, item in data.items():
            if isinstance(item, dict):
                if target_key in item:
                    item["graphValue"] = item[target_key]
                if header_key in item:
                    item["rowHeader"] = item[header_key]
                modified_count += 1

    print(f"\nSuccessfully updated {modified_count} data points!")
    return data


def save_json_data(data, output_path):
    """Saves the modified JSON data to a file."""
    with open(output_path, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Formatted dataset saved to: {output_path}")


def get_user_choice(keys, prompt_text):
    """Helper function to handle menu selection validation."""
    while True:
        try:
            choice = int(input(prompt_text))
            if 1 <= choice <= len(keys):
                return keys[choice - 1]
            print(f"Invalid selection. Please choose a number from 1 to {len(keys)}.")
        except ValueError:
            print("Please enter a valid integer.")


def main():
    # 1. Get file input
    file_path = input(
        "Enter the path to your JSON file (e.g., data.json): "
    ).strip()
    data = load_json_data(file_path)

    if data is None:
        return

    # 2. Extract and display available keys
    keys = get_available_keys(data)

    if not keys:
        print(
            "Could not automatically detect nested keys. Ensure your JSON is a list of objects."
        )
        return

    print("\n--- Available Fields in Dataset ---")
    for index, key in enumerate(keys, 1):
        print(f"[{index}] {key}")

    # 3. User selects the key for graphValue
    prompt_graph = f"\nSelect the number (1-{len(keys)}) to use as 'graphValue': "
    selected_graph_key = get_user_choice(keys, prompt_graph)
    print(f"Selected graphValue field: '{selected_graph_key}'")

    # 4. User selects the key for rowHeader
    prompt_header = f"\nSelect the number (1-{len(keys)}) to use as 'rowHeader': "
    selected_header_key = get_user_choice(keys, prompt_header)
    print(f"Selected rowHeader field: '{selected_header_key}'")

    # 5. Process the data
    formatted_data = format_dataset(data, selected_graph_key, selected_header_key)

    # 6. Save the output
    base, ext = os.path.splitext(file_path)
    output_path = f"{base}_formatted{ext}"
    save_json_data(formatted_data, output_path)


if __name__ == "__main__":
    main()