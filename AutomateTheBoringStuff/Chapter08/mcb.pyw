#This is for a project on chapter 08 

#Step 1: Comments and shelf setup 

import shelve,pyperclip,sys

mcbshelf = shelve.open('mcb')

#TODO : Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbshelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    #TODO : List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbshelf.keys())))
    elif sys.argv[1] == mcbshelf:
        pyperclip.copy(mcbshelf[sys.argv[1]])
mcbshelf.close()