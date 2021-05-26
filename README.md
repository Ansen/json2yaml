Convert the input json file to ymal 

Example：
```shell
# Convert a single file: json_file.json ==> json_file.yaml
python3 json2yaml.py json_file.json

# Batch conversion: *.json ==> *.yaml
find backup -type f -name '*.json' -exec python3 json2yaml.py {} \;
```
