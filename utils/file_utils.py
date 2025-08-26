import os
import json

def save_json(input_path, json_obj):
    base = os.path.basename(input_path)
    name, _ = os.path.splitext(base)
    output_path = os.path.join("output", f"{name}.json")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(json_obj, f, indent=4, ensure_ascii=False)

    print(f"✅ Saved JSON: {output_path}")
