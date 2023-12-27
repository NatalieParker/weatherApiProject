import requests

baseUrl = "http://api.weatherapi.com/v1"
request = None;
data = None;

getInput = input("Enter a city name. \n");
forecastRange = str(10);

while True:
    getUrl = "http://api.weatherapi.com/v1/forecast.json?key=c69cac9f370144a4baa212601232712&q=" + getInput + "&days=" + (forecastRange);
    request = requests.get(getUrl);
    data = request.json();
    if ('error' in data):
        print("Invalid city name, please try again.");
        getInput = input();
    else:
        break;


if (request.status_code == 200):
    # print("RESPONSE: ", data);
    print(forecastRange + "-Day Forecast for:", data.get('location', {}).get('name', 'N/A'));
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

