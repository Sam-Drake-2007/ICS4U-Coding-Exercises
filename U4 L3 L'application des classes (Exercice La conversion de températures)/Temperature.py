class Temperature:
    
    def __init__(self):
        self._fltKelvin = 0
        self._fltCelcius = -273.15
        self._fltFahrenheit = -459.67
    
    def setKelvin(self, k):
        if k >= 0:
            self._fltKelvin = k
            self._fltCelcius = k - 273.15
            self._fltFahrenheit = (k - 273.15) * (9/5) + 32
        else:
            print("Peut pas avoir de température en dessous du zéro absolu.")
    def getKelvin(self):
        return self._fltKelvin

    def setCelsius(self, c):
        self._fltKelvin = c + 273.15
        self._fltCelcius = c
        self._fltFahrenheit = c * (9/5) + 32
    def getCelsius(self):
        return self._fltCelcius

    def setFahrenheit(self, f):
        self._fltKelvin = (f - 32) * (5/9) + 273.15
        self._fltCelcius = (f - 32) * (5/9)
        self._fltFahrenheit = f
    def getFahrenheit(self):
        return self._fltFahrenheit