import csv
import json

# encoding to remove \ufeff at the beginning of csv file
with open('data.csv', 'r',  encoding='utf-8-sig') as csv_file:
    fieldnames = ("voltage","current","power","energy","charge_cycles", "temperature", "status", "error", "time")
    fieldnames1 = [s + "1" for s in fieldnames]
    fieldnames2 = [s + "2" for s in fieldnames]

    csv_reader = csv.DictReader(csv_file, delimiter=';')

    pk_iter = 0
    data = []
    for row in csv_reader:
        data.append(
            {
                "model" : "server.sensor1",
                "pk": pk_iter,
                "fields" : {
                    "voltage" : float(row["voltage1"]),
                    "current" : float(row["current1"]),
                    "power" : float(row["power1"]),
                    "energy" : float(row["energy1"]),
                    "charge_cycles" : int(row["charge_cycles1"]),
                    "temperature" : float(row["temperature1"]),
                    "status" : 1,
                    "error" : 0,
                    "time" : row["time"].replace('"', '')
                }
            },
        )
        data.append(
            {
                "model" : "server.sensor2",
                "pk": pk_iter,
                "fields" : {
                    "voltage" : float(row["voltage2"]),
                    "current" : float(row["current2"]),
                    "power" : float(row["power2"]),
                    "energy" : float(row["energy2"]),
                    "charge_cycles" : int(row["charge_cycles2"]),
                    "temperature" : float(row["temperature2"]),
                    "status" : 1,
                    "error" : 0,
                    "time" : row["time"].replace('"', '')
                }
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
        


