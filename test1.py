import speech_recognition as sr

r = sr.Recognizer()

#r.recognize_google

f= sr.AudioFile("harvard.wav",duration=4)
with f as source:
    audio= r.record(source)

r.recognize_google(audio)



with f as source:
    audio1 = r.record(source, duration=4)
    audio2= r.record(source,duration=2)

r.recognize_google(audio1)
r.recognize_google(audio2)


with f as source:
    r.adjust_for_ambient_noise(source)      #cuts noise
    audio3 = r.record(source, offset=4, duration=3)

r.recognize_google(audio3) 
