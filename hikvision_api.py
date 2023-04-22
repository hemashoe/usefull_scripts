from hikvisionapi import Client
from dict2xml import dict2xml
import xml.etree.ElementTree as ET
import time
import mysql.connector
from datetime import datetime


connection = mysql.connector.connect(
        host='localhost',
        database='ulaglar',
        user='root',
        password='Standart1@345',)
cursor = connection.cursor()
print("Connection", connection.is_connected())

body = "<?xml version='1.0' encoding='UTF-8'?><VehicleInfoCond><searchID>1</searchID>"  \
       "<TimeSpan><startTime>2022-06-07T00:00:00Z</startTime><stopTime>2030-05-31T22:59:59Z</stopTime>" \
       "</TimeSpan><maxResults>10000000000000</maxResults><plateLicense /><downloadResultPosition>100</downloadResultPosition></VehicleInfoCond>"

# params = "<?xml version='1.0' encoding='UTF-8'?><Plate version='2.0' count='100' \
#         xmlns='http://www.hikvision.com/ver20/XMLSchema'> </Plate>"

hik = Client("http://*.*.*.*", "admin", "pASSWORD", timeout='30')
now = datetime.now()


def img():
    car_img = hik.Streaming.channels[103].picture(method='get', type='opaque_data')
    filename = "media/photos/" + str(now) + '.png'
    with open(filename, "wb") as surat:
        for ulag_s in car_img.iter_content(chunk_size=254):
            surat.write(ulag_s)
        return filename


def api():
    x_value = []
    y_value = []
    while Client:
        plates = hik.Traffic.vehicleInfoCond(method='get', sdata=body)
        got_xml = dict2xml(plates, indent="  ")
        root = ET.fromstring(got_xml)
        a = root.iterfind(".//VehicleInfo/plateNo")
        b = root.iterfind(".//VehicleInfo/timeSpan")

        for x, y in zip(a, b):
            x_value.append(x.text)
            y_value.append(y.text)

        x_val = x_value[-1]
        y_val = y_value[-1]
        print(x_val, y_val)

        # Do insert to database.
        time.sleep(4)


api()
