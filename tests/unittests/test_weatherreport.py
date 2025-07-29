from src.weatherreport import report


def sensorStub():
    return {
        'temperatureInC': 50,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 52
    }


def sensorStubHighPrecipLowWind():
    # High precipitation (>60), low wind-speed (<50)
    return {
        'temperatureInC': 30,
        'precipitation': 70,  # >60
        'humidity': 40,
        'windSpeedKMPH': 40  # <50
    }


def testRainy():
    weather = report(sensorStub)
    print(weather)
    assert("rain" in weather)
    

def testHighPrecipitation():
    # Use the new stub to expose the bug
    weather = report(sensorStubHighPrecipLowWind)
    print(weather)

    # This should ideally predict rain, but currently does not
    assert("rain" in weather.lower())
