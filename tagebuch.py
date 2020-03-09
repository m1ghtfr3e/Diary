#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 16:12:27 2020

@author: n0way
"""

import datetime

#tagebuch = open('MeinTagebuch.txt', 'w')

def readTagebuch():
    tagebuch = open('MeinTagebuch.txt', 'r')
    for line in tagebuch:
        print(line.strip())
    tagebuch.close()


def writeTagebuch():
    thetime = datetime.datetime.now()
    neuerEintrag = input("Dein neuer Eintrag: ")
    with open('MeinTagebuch.txt', 'a') as wt:
        wt.write("\n ------------------------ \n")
        wt.write("\n Eintrag vom: ")
        wt.write(str(thetime))
        wt.write("\n")
        wt.write(neuerEintrag)


def main():
    print("Hallo Polo, willkommen zu Deinem Tagebuch :) ")
    while True:
        opt = input("""Willst du mich lesen oder
                    etwas neues hinzufügen? : """)
        if opt == 'lesen':
            readTagebuch()
        if opt == 'schreiben':
            writeTagebuch()
        if opt == 'stop':
            break

main()
    