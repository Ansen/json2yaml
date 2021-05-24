#!/usr/bin/env python3
import json
import yaml
import sys

def main():
    json_file = sys.argv[1]

    file_name = json_file.split('.')[0]

    yaml_file = file_name + '.yaml'

    with open(json_file, 'r') as f:
        data = json.loads(f.read())

    with open(yaml_file, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, encoding='utf-8',  allow_unicode=True)

if __name__ == '__main__':
    main()