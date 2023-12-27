import requests

baseUrl = "http://api.weatherapi.com/v1"
testUrl = "http://api.weatherapi.com/v1/current.json?key=c69cac9f370144a4baa212601232712&q=92071"
request = requests.get(testUrl);

if (request.status_code == 200):
    data = request.json();
    print("RESPONSE: ", data);
    print("CITY NAME:", data.get('location', {}).get('name', 'N/A'));
    print("WEATHER:", data.get('current', {}).get('condition', {}).get('text', 'N/A'));
    print("FARENHEIT:", data.get('current', {}).get('temp_f', 'N/A'));
    print("CELCIUS:", data.get('current', {}).get('temp_c', 'N/A'));
else:
    print("ERROR: ", request.status_code, request.text);

