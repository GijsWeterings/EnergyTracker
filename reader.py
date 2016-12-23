"""
You probably want to run this as a deamon on startup
"""
from smeterd.meter import SmartMeter
import sys
import os
import time
import pyrebase
from time import sleep

meter = SmartMeter("/dev/ttyUSB0")
meter.serial.baudrate = 115200
meter.connect()

api = os.environ["APIKEY"]

config = {
    "apiKey": "AIzaSyC9cO-6W6SJ5oz8I_8Ewysf3S2E9Ubx-KQ",
    "authDomain": "energytracking-65210.firebaseapp.com",
    "databaseURL": "https://energytracking-65210.firebaseio.com",
    "storageBucket": "energytracking-65210.appspot.com",
    "serviceAccount": "sdk-key.json"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

token = auth.create_custom_token("your_custom_id")
user = auth.sign_in_with_custom_token(token)

db = firebase.database()

while True:
    try:
        raw_packet = meter.read_one_packet()
        print raw_packet._keys['gas']['valve']

        timestamp = str(int(time.time()))
        data = {}
	data['timestamp'] = timestamp
        data['gas'] = {}
        data['kwh'] = {}
        data['gas']['valve'] = raw_packet._keys['gas']['valve']
        data['gas']['total'] = raw_packet._keys['gas']['total'] #m3
        data['kwh']['current_consumed'] = raw_packet._keys['kwh']['current_consumed'] #kW
        data['kwh']['high_total'] = raw_packet._keys['kwh']['high']['consumed'] #kW
        data['kwh']['low_total'] = raw_packet._keys['kwh']['low']['consumed'] #kW
        
        
        db.child("usage").add(data)

        # sleep for 5 minutes
        sleep(300)
    except P1PacketError:
        continue
    except KeyboardInterrupt:
        meter.disconnect()
        sys.exit()
