import csv
import json

with open('data.csv', 'r') as csv_file:
    fieldnames = ("voltage","current","power","energy","charge_cycles", "temperature", "status", "error", "time")
    fieldnames1 = [s + "1" for s in fieldnames]
    fieldnames2 = [s + "2" for s in fieldnames]

    csv_reader = csv.DictReader(csv_file, delimiter=';')

    pk_iter = 0
    data = []
    for row in csv_reader:
        fieldnames1 = dict(filter(lambda x:x[0].endswith("1"), row.items()))
        fieldnames2 = dict(filter(lambda x:x[0].endswith("2"), row.items()))
        data.append(
            {
                "model" : "server.sensor1",
                "pk": pk_iter,
                "fields" : fieldnames1
            },
        )
        data.append(
            {
                "model" : "server.sensor2",
                "pk": pk_iter,
                "fields" : fieldnames2
            },
        )
        pk_iter += 1

    for i in range(pk_iter):
        data.append(
            {
                "model": "server.data",
                "pk" : i,
                "fields": { 
                        "sensor1": i, 
                        "sensor2": i 
                    }
            }
        )

    out = json.dumps(data, ensure_ascii=False, indent=4)

    print(out)
        


