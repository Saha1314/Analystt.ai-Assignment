import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            print("\nWeather Information for", city)
            print("Temperature:", data['main']['temp'], "°C")
            print("Weather:", data['weather'][0]['description'])
            print("Humidity:", data['main']['humidity'], "%")
            print("Wind Speed:", data['wind']['speed'], "m/s")
        else:
            print(f"Error: {data['message']}")
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    api_key = "8d9ea67ff7cfa8299828873b97850f03"
    city = input("Enter the city name: ")

    get_weather(api_key, city)

if __name__ == "__main__":
    main()
