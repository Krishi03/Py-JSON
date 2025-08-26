import json

def build_json(data_dict):
    """
    Assembles extracted components into structured JSON.
    """
    return {
        "document": {
            "sections": {
                "content": data_dict.get("text", "No content extracted"),
                "headlines": data_dict.get("headlines", {})
            },
            "key_values": data_dict.get("key_values", {}),
            "tables": data_dict.get("tables", [])
        }
    }
