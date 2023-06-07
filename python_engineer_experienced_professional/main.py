import json
from common.toolbox import n2w, get_data_type, verify_filepath


def get_schema(data_filepath, schema_filepath) -> str:
    # Verify filepaths
    if not verify_filepath(data_filepath) or not verify_filepath(schema_filepath):
        return {}

    try:
        # Read input JSON data
        with open(data_filepath) as data_file:
            data_content = json.load(data_file)

        # Get the "message" attribute from JSON, or an empty dictionary if it doesn't exist
        message = data_content.get("message", {})

        schema = {}
        key_value = 0

        for attr, value in message.items():
            key_value += 1
            schema[f"key_{n2w(key_value)}"] = {
                "type": get_data_type(value),
                "tag": "",
                "description": "",
                "required": False
            }

        # Convert schema to JSON and write to the output filepath
        with open(schema_filepath, 'w') as schema_file:
            json.dump(schema, schema_file, indent=4)

    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        return {}

    return schema

if __name__ == "__main__":
    for i in range(1,3):
        print()
        print(f'data/data_{i}.json', f"schema/schema_{i}.json")
        print()
        get_schema(f'data/data_{i}.json', f"schema/schema_{i}.json")
