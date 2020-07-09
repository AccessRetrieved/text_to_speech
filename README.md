# Python text to speech

This is a text to speech program build in python.

## Installation

Packages needed:
- itertookls
- gtts
- os

`pip install gtts`

## Inputs

### Usinng input

```
import itertools
from gtts import gTTS 
import os 
from time import sleep

mytext = input('Text: ')
  
#Language we want to use 
language = 'en'
  

myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("output.mp3") 

#Play the converted file 
os.system("start output.mp3")
sleep(5)
print('file played and removed')
sleep(5)
os.remove('output.mp3')
```

### Using text from script (not recommended)

```
import itertools
from gtts import gTTS 
import os 
from time import sleep

mytext = 'Your text here'
  
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
```
