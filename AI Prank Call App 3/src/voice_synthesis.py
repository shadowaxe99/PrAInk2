import pyttsx3


def synthesize_text(text, voice):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if voice == 'male':
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)
    engine.save_to_file(text, 'audio.mp3')
    engine.runAndWait()
    return 'audio.mp3'