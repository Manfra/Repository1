def Check():
    i = 0
    for line in f:
        i += line.upper().count(s.upper())      
    return i                                    
try:
    f = open(raw_input('Type the path of the .txt file:'))
    print 'File successfully open'
    s = raw_input('Enter the word you will found in the text: ')
    print 'Searching:', s
    count = Check()
    print 'The word is found', count ,'times'
except IOError:
    print 'Error: File does not appear to exist.'
f.close()
