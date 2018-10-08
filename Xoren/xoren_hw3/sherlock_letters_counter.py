import sys
f = open('C:/Users/User/Desktop/Sherlock.txt', mode = 'r')
s = f.read().lower()
f.close()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in alphabet:
    print("%s: %s" % (i, s.count(i)))
    
