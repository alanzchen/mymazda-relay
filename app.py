from flask import Flask, request, jsonify
from urllib.parse import urlparse, parse_qs
import pymazda
import requests
import re

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<p>Your MyMazda Relay is working.</p>"

@app.post("/vehicles")
async def getVehicles() -> None:
  r = request.json
  username = r.get('username')
  password = r.get('password')
  region = r.get('region') or "MNAO"
  client = pymazda.Client(username, password, region)
  vehicles = await client.get_vehicles()
  # Close the session
  await client.close()
  return jsonify(vehicles)

@app.post("/startEngine")
async def startEngine() -> None:
  r = request.json
  username = r.get('username')
  password = r.get('password')
  region = r.get('region') or "MNAO"
  vid = r.get('vid')
  client = pymazda.Client(username, password, region)
  await client.start_engine(vid)
  await client.close()
  return "Success"

@app.post("/stopEngine")
async def stopEngine() -> None:
  r = request.json
  username = r.get('username')
  password = r.get('password')
  region = r.get('region') or "MNAO"
  vid = r.get('vid')
  client = pymazda.Client(username, password, region)
  await client.stop_engine(vid)
  await client.close()
  return "Success"

@app.post("/lockDoors")
async def lockDoors() -> None:
  r = request.json
  username = r.get('username')
  password = r.get('password')
  region = r.get('region') or "MNAO"
  vid = r.get('vid')
  client = pymazda.Client(username, password, region)
  await client.lock_doors(vid)
  await client.close()
  return "Success"

@app.post("/unlockDoors")
async def unlockDoors() -> None:
  r = request.json
  username = r.get('username')
  password = r.get('password')
  region = r.get('region') or "MNAO"
  vid = r.get('vid')
  client = pymazda.Client(username, password, region)
  await client.unlock_doors(vid)
  await client.close()
  return "Success"

@app.post("/hazardLightsOn")
async def turn_on_hazard_lights() -> None:
  r = request.json
  username = r.get('username')
  password = r.get('password')
  region = r.get('region') or "MNAO"
  vid = r.get('vid')
  client = pymazda.Client(username, password, region)
  await client.turn_on_hazard_lights(vid)
  await client.close()
  return "Success"

@app.post("/hazardLightsOff")
async def turn_off_hazard_lights() -> None:
  r = request.json
  username = r.get('username')
  password = r.get('password')
  region = r.get('region') or "MNAO"
  vid = r.get('vid')
  client = pymazda.Client(username, password, region)
  await client.turn_off_hazard_lights(vid)
  await client.close()
  return "Success"

@app.post("/sendPOI")
async def sendPOI() -> None:
  r = request.json
  username = r.get('username')
  password = r.get('password')
  region = r.get('region') or "MNAO"
  vid = r.get('vid')
  latitude = float(r.get('latitude'))
  longitude = float(r.get('longitude'))
  name = r.get('name')
  client = pymazda.Client(username, password, region)
  await client.send_poi(vid, latitude, longitude, name)
  await client.close()
  return "Success"

@app.post("/sendPOIfromURL")
async def sendPOIfromURL() -> None:
  r = request.json
  username = r.get('username')
  password = r.get('password')
  region = r.get('region') or "MNAO"
  vid = r.get('vid')
  u = urlparse(r.get('url'))
  q = parse_qs(u.query)
  if u.hostname == "maps.apple.com":
    name = q.get('q')[0]
    ll = q.get('ll')[0].split(',')
    latitude = float(ll[0])
    longitude = float(ll[1])
  elif u.hostname == "maps.app.goo.gl":
    res_ = requests.get(r.get('url'))
    latitude, longitude, name = get_google_coordinates(res_.url)
  elif u.hostname == "www.google.com":
    latitude, longitude, name = get_google_coordinates(r.get('url'))
  else:
    return "URL Not Supported Yet."
  client = pymazda.Client(username, password, region)
  await client.send_poi(vid, latitude, longitude, name)
  await client.close()
  return "Success"

def get_google_coordinates(full_gmap_url):
  match = re.findall('place\/(.*?),(.*?)\/', full_gmap_url)
  return float(match[0][0]), float(match[0][1]), "Coordinate from Google Maps"

if __name__ == "__main__":
  app.run(port=5001)