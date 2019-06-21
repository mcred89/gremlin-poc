from flask import Flask, jsonify
from geolite2 import geolite2
import pytz
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
  return "Yo"

@app.route("/<dashed_ip>", methods=['GET'])
def get_time(dashed_ip):
  ip = dashed_ip.replace("-", ".")
  reader = geolite2.reader()
  geo_info = reader.get(ip)
  geolite2.close()
  print(geo_info)
  tz = geo_info['location']['time_zone']
  time_obj = pytz.timezone(tz)
  date_time = datetime.now(time_obj)
  time = date_time.strftime("%H:%M:%S")
  return jsonify({'time': time})

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')
