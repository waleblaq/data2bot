import unittest
import json
from jsonschema import validate
from main import get_schema

class TestJsonSchemaSniffer(unittest.TestCase):
    def test_get_schema(self):
        # Define test input and expected output
        data_filepath = 'data/test_data.json'
        schema_filepath = 'schema/test_schema.json'
        expected_schema = {
            "key_one": {
                "type": "string",
                "tag": "",
                "description": "",
                "required": False
            },
            "key_two": {
                "type": "integer",
                "tag": "",
                "description": "",
                "required": False
            }
        }

        # Call the function to generate the schema
        generated_schema = get_schema(data_filepath, schema_filepath)

        # Load the generated schema from the file
        with open(schema_filepath) as schema_file:
            loaded_schema = json.load(schema_file)

        # Assert that the generated schema matches the expected schema
        self.assertEqual(generated_schema, expected_schema)

        # Assert that the loaded schema is a valid JSON schema
        self.assertEqual(loaded_schema, generated_schema)

if __name__ == '__main__':
    unittest.main()
