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
                "model": "server.acdcsensor",
                "pk": pk_iter,
                "fields": {
                    "time": time.__str__(),
                    "voltage1Rms": float(row["acdc_voltage1Rms"]),
                    "voltage2Rms": float(row["acdc_voltage2Rms"]),
                    "voltage3Rms": float(row["acdc_voltage3Rms"]),
                    "current1Rms": float(row["acdc_current1Rms"]),
                    "current2Rms": float(row["acdc_current2Rms"]),
                    "current3Rms": float(row["acdc_current3Rms"]),
                    "pPower": float(row["acdc_pPower"]),
                    "qPower": float(row["acdc_qPower"]),
                    "sPower": float(row["acdc_sPower"]),
                    "pEnergy": float(row["acdc_pEnergy"]),
                    "qEnergy": float(row["acdc_qEnergy"]),
                    "currentThd": 0,
                    "voltageThd": 0,
                    "powerCos": float(row["acdc_powerCos"]),
                    "frequence": float(row["acdc_frequence"]),
                    "status": 0
                }
            },
        )
        data.append(
            {
                "model": "server.dcsensor1",
                "pk": pk_iter,
                "fields": {
                    "time": time.__str__(),
                    "voltageCh1": float(row["dc1_voltageCh1"]),
                    "currentCh1": float(row["dc1_currentCh1"]),
                    "powerDcCh1": float(row["dc1_powerDcCh1"]),
                    "energyDcCh1": float(row["dc1_energyDcCh1"]),
                    "statusCh1": 0,
                    "temperatureCh1": 0,
                    "voltageCh2": 0,
                    "currentCh2": 0,
                    "powerDcCh2": 0,
                    "energyDcCh2": 0,
                    "statusCh2": 0,
                    "temperatureCh2": 0,
                    
                }
            },
        )
        data.append(
            {
                "model": "server.dcsensor2pv",
                "pk": pk_iter,
                "fields": {
                    "time": time.__str__(),
                    "voltageCh1": float(row["dc2_voltageCh1"]),
                    "currentCh1": float(row["dc2_currentCh1"]),
                    "powerDcCh1": float(row["dc2_powerDcCh1"]),
                    "energyDcCh1": float(row["dc2_energyDcCh1"]),
                    "statusCh1": 0,
                    "temperatureCh1": 0,
                    "voltageCh2": float(row["dc2_voltageCh2"]),
                    "currentCh2": float(row["dc2_currentCh2"]),
                    "powerDcCh2": float(row["dc2_powerDcCh2"]),
                    "energyDcCh2": float(row["dc2_energyDcCh2"]),
                    "statusCh2": 0,
                    "temperatureCh2": 0,
                    "lighting": float(row["dc2_lighting"]),
                }
            },
        )
        data.append(
            {
                "model": "server.dcsensor3liion",
                "pk": pk_iter,
                "fields": {
                    "time": time.__str__(),
                    "voltageCh1": float(row["dc3_voltageCh1"]),
                    "currentCh1": float(row["dc3_currentCh1"]),
                    "powerDcCh1": float(row["dc3_powerDcCh1"]),
                    "energyDcCh1": float(row["dc3_energyDcCh1"]),
                    "statusCh1": 0,
                    "temperatureCh1": 0,
                    "charge": 0,
                    "cycles": 0,
                    "voltageCh2": float(row["dc3_voltageCh2"]),
                    "currentCh2": float(row["dc3_currentCh2"]),
                    "powerDcCh2": float(row["dc3_powerDcCh2"]),
                    "energyDcCh2": float(row["dc3_energyDcCh2"]),
                    "statusSoh": 0,
                    "temperatureCh2": 0,
                    "soc": float(row["dc3_soc"]),
                    "capacity": float(row["dc3_capacity"])
                }
            },
        )
        data.append(
            {
                "model": "server.dcsensor4scap",
                "pk": pk_iter,
                "fields": {
                    "time": time.__str__(),
                    "voltageCh1": float(row["dc4_voltageCh1"]),
                    "currentCh1": float(row["dc4_currentCh1"]),
                    "powerDcCh1": float(row["dc4_powerDcCh1"]),
                    "energyDcCh1": float(row["dc4_energyDcCh1"]),
                    "statusCh1": 0,
                    "temperatureCh1": 0,
                    "charge": 0,
                    "cycles": 0,
                    "voltageCh2": float(row["dc4_voltageCh2"]),
                    "currentCh2": float(row["dc4_currentCh2"]),
                    "powerDcCh2": float(row["dc4_powerDcCh2"]),
                    "energyDcCh2": float(row["dc4_energyDcCh2"]),
                    "statusSoh": 0,
                    "temperatureCh2": 0,
                    "soc": float(row["dc4_soc"]),
                    "capacity": float(row["dc4_capacity"])
                    
                }
            },
        )
        data.append(
            {
                "model": "server.dcsensor5charger",
                "pk": pk_iter,
                "fields": {
                    "time": time.__str__(),
                    "voltageCh1": float(row["dc5_voltageCh1"]),
                    "currentCh1": float(row["dc5_currentCh1"]),
                    "powerDcCh1": float(row["dc5_powerDcCh1"]),
                    "energyDcCh1": float(row["dc5_energyDcCh1"]),
                    "statusCh1": 0,
                    "temperatureCh1": 0,
                    "charge": 0,
                    "voltageCh2": float(row["dc5_voltageCh2"]),
                    "currentCh2": float(row["dc5_currentCh2"]),
                    "powerDcCh2": float(row["dc5_powerDcCh2"]),
                    "energyDcCh2": float(row["dc5_energyDcCh2"]),
                    "status": 0,
                    "temperatureCh2": 0,
                    "soc": float(row["dc5_soc"]),
                    "energy": float(row["dc5_energy"])
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
                    "acdc_sensor": i,
                    "dc_sensor1": i,
                    "dc_sensor2pv": i,
                    "dc_sensor3liion": i,
                    "dc_sensor4scap": i,
                    "dc_sensor5charger": i,
                }
            }
        )

    # out = json.dumps(data, ensure_ascii=False, indent=4)

    with open('data.json', 'w') as f:
        json.dump(data, f)
