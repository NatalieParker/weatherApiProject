import requests
from prompt_toolkit.completion import FuzzyCompleter, Completion, Completer
from prompt_toolkit.shortcuts import CompleteStyle, prompt

cities = [
  "Abu Dhabi", "Amsterdam", "Ankara", "Athens", "Auckland", "Bangkok", "Barcelona", "Beijing", "Belgrade", "Berlin",
  "Bogota", "Brasilia", "Brussels", "Bucharest", "Budapest", "Buenos Aires", "Cairo", "Cape Town", "Caracas", "Chicago",
  "Copenhagen", "Dakar", "Delhi", "Dhaka", "Dubai", "Dublin", "Durban", "Edinburgh", "Frankfurt", "Geneva",
  "Hanoi", "Havana", "Helsinki", "Ho Chi Minh City", "Hong Kong", "Istanbul", "Jakarta", "Jerusalem", "Johannesburg", "Kabul",
  "Karachi", "Kathmandu", "Kiev", "Kigali", "Kingston", "Kuala Lumpur", "Lagos", "Lahore", "Lima", "Lisbon",
  "Ljubljana", "London", "Los Angeles", "Luanda", "Madrid", "Manila", "Marrakesh", "Melbourne", "Mexico City", "Miami",
  "Milan", "Minsk", "Montreal", "Moscow", "Mumbai", "Munich", "Nairobi", "New Delhi", "New York", "Oslo",
  "Ottawa", "Paris", "Perth", "Portsmouth", "Prague", "Quito", "Reykjavik", "Rio de Janeiro", "Riyadh", "Rome", "Saint Petersburg",
  "San Francisco", "Santee", "Santiago", "Sao Paulo", "Seoul", "Shanghai", "Singapore", "Stockholm", "Sydney", "Taipei", "Tallinn",
  "Tehran", "Tel Aviv", "Tokyo", "Toronto", "Tripoli", "Tunis", "Ulaanbaatar", "Vienna", "Vilnius", "Warsaw",
  "Washington", "Wellington", "Zagreb", "Zurich"
]

baseUrl = "http://api.weatherapi.com/v1"
request = None;
data = None;

class CityCompleter(Completer):
    def get_completions(self, document, complete_event):
        word = document.get_word_before_cursor();
        for city in cities:
            if word.lower() in city.lower():
                yield Completion(
                    city,
                    start_position=0,
                )

forecastRange = str(10);
getInput = prompt("Enter a city name. \n", completer=FuzzyCompleter(CityCompleter()));
    

while True:
    getUrl = "http://api.weatherapi.com/v1/forecast.json?key=c69cac9f370144a4baa212601232712&q=" + getInput + "&days=" + (forecastRange);
    request = requests.get(getUrl);
    data = request.json();
    if ('error' in data):
        print("Invalid city name, please try again.");
        getInput = prompt(completer=FuzzyCompleter(CityCompleter()));
    else:
        break;

if (request.status_code == 200):
    cityName = data.get('location', {}).get('name', 'N/A');

    if cityName not in cities:
        print("This city is not within range of suggestions. \n");
    
    print(forecastRange + "-Day Forecast for:", cityName);
    forecast = data.get('forecast', {}).get("forecastday", [{}]);
    day = 0

    for date in forecast:
        print("DATE:", data.get('forecast', {}).get("forecastday", [{}])[day].get('date', 'N/A'));
        print("WEATHER:", data.get('current', {}).get('condition', {}).get('text', 'N/A'));
        print("MIN FARENHEIT:", str(data.get('forecast', {}).get("forecastday", [{}])[day].get('day', {}).get('mintemp_f', 'N/A')) +
            ", MAX FARENHEIT:", str(data.get('forecast', {}).get("forecastday", [{}])[day].get('day', {}).get('maxtemp_f', 'N/A')));
        print("MIN CELCIUS:", str(data.get('forecast', {}).get("forecastday", [{}])[day].get('day', {}).get('mintemp_c', 'N/A')) +
            ", MAX CELCIUS: ", str(data.get('forecast', {}).get("forecastday", [{}])[day].get('day', {}).get('maxtemp_c', 'N/A')));
        print();
        day+=1; 
else:
    print("ERROR: ", request.status_code, request.text);