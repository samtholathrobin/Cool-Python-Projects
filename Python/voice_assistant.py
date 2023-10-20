from gtts import gTTS
import speech_recognition as sr
import openai 
from pydub import AudioSegment
from pydub.playback import play

openai.api_key = 'ENTER YOUR API KEY HERE'
messages = [ {"role": "system", "content": 
                "You are a intelligent assistant. And an excellent teacher with a great knowledge in academics. You give precise and consice answers."} ] 

def TTSCK(text):
    l='en'
    speech=gTTS(text=text, lang=l, slow=False, tld="us")
    speech.save("voice.mp3")
    song = AudioSegment.from_mp3("voice.mp3")
    print('Replying with voice')
    play(song)

def SR():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source,2)
        print("Listening :\n")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print(text,end="\n\n")
        GPT(text)

def GPT(text):
    message = text 
    messages.append( {"role": "user", "content": message}, ) 
    chat = openai.ChatCompletion.create(model="gpt-4", messages=messages) 
    reply = chat.choices[0].message.content 
    messages.append( {"role": "assistant", "content": reply}, ) 
    print(reply,end="\n\n")
    TTSCK(reply)

while True:
    SR()
    if input():
        break


