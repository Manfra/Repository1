f = open('data.txt','r')
def Check(par1):
    for line in f:
        if line.upper().find(s.upper())!= -1:
           par1=par1+1
    if par1 == 0:
        print 'No match found'
    else:
        print 'The word is found', par1 ,'times'
s = raw_input('Enter the word you will found in the text: ')
print 'Searching:', s
Check(0)
f.close()
