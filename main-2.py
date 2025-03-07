import json
import requests
from PIL import Image, ImageTk
from io import BytesIO
import tkinter as tk
from datetime import date, timedelta


def weather():
    city_name = 'Yuhang'
    key1 = '2f44ab8d94825710392977b37c24d3ac'
    response1 = requests.post(f'https://api.openweathermap.org'
                              f'/data/2.5/weather?q={city_name}&appid={key1}')
    result1 = json.loads(response1.text)

    print(f"Weather in {city_name}: {result1['weather'][0].get('description')}")
    print(f"Humidity: {result1['main'].get('humidity')}")
    print(f"Pressure: {result1['main'].get('pressure')}")

def news():
    q = 'tesla' # key word
    date_from = '2025-03-01'
    key2 = 'b15d86218ad64cecb75ab4502dc615cc'
    response2 = requests.get(f'https://newsapi.org/v2/everything?'
                     f'q={q}&from={date_from}&sortBy=publishedAt&apiKey={key2}')
    result2 = json.loads(response2.text)

    print(f'Total articles about {q} from {date_from}:'
           f'{result2.get('totalResults')}')
    print("Author, title")

    for i in range(6):
        print(f'{result2.get('articles')[i].get('author')},' 
              f'{result2.get('articles')[i].get('title')}')

def image():
    global date_photo
    date_photo= date.today()

    def next(): # show the previous day image
        global date_photo
        date_photo -= timedelta(days=1)
        response4 = requests.get(f'https://api.nasa.gov/planetary/apod?'
                                 f'api_key={key3}&date={date_photo}')
        data4 = response4.json()
        image_url4 = data4["url"]
        image_response4 = requests.get(image_url4, stream=True)
        image4 = Image.open(BytesIO(image_response4.content))
        image_tk4 = ImageTk.PhotoImage(image4)
        image_label.config(image=image_tk4)
        image_label.image = image_tk4 

    window = tk.Tk()
    window.title('Astronomy Picture of the Day Archive')
    window.geometry('600x600')
    button1 = tk.Button(window, width=5, text='next', command=next)
    button1.pack()
    key3 = 'OGdKMpxptsDcy9f1slyhckVUaztVEVKpec7IqBaO'
    response3 = requests.get(f'https://api.nasa.gov/planetary/apod'
                            f'?api_key={key3}&date={date_photo}')
    data = response3.json()
    image_url = data["url"]
    image_response = requests.get(image_url, stream=True)
    image = Image.open(BytesIO(image_response.content))
    image_tk = ImageTk.PhotoImage(image)
    image_label = tk.Label(window, image=image_tk)
    image_label.pack()


    window.mainloop()

if __name__ == '__main__':
    weather()
    news()
    image()