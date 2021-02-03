import os ## Требуется для os.path и поиска пути директории
import youtube_dl  # импортирую библиотеку
import time
import ffmpeg
ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
with ydl:
    result = ydl.extract_info(  ##извлекаем информацию о видеофайле из ссылки
        'https://www.youtube.com/watch?v=hVivvHS4QZQ',  ## ссылка на видеофайл
        download=False  ## Скачать информацию True False
    )

if 'entries' in result:
    # Если плейлист или список
    video = result['entries'][0]
else:
    ## просто видео
    video = result




slovar = video.keys()

videos = video['formats'][6]['url']
print(video['formats'][6]['url'])
audios = video['formats'][3]['url']
print(video['formats'][3]['url'])

import random
import wget
namefile = 'hehes'+ str(random.randint(0,999))
print(namefile)

wget.download(videos, namefile+".mpeg")
#wget.download(audios, "yt_sound.mp3")


path_vid = os.path.join(os.getcwd(), 'yt_vid.mpeg') ## Путь до видеофайла
path_audio = os.path.join(os.getcwd(), 'yt_sound.mp3') ## Путь до аудиофайла




import youtube_dl





ydl_opts = {
'format': 'bestaudio/best', # choice of quality
'extractaudio' : True, # only keep the audio
'audioformat' : "mp3", # convert to mp3
'outtmpl': f"{os.path.join(os.getcwd(), namefile)}.mp3", #name
'noplaylist' : True, # download single, not playlist
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=hVivvHS4QZQ'])

start_time = time.time()
import speech_recognition as sr
from os import path
from pydub import AudioSegment

AudioSegment.converter = "ffmpeg.exe"
AudioSegment.ffmpeg = "ffmpeg.exe"
AudioSegment.ffprobe ="ffprobe.exe"

# convert mp3 file to wav
sound = AudioSegment.from_file(namefile+".mp3")
#first_20_seconds = sound[:20000]
beginning = sound
beginning.export("outputfile.wav", format="wav")



from speech_recognition import *
import speech_recognition

sample_audio = speech_recognition.AudioFile('outputfile.wav')
r = sr.Recognizer()
with sr.AudioFile('outputfile.wav') as source:
    audio = r.record(source)  # read the entire audio file

print(type(audio))

massslov = []

try:
    # Just pass a language parameter
    out =  r.recognize_sphinx(audio, language="en-US")
    massslov.append(out)
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))


print("--- %s seconds ---" % (time.time() - start_time))
print(massslov)

from deep_translator import GoogleTranslator

to_translate = massslov[0]
translated = GoogleTranslator(source='auto', target='ru').translate(to_translate)

print(translated)



from gtts import gTTS
import os

text = translated

language = 'ru'

speech = gTTS(text = text, lang = language, slow = False)

speech.save("text.mp3")

#os.system("start text.mp3")



from mhmovie import *

m = Movie(namefile+".mpeg")
mu = Music('text.mp3')

final = m+mu
final.save(namefile+"film.mp4")