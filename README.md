Convert the input json file to ymal 

Example：
```shell
# Convert a single file 
python3 json2yaml.py json_file.json

# Batch conversion 
find backup -type f -name '*.json' -exec python3 json2yaml.py {} \;
```