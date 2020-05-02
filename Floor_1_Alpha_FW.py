
import sys
import csv
import json


def compare(input_json):
    with open(input_json) as f:
        data = json.load(f)
    content = []

    for butler_rec in data:
        d = {'butler_id': butler_rec['butler_id']}
        d.update({'ip': butler_rec['ip'], 'butler_version': butler_rec['butler_version']})
        for counter, each_subsystem in enumerate(butler_rec['butler_subsystem_relations']):
            d.update({f'subsystem_version_{counter}': each_subsystem['version_number'],
                      f'subsystem_subsystem_{counter}': each_subsystem['subsystem']})
        content.append(d)

    keys = content[0].keys()
    with open("Floor_1_Alpha_FW.csv", "w") as f:
        dw = csv.DictWriter(f, keys)
        dw.writeheader()
        dw.writerows(content)


if len(sys.argv) != 2:
    print("\nUsage: python3 json_to_csv.py <JSON_FILE_NAME>\n")
    raise Exception
json_file = sys.argv[1]
compare(json_file)
