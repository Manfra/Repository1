def Check(par):
    for line in f:
        if line.upper().find(s.upper())!= -1:
           par = par+1
    if par == 0:
        print 'No match found'
    else:
        print 'The word is found', par ,'times'

while True:
    try:
        f = open(raw_input('type the path of the .txt file:'))
        print 'File successfully open'
        break
    except IOError:
        print 'Error: File does not appear to exist.'
        
s = raw_input('Enter the word you will found in the text: ')
print 'Searching:', s
Check(0)
f.close()
