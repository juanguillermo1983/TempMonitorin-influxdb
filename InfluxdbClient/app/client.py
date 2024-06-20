import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import random



# Función para generar valores aleatorios
def generar_valores():
    nodo = "MTX1"
    sensores = {
        "S1": {"tipo": "Cloro", "valor": random.uniform(0, 100)},
        "S2": {"tipo": "Presion", "valor": random.uniform(2, 3.5)},
        "S3": {"tipo": "Caudal", "valor": random.uniform(15, 18)},
        "S4": {"tipo": "Presion", "valor": random.uniform(2, 3.5)}
    }
    return nodo, sensores

#token = os.environ.get("INFLUXDB_TOKEN")
token ="i0z5f5--18rdfEV-K1ynQDaU0_dF9Tk3wSklYnynzHb6XYqH1oC6X6NOjI6oy9vx4hVKPqlq3h3u0sbqcQytMA=="
org = "influxDev"
url = "http://192.168.68.107:8086"

write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

bucket="CDP1"

write_api = write_client.write_api(write_options=SYNCHRONOUS)
   
# Enviar valores generados a InfluxDB
for i in range(500):
    nodo, sensores = generar_valores()
    print(f"Iteración {i+1}")
    for sensor, datos in sensores.items():
        point = (
            Point(nodo)
            .tag("sensor", sensor)
            .tag("tipo", datos["tipo"])
            .field("valor", datos["valor"])
        )
        write_api.write(bucket=bucket, org=org, record=point)
        print(f"Escribiendo punto: nodo={nodo}, sensor={sensor}, tipo={datos['tipo']}, valor={datos['valor']:.2f}")
    time.sleep(1)  # separar los puntos por 1 segundo