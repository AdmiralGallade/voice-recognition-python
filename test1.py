import speech_recognition as sr

r = sr.Recognizer()

#r.recognize_google

f= sr.AudioFile("filename.wav")
with f as source:
    audio= r.record(source)

