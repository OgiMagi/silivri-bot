import praw
import requests
import json
import prawConfigs

reddit = praw.Reddit(client_id='_5uCiim-3AwyIg',
                     client_secret='PX103UIlVdXm_zBBv_8DTPFim47Hnw',
                     username='SilivriHavaDurumu',
                     password='silivribotpw',
                     user_agent='bot by OgiMagi')

subreddit = reddit.subreddit('PogacaZencileri+Turkey+TurkeyJerky')

keyphrase = '!silivribot'


# Open Weather Map Base URL'si
baseUrl = "https://api.openweathermap.org/data/2.5/weather?"
city = "Silivri&units=metric"
url = baseUrl + "q=" + city + "&appid=" + "bd9fc5a53ad23f2d5a629404bb8e213b"


response = requests.get(url)
if response.status_code == 200:
    # getting data in the json format
    data = response.json()
    # getting the main dict block
    main = data['main']
    # getting temperature
    temperature = main['temp']
    temperature = int(temperature)
    if temperature <= 15:
        durum = " ve hava gerçekten de soğuk."
    elif temperature > 15:
        durum = " hava pek de soğuk sayılmaz."
    print(f"Silivri'de Hava Şuan {temperature} °C " + durum +
          "\n\n^^Ben bir botum ve bu otomatik bir cevap.")
else:
    # showing the error message
    print("HTTP alımında hata gerçekleşti.")

    # postlama mekanizması


for comment in subreddit.stream.comments():
    if keyphrase in comment.body:
        if not comment.saved:
            temperature = int(main['temp'])
            reply = (f"Silivri'de Hava Şuan {temperature} °C " + durum +
                     "\n\n^^Ben ^^bir ^^botum ^^ve ^^bu ^^otomatik ^^bir ^^cevap.")
            comment.reply(reply)
            comment.save()
            print('posted')
