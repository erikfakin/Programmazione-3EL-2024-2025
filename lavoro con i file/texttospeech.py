import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(len(voices))
for voice in voices:
    print(voice.id)
    engine.setProperty('voice', voice[0].id)
    engine.say("The quick brown fox jumped over the fence.")

engine.runAndWait()
    
# engine.say("I will speak this text")
# engine.runAndWait()
