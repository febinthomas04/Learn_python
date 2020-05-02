
import sys
import csv
import json


def compare(input_json):
    with open(input_json) as f:
        data = json.load(f)
    content = []
    for series in data['results'][0]['series']:
        d = dict(zip(series['columns'], series['values'][0]))
        d.update(series["tags"])
        d.update({"name": series["name"]})
        content.append(d)
    keys = content[0].keys()

    with open("test.csv", "w") as f:
        dw = csv.DictWriter(f, keys)
        dw.writeheader()
        dw.writerows(content)


if len(sys.argv) != 2:
    print("\nUsage: python3 json_to_csv.py <JSON_FILE_NAME>\n")
    raise Exception
json_file = sys.argv[1]
compare(json_file)
