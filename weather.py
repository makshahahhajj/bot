import requests

key = 'c745957e5188b4341c8e084600f9caf1'

class Weather:
    def __init__(self, city):
        self.res = ''
        self.data = ''
        self.city = city + ',RU'

    def load_weather(self):
        try:
            self.res = requests.get(
                "http://api.openweathermap.org/data/2.5/find?q=" + self.city + "&type=like&APPID=c745957e5188b4341c8e084600f9caf1")
            self.data = self.res.json()
            temp = str(int(self.data['list'][0]['main']['temp'] - 273.15)) + u"\u2103"
            print(temp)
        except Exception as e:
            print("Exception (find):", e)
            pass
        return temp



