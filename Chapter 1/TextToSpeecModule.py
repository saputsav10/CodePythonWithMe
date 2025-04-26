# Installing a text to speech library in Python and testing it out.
import pyttsx3
engine = pyttsx3.init()
engine.say("Thos who break the rules are scum, but those who abandon their friends are worse than scum, and those who don't care about their friend's feelings are even wors scum.")
engine.runAndWait()