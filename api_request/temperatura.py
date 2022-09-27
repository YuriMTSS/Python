from requests_html import HTMLSession
import requests

def temperatura_cidade():
    s = HTMLSession()
    query = 'quixada'

    url = f'https://www.google.com/search?q=wheather+{query}'

    r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 OPR/89.0.4447.64'})

    temperatura = r.html.find('span#wob_tm', first = True).text

    Float = float(temperatura)
    celsius = Float
    kelvin = Float + 273.15
    farenheit = (Float * 1.8) + 32

    printar = "Local: " + query + "\nCelsius: %.2fºC" % celsius + "\nKelvin: %.2fºK" % kelvin + "\nFarenheit: %.2fºF" % farenheit
    return printar


teste = temperatura_cidade()
print(teste)

