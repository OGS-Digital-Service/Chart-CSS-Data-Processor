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
        # Assuming a list of dictionaries, inspect the first item
        if isinstance(data[0], dict):
            return list(data[0].keys())
    elif isinstance(data, dict):
        # If it's a single dictionary where keys represent data points
        first_val = next(iter(data.values()))
        if isinstance(first_val, dict):
            return list(first_val.keys())
    return []


def format_dataset(data, target_key):
    """Adds the 'graphValue' key to each data point based on user selection."""
    modified_count = 0

    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict) and target_key in item:
                item["graphValue"] = item[target_key]
                modified_count += 1

    elif isinstance(data, dict):
        for key, item in data.items():
            if isinstance(item, dict) and target_key in item:
                item["graphValue"] = item[target_key]
                modified_count += 1

    print(f"\nSuccessfully updated {modified_count} data points!")
    return data


def save_json_data(data, output_path):
    """Saves the modified JSON data to a file."""
    with open(output_path, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Formatted dataset saved to: {output_path}")


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

    print("\n--- Available Fields for Graphing ---")
    for index, key in enumerate(keys, 1):
        print(f"[{index}] {key}")

    # 3. User selects the key
    while True:
        try:
            choice = int(
                input(
                    f"\nSelect the number (1-{len(keys)}) you want to use as 'graphValue': "
                )
            )
            if 1 <= choice <= len(keys):
                selected_key = keys[choice - 1]
                break
            print("Invalid selection. Please choose a number from the list.")
        except ValueError:
            print("Please enter a valid integer.")

    print(f"\nSelected field: '{selected_key}'")

    # 4. Process the data
    formatted_data = format_dataset(data, selected_key)

    # 5. Save the output
    base, ext = os.path.splitext(file_path)
    output_path = f"{base}_formatted{ext}"
    save_json_data(formatted_data, output_path)


if __name__ == "__main__":
    main()