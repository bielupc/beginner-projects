# moduls

from twilio.rest import Client
import requests
from bs4 import BeautifulSoup
import PySimpleGUI as sg

# layout

layout = [[sg.Text('SELECCIONA EL SERVEI')],
          [sg.Button('NIVELL DE POL·LEN'), sg.Button('TOP AL·ÈRGENS'), sg.Button("TEMPS"), sg.Button("TOT")]]
window = sg.Window('INFORMACIÓ METEOROLÒGICA I AMBIENTAL', layout)


# funcions


def nivell_polen():
    url = "https://www.eltiempo.es/city.html"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    nivell = soup.find(class_="m_pollen-city").get_text()

    if "Alto" in nivell:
        message = "🌺NIVELL DE POL·LEN: ALT❌"
    if "Bajo" in nivell:
        message = "🌺NIVELL DE POL·LEN: BAIX✅"

    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:',
        body=message,
        to='whatsapp:'
    )


def top_alergens():
    url = "https://www.eltiempo.es/barcelona/polen"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    taula = soup.find(class_="m_table-basic m_pollen-table").get_text()
    message = (f"TOP AL·LÈRGENS🌷 🌹  🌺 🌸 🌼 🌻{taula[25:83]}")

    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+',
        body=message,
        to='whatsapp:+'
    )


def temps():
    url = "https://www.eltiempo.es/manresa.html"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    max1 = soup.find(class_="m_table_weather_day_max_temp").get_text()
    min1 = soup.find(class_="m_table_weather_day_min_temp").get_text()
    plujes = soup.find(class_="m_table_weather_day_child m_table_weather_day_rain").get_text()
    vent = soup.find(class_="m_table_weather_day_wind_ico").get_text()

    message = (f"TEMPS D'AVUI☀🌤🌧🌩🌨                                                     Avui, hi hauràn temperatures màximes de {max1} i mínimes de {min1}. Plouràn {plujes[9:13]} i el vent d'avui "
               f"tindrà una velocitat de {vent[2:8]}.")

    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+',
        body=message,
        to='whatsapp:+'
    )


# mainloop

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    if event == "NIVELL DE POL·LEN":
        nivell_polen()
    if event == "TOP AL·ÈRGENS":
        top_alergens()
    if event == "TEMPS":
        temps()
    if event == "TOT":
        nivell_polen()
        top_alergens()
        temps()

window.close()
