import speech_recognition as sr
import requests
import time
import hashlib
import base64
import json
import pyttsx3
# from aip import AipSpeech
from pydub import AudioSegment
import os.path as path

def text_to_speech(sentence: str):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.say(sentence)
    engine.runAndWait()
    voicesc = engine.getProperty('voices')
    for voice in voicesc:
        print("Voice: %s" % voice.name)
        print(" - ID: %s" % voice.id)
        print(" - Languages: %s" % voice.languages)
        print(" - Gender: %s" % voice.gender)
        print(" - Age: %s" % voice.age)
        print("\n")