import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Sage etwas...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="de-DE")
        print("Du hast gesagt:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, ich habe dich nicht verstanden.")
        return None
    except sr.RequestError as e:
        print("Fehler bei der Spracherkennung: ", e)
        return None

if __name__ == "__main__":
    recognize_speech()
