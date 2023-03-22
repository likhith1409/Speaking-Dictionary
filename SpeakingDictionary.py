import json
import pyttsx3
import os
from difflib import get_close_matches
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
engine.setProperty('rate',170)

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")
        print("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
        print("good afternoon")
    else:
        speak("good evening")
        print("good evening")

words_data = json.load(open("data.json"))

def word_meaning(word):
      
    word = word.lower()

    if word in words_data:
        return words_data[word]
      
    elif word.title() in words_data:
        return words_data[word.title()]
      
    elif word.upper() in words_data:
        return words_data[word.upper()]
      
    elif len(get_close_matches(word, words_data.keys())) >0:
      
        similar_words_list = list(map(str, get_close_matches(word, words_data.keys())))
        
        speak("Did you mean %s instead? Enter 'Y' If yes or 'N' if No"% similar_words_list)
        ans = input("Did you mean %s instead? Enter 'Y' If yes or 'N' if No " % similar_words_list)
        
        if ans.lower() == 'y':
            index = input("Enter the position number of word to select the word. Ex 1 or Ex 2 or Ex 3 : ")
            return word_meaning(get_close_matches(word, words_data.keys())[int(index)-1])
        elif ans.lower() == 'n':
            print("Word Doesnt exists. Please double check it!!!")
        else:
            print("Sorry, We don't understand you!!!!")
    else:
        print("Word Doesnt exists. Please double check it!!!")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

wish()
speak("Enter a word:")
word = input("Enter a word :")

print(word_meaning(word))
speak(word_meaning(word))

