import csv
import json

#--Open JSON File and Load to Parser
f=open('/Users/febin.t/febin.json')
jsonData=json.load(f)
f.close

#--Open CSV File in Output Mode
with open('/Users/febin.t/febin.csv', 'w') as f:
    JsonToCSV = csv.writer(f)
    JsonToCSV.writerow(["butler_id", "time", "count"])

    #--Loop thru Each Object or Collection in JSON file
    for item in jsonData:
            JsonToCSV.writerow([
                item["results"]["series"]["values"],
                item["results"]["series"]["values"]])

                # [item["results"]["series"]["tags"]["butler_id"],