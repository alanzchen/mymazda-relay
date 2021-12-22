# Mazda Connected Service Relay

Mazda Connected Service API wrapper based on pymazda and Flask.

# Usage

Make `POST` calls to `https://mymazda.herokuapp.com/{endpoint}`, where `endpoint` could be something like `startEngine`. To make a valid request, you will need to attach a JSON payload with the following fields:

```json
{
  "username": your_mazda_email,
  "password": your_mazda_password,
  "vid": internal_vehicle_id,
}
```

To obtain the `vid` for your vehicle, you can first make a `POST` call to `https://mymazda.herokuapp.com/vehicles` with just the `username` and `password` as the JSON payload. After getting a list of vehicles, find `id` associated with it. It will be the `vid` of your future API requests.

Below are some examples of API usage. To see a full list of API endpoints, see `app.py`. 

## Example: Start / Stop Engine

`POST` the above JSON to `https://mymazda.herokuapp.com/startEngine` or `https://mymazda.herokuapp.com/stopEngine` to start / stop the engine.

## Example: Send navigation destination to infortainment

Send the following JSON to `https://mymazda.herokuapp.com/sendPOI`. Note that you need the navigation SD card for it to work.

```json
{
  "username": your_mazda_email,
  "password": your_mazda_password,
  "vid": internal_vehicle_id,
  "longitude": longitude_float,
  "latitude": latitude_float,
  "name": name
}
```

# iOS Shortcuts Example

 - [Send Apple Maps location to your vehicle](https://www.icloud.com/shortcuts/3e6b090e5b3c43968710d5daf6be3fa0)
 - [Start Engine](https://www.icloud.com/shortcuts/3950a9c831cb4f4eb4122863cfe8fa9b)