import itertools
from gtts import gTTS 
import os 
from time import sleep

mytext = input('Text: ')
  
# Language we want to use 
language = 'en'
  

myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("output.mp3") 

# Play the converted file 
os.system("start output.mp3")
sleep(5)
print('file played and removed')
sleep(5)
os.remove('output.mp3')
