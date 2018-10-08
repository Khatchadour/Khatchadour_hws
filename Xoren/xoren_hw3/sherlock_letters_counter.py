import sys
f = open(sys.argv[1], mode = 'r')
s = f.read().lower()
f.close()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in alphabet:
    print("%s: %s" % (i, s.count(i)))
    
