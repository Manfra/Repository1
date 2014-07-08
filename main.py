def Check():
    n = 0
    for line in f:
        n = n + line.upper().count(s.upper())
    print 'The word is found', n ,'times'

while True:
    try:
        f = open(raw_input('Type the path of the .txt file:'))
        print 'File successfully open'
        break
    except IOError:
        print 'Error: File does not appear to exist.'
        
s = raw_input('Enter the word you will found in the text: ')
print 'Searching:', s
Check()
f.close()
