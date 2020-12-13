import speech_recognition as sr
import pyttsx3


def text_to_speech(command):
    """
    General function to convert text to speech
    :param command: text (type:string)
    :return: speech
    """
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


def hear_speech():
    """
    General function to hear the speaker.
    :return: Text data of the interpreted message (type:string)
    """
    print('Please speak and wait...')
    while (1):
        try:
            with sr.Microphone() as source2:
                # print('Please wait while we adjust the surrounding noise.')
                r.adjust_for_ambient_noise(source2, duration=0.2)
                # listens for the user's input
                audio2 = r.listen(source2)
                data = r.recognize_google(audio2)

        except sr.UnknownValueError:
            data = 0
        if data != 0:
            print('Recognizing...')
            return data


def text_dict(text):
    """
    General function for information extraction from text
    :param text: input text from speaker (type:string)
    :return: output text to be spoken (type:string)
    """
    hey_words = {'hello', 'hey', 'hi', 'heya', 'hiya', 'hai'}
    fine_words = {'fine', 'good', 'splendid', 'amazing', 'well', 'lovely', 'cool'}
    bye_words = {'goodbye', 'bye', 'adios'}
    thank_words = {'thanks', 'thank'}
    notes_words = {'notes', 'note'}
    tokens = set(text.split())

    if len(notes_words.intersection(tokens)) > 0:
        text = 'Ok sure. Please tell me what to note down.'

    elif len(fine_words.intersection(tokens)) > 0:
        text = '''Good to hear that. How may I help you?'''

    elif len(hey_words.intersection(tokens)) > 0:
        text = '''Hi Shivek. How are you doing today?'''

    elif len(thank_words.intersection(tokens)) > 0:
        text = '''You are welcome. Can I help you with anything else?'''

    elif len(bye_words.intersection(tokens)) > 0 or 'see you' in text or 'see ya' in text or 'no thank' in text:
        text = '''Ok goodbye!'''


    else:
        text = '''Sorry, I didn't get you. Can you please repeat?'''
    return text


if __name__ == '__main__':
    # Initialize the recognizer
    data = ''
    flag = 0
    while (data != '9fb123'):

        r = sr.Recognizer()
        data = hear_speech()
        print('\nSpeaker: ', data)
        if flag != 1:
            text = text_dict(data)
        if flag == 1:
            f = open('notes.txt', 'w')
            f.write(data)
            f.close()
            text_to_speech('Note written and saved. Is there anything else?')
            print('Assistant: Note written and saved. Is there anything else? \n')
            flag = 0
            continue
        if text == 'Ok sure. Please tell me what to note down.':
            flag = 1
        print('Assistant: ', text)
        print('\n')
        text_to_speech(text)
        if text == 'Ok goodbye!':
            break
