from pathlib import Path

import yaml

class YamlParser:
    @staticmethod
    def parse(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.load(f.read(), Loader=yaml.FullLoader)

    @staticmethod
    def get_test_bed():
        with open([p.joinpath('test_bed.yaml') for p in Path(__file__).resolve().parents if p.joinpath('test_bed.yaml').is_file()][0], 'r', encoding='utf-8') as f:
            return yaml.load(f.read(), Loader=yaml.FullLoader)
