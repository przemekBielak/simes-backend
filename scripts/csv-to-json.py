import csv
import json
from datetime import datetime, timedelta
from django.utils import timezone

# encoding to remove \ufeff at the beginning of csv file
with open('data.csv', 'r',  encoding='utf-8-sig') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    pk_iter = 0
    data = []
    time = datetime.now(tz=timezone.utc)

    for row in csv_reader:
        data.append(
            {
                "model": "server.sensor1",
                "pk": pk_iter,
                "fields": {
                    "voltage": float(row["voltage1"]),
                    "current": float(row["current1"]),
                    "power": float(row["power1"]),
                    "temperature": float(row["temperature1"]),
                    "energy": float(row["energy1"]),
                    "charge": float(row["charge1"]),
                    "time": time.__str__()
                }
            },
        )
        data.append(
            {
                "model": "server.sensor2",
                "pk": pk_iter,
                "fields": {
                    "voltage": float(row["voltage2"]),
                    "current": float(row["current2"]),
                    "power": float(row["power2"]),
                    "temperature": float(row["temperature2"]),
                    "energy": float(row["energy2"]),
                    "charge": float(row["charge2"]),
                    "time": time.__str__()
                }
            },
        )
        data.append(
            {
                "model": "server.sensor3",
                "pk": pk_iter,
                "fields": {
                    "voltage": float(row["voltage3"]),
                    "current": float(row["current3"]),
                    "power": float(row["power3"]),
                    "temperature": float(row["temperature3"]),
                    "energy": float(row["energy3"]),
                    "charge": float(row["charge3"]),
                    "time": time.__str__()
                }
            },
        )
        data.append(
            {
                "model": "server.sensor4",
                "pk": pk_iter,
                "fields": {
                    "voltage": float(row["voltage4"]),
                    "current": float(row["current4"]),
                    "power": float(row["power4"]),
                    "temperature": float(row["temperature4"]),
                    "energy": float(row["energy4"]),
                    "charge": float(row["charge4"]),
                    "time": time.__str__()
                }
            },
        )
        data.append(
            {
                "model": "server.sensor5",
                "pk": pk_iter,
                "fields": {
                    "voltage": float(row["voltage5"]),
                    "current": float(row["current5"]),
                    "power": float(row["power5"]),
                    "temperature": float(row["temperature5"]),
                    "energy": float(row["energy5"]),
                    "time": time.__str__()
                }
            },
        )
        pk_iter += 1
        time += timedelta(seconds=5)

    for i in range(pk_iter):
        data.append(
            {
                "model": "server.data",
                "pk": i,
                "fields": {
                    "sensor1": i,
                    "sensor2": i,
                    "sensor3": i,
                    "sensor4": i,
                    "sensor5": i
                }
            }
        )

    # out = json.dumps(data, ensure_ascii=False, indent=4)

    with open('data.json', 'w') as f:
        json.dump(data, f)
