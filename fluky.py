import time, random
from jikanpy import Jikan
from twython import Twython
from os import environ

jikan = Jikan()

consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']
twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)
auth = twitter.get_authentication_tokens

def getManga():
    print ('GETTING MANGA')
    random_number = random.randint(1, 45)
    random_number2 = random.randint(1, 40)
    archive = (jikan.genre(type='manga', genre_id=random_number)['manga'])
    print (archive[random_number2])
    manga_id = (archive[random_number2]['mal_id'])
    print (f'MANGA ID: {manga_id}')
    return manga_id

def parseManga():
    print ('PARSING MANGA')
    manga_id = getManga()
    manga_title = (jikan.manga(manga_id)['title'])
    manga_status = (jikan.manga(manga_id)['status'])
    manga_score = (jikan.manga(manga_id)['score'])
    manga_url = (jikan.manga(manga_id)['url'])
    print (manga_title)
    print (manga_status)
    print (manga_score)
    print (manga_url)
    return (manga_title, manga_status, manga_score, manga_url)

def tweet():
    (manga_title, manga_status, manga_score, manga_url) = parseManga()
    print ('TWEETING')
    twitter.update_status(status=f'{manga_title} \nStatus: {manga_status} \nScore: {manga_score} \nMAL: {manga_url}')

while True:
    tweet()
    time.sleep(3600)
 


