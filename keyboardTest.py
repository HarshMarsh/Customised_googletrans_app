import keyboard
import time
import pyperclip
from googletrans import Translator
counter = 0
translator = Translator()
while True:
    keyPressed=keyboard.read_key()
    if keyPressed == 'f1':
        counter += 1
        time.sleep(2)
    if counter >= 1:
        input_txt = translator.translate(pyperclip.paste(),dest = 'english')
        print(input_txt.text)
        k = translator.translate(input_txt.text,dest = input_txt.src)
        print(k.pronunciation)
        counter = 0

