from collections import Counter
import json
import os

# 1. Resolve path to your JSON dataset in the same directory
script_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(script_dir, "_regReform.json")
output_file_path = os.path.join(script_dir, "_reformsSummary.json")

print(f"Reading dataset from: {input_file_path}")

try:
  # 2. Open and load the dataset safely (utf-8-sig handles any hidden BOM headers)
  with open(input_file_path, "r", encoding="utf-8-sig") as f:
    raw_content = f.read().strip()

  if not raw_content:
    print("❌ Error: The JSON file is empty.")
    exit(1)

  data = json.loads(raw_content)
  print(f"Successfully loaded {len(data)} total records!\n")

  # 3. Aggregate total reforms per agency
  counts = Counter(item.get("agency") for item in data if item.get("agency"))

  # Sort by highest total reforms first
  result = [
      {"agency": agency, "total_reforms": count}
      for agency, count in counts.most_common()
  ]

  # 4. Save the aggregated results to a new output JSON file
  with open(output_file_path, "w", encoding="utf-8") as out_f:
    json.dump(result, out_f, indent=2)

  print(f"✅ Aggregation complete! Saved summary to: {output_file_path}\n")

  # 5. Print a clean summary table to the terminal
  print(f"{'Agency':<65} | {'Total Reforms'}")
  print("-" * 83)
  for item in result:
    print(f"{item['agency']:<65} | {item['total_reforms']}")

except FileNotFoundError:
  print(f"❌ Error: Could not find '{input_file_path}'.")
except json.JSONDecodeError as e:
  print(f"❌ JSON Syntax Error: {e.msg} at line {e.lineno}, column {e.colno}")
except Exception as ex:
  print(f"❌ An unexpected error occurred: {ex}")