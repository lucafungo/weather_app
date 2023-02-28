
import requests

# this funcion runs in case the city does not exist
def city_not_found():
    print(f'Oops! this city does not exist!\n')

# this function runs in case the city typed exixst and is found
def city_found():
    r = requests.get(url).json()
    temp_in_kelvin = (r['main']['temp'])

    temp_in_celsius = round((float(temp_in_kelvin - 274.15)), 1)
    humidity = (r['main']['humidity'])
    description = (r['weather'][0]['description']).title()
    
    print(f"Looks like the weather in {city_input} is {description}\nThe temperature is {temp_in_celsius}°\nHumidity {humidity}%")

# city input and URL handling
api_key = '<PERSONAL APY KEY GOES HERE>'
city_input = input('Please type a city: ')
url = (f"https://api.openweathermap.org/data/2.5/weather?q={city_input}&appid={api_key}")
api_call = requests.get(url)

# error handling
if (api_call.status_code) == 200:
    city_found()
elif (api_call.status_code) == 404:
    city_not_found()

