
def getTempInCelsius(sense):
  temp = sense.get_temperature_from_pressure()
  return temp

def getTempInKelvin(sense):
  temp = sense.get_temperature_from_pressure()
  KTemp = temp + 273
  return KTemp

def getTempInFarenheit(sense):
  temp = sense.get_temperature_from_pressure()
  FTemp = (temp * (9/5)) + 32
  return FTemp
