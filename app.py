from fastapi import FastAPI, HTTPException

app = FastAPI()

readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True}
]

def average_temp(devices):
    temp_sum = 0
    count = 0
    for device in devices:
        temp_sum += device["temp"]
        count += 1
    return temp_sum / count

print(average_temp(readings))


def hottest(devices):
    max_temp = 0
    for device in devices:
        if device["temp"] > max_temp:
            max_temp = device["temp"]
    for device in devices:
        if device["temp"] == max_temp:
            return device

hottest(readings)

@app.get("/devices")
async def get_devices():
    return readings

@app.get("/devices/hottest")
async def get_hottest_device():
    return hottest(readings)


@app.get("/devices/online")
async def get_online():
    online_list = []
    for reading in readings:
        if reading["online"] == True:
            online_list.append(reading)
    return online_list
