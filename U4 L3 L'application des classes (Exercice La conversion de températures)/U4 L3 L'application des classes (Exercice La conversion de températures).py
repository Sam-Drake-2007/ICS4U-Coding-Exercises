# Utilise la classe temperatureFB pour convertir des valeurs de température à Celcius ou à Fahrenheit
import Temperature

# instanciation / création de l'objet temperature : syntaxe modulename.classname()
temperature = Temperature.Temperature()

print("J'apprends la prog orientée objet")
print("La valeur de la température Kelvin par défaut:", temperature.getKelvin())

# Vérification de la température en degrés Celsius

temperature.setCelsius(100)
print("----- Celsius : Température = 100°C -----")
print(f"Kelvin = {temperature.getKelvin()}")
print(f"Celsius = {temperature.getCelsius()}")
print(f"Fahrenheit = {temperature.getFahrenheit()}")
print()
# Vérification de la température en degrés Fahrenheit
temperature.setFahrenheit(0)
print("----- Fahrenheit : Température = 0°F ----")
print(f"Kelvin = {temperature.getKelvin()}")
print(f"Celsius = {temperature.getCelsius()}")
print(f"Fahrenheit = {temperature.getFahrenheit()}")
print()
# Vérification de la température en kelvin
temperature.setKelvin(0)
print("---- Kelvin : Température = 0°K ----")
print(f"Kelvin = {temperature.getKelvin()}")
print(f"Celsius = {temperature.getCelsius()}")
print(f"Fahrenheit = {temperature.getFahrenheit()}")