import pyttsx3
import wikipedia
import lxml

#My assistance GhostAI
GhostAI = pyttsx3.init()
voices = GhostAI.getProperty('voices')
GhostAI.setProperty('voice', voices[0].id)

#search wikepedia
GhostAI.say("Search wikipedia")
GhostAI.runAndWait()
In = input("Topic: ")

#number of sentences
GhostAI.say("In how many sentences do you want the result to be")
GhostAI.runAndWait()
lines= input("Number: ")

#result
result = wikipedia.summary(In, sentences = lines)

print(result)
GhostAI.say('According to wikipedia')
GhostAI.say(result)
GhostAI.runAndWait()
