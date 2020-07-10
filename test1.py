import speech_recognition as sr

r = sr.Recognizer()

#r.recognize_google

f= sr.AudioFile("harvard.wav",duration=4)
with f as source:
    audio= r.record(source)

r.recognize_google(audio)
