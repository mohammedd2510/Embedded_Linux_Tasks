from Alexa import Alexa

Alexa.Speak("إزايك يا محمد")

while True:
    text =Alexa.Recognize_Speech()
    Alexa.Respond_to_Speech(text)
