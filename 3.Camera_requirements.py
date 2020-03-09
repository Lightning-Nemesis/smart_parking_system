# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 21:29:47 2019

@author: User
"""

from getpass import getpass
passwd = getpass("password: ")
if passwd=='1234':
    print("Camera Model Suggestor")
    l=int(input("Enter Length of the parking lot(metres): "))
    b=int(input("Enter Breadth of the parking lot(metres): "))
    area=l*b
    c=0
    while(area>6400):
        area=area/2
        c=c+1
    print("number of camera required  "+str(2**c))
    
    
    if (l<5 and b<5) or area<25:
        Focal_length=3.6
        angle=75.7
        print("Elvy Full HD 3MP CCTV Camera Lens 3.6mm Security Board Lens Wide Angle 92 Degree for HD CCTV IR Camera ip Camera")
        print("price = 1050")
    if (l<6 and b<6) or area<36:
        Focal_length=4
        angle=69.9
        print("CCTV Camera CS Mount 1/3 Format 4mm Focal Length Fixed Iris Lens")
    if (l>5 and b>5 and l<=10 and b<=10) or (area>25 and area<=36):
        Focal_length=6
        angle=50
        print("SLB Works 6mm Focus Length Fixed Board Lens for CCTV Camera H3B3 J2K4 M6E8")
        print("price = 1500")
    if (l>10 and b>10 and l<=20 and b<=20) or (area>100 and area<=400):
        Focal_length=8
        angle=38.5
        print("Hikvision 8 CCTV Cameras (Night Vision) & 8Channel DVR Standalone Kit")
        print("price = 1899")
    if (l>20 and b>20 and l<=35 and b<=35 )or (area>400 and area<=1225):
        Focal_length=12
        angle=26.2
        print("DealMux CCTV Security Camera 8mm Focal Length Board IR Lens")
        print("price = 2000")
    if (l>35 and b>35 and l<=50 and b<=50) or (area>1225 and area<=2500):
        Focal_length=16
        angle=19.8
        print("DealMux CCTV Security Camera 8mm Focal Length Board IR Lens")
        print("price = 2725")
        
    if (l>50 and b>50 and l<=80 and b<=80 )or (area>2500 and area<=6400):
        Focal_length=25
        angle=26.2
        print("CCTV Camera 25mm Focus Length IR Fixed Iris Lens")
        print("price=3594")
        