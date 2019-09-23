#!/usr/bin/env python3
import time
pass_counter = 0
pass_lenght = 8

alphabet = ("abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ")

f = open("passwords.txt", "w")
starttime = time.time()
def pass1(pass_counter):
    for i in alphabet:
        pass_counter += 1
        print (i)
    print(pass_counter)
    

for a in alphabet:
    for b in alphabet:
        for c in alphabet:
            for d in alphabet:
                for e in alphabet:
                    for f in alphabet:
                        for g in alphabet:
                            for h in alphabet:
                                pass_counter += 1
                                print(a+b+c+d+e+f+g+h, time.time() - starttime, pass_counter)
print('zabralo to {} sekund'.format(time.time() - starttime))
pass8(pass_counter)