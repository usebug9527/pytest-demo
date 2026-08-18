import json
import os


class JsonParser:

    @staticmethod
    def parse_api():
        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, "..", "resources", "api.json")
        with open(path, 'r', encoding='utf-8') as f:
            return json.loads(f.read())

# if __name__ == '__main__':
#     json_data = JsonParser().parse_api()
#     print(json_data)