# 0=RED, 1=GREEN, 2=BLUE, 3=ALPHA

#import tkinter as tk
#import tkinter.ttk as ttk
#from tkcolorpicker import askcolor
import time

c1 = [0,0,0,0] #this color
c2 = [0,0,0] #over this color
c3 = [0,0,0] #result

cont='y'

#--------------------------------

while cont=='y':
    print('--enter underlay color in r,g,b--')
    c2[0]=int(input('red: '))
    c2[1]=int(input('green: '))
    c2[2]=int(input('blue: '))
    print('')
    
    print('--enter desired color in r,g,b--')
    c3[0]=int(input('red: '))
    c3[1]=int(input('green: '))
    c3[2]=int(input('blue: '))
    print('')
    
    #--------------------------------

    alpha = 0
    r = -1
    g = -1
    b = -1

    while alpha < 1 and r < 0 or g < 0 or b < 0 or r > 255 or g > 255 or b > 255:
        alpha+= 1/256
        inv = 1 / alpha
        r = c3[0] * inv + c2[0] * (1 - inv)
        g = c3[1] * inv + c2[1] * (1 - inv)
        b = c3[2] * inv + c2[2] * (1 - inv)

    print('---result---')
    print('red:', round(r))
    print('green:', round(g))
    print('blue:', round(b))
    print('alpha:', round(alpha*256))
    print('------------')
    print('')

    cont=input('again? y/n')
    print('')

