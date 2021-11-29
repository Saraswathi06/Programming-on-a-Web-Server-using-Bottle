from bottle import route,run,request
temp = input("Enter the temperature value (0-70):\n")
hum = input("Enter the humidity value(0-100):\n ")
wind = input("Enter the wind speed value (0-100):\n")
rain = input("Enter the rain value (0-100):\n")
@route ('/')
def getsense():
    sensorLog = [
        {
            'sensor': 'Temperature',
            'value': temp,
},
        {
            'sensor': 'Humidity',
            'value': hum,
        },
        {
            'sensor': 'Windspeed',
            'value': wind,
        },
        {
            'sensor': 'Rain',
            'value': rain
        }
    ]

    return dict(data=sensorLog)
run(host='localhost', port=5500, debug=True)
