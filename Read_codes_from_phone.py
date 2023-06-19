import cv2 
import requests
from pylibdmtx.pylibdmtx import decode
import numpy as np
import time, threading
from threading import Thread
import os

#images=requests.get("https://koshelevzz.ru/cam/2/qw.jpg")
codes =[]


def get_pictrure():
    global images
    while True:
        global images
        images=requests.get("https://koshelevzz.ru/cam/2/qw.jpg")
        time.sleep(0.1)
        #return images
    


def run():
    while True:
        #global images
        #get_pictrure()
        video=np.array(bytearray(images.content), dtype=np.uint8)
        try:
            render=cv2.imdecode(video,-1)
            cv2.imshow('frame', render)
            time.sleep(0.1)
            
        except:
            pass
        try:
            code = decode(render, timeout=100, max_count=1, corrections=3)
            print(code[0].data.decode('utf-8'))
        except:
            print("no codes")
            pass

        if cv2.waitKey(1)== 27:
            print("kal")
            break


def showing():
    #global images
    while True:
        try:
            global render
            video=np.array(bytearray(images.content), dtype=np.uint8)
            render=cv2.imdecode(video,-1)
            cv2.imshow('frame', render)
            time.sleep(0.1)
            if cv2.waitKey(1)== 27:
                break
        except:
             pass
            
        


def decoder():
    while True:
            try:
                code = decode(render, timeout=100, max_count=1, corrections=3)
                print(code[0].data.decode('utf-8'))
                time.sleep(0.01)
                check_and_append(code[0].data.decode('utf-8'))
            except:
                print("no codes")
       
           
            



            




def check_and_append(codeToAdd):
    
    
    if codeToAdd[18:25] in codes:
        #print('Такой код уже имеется')
        print(len(codes))
        #print(codes)
       
        
    else:
        codes.append(codeToAdd[18:25])
        print(codeToAdd[18:25])
        print('добавил!, Количество элементов: ')
        print(len(codes))
        #print(codes)
        #add_to_file(codeToAdd[18:25])
        add_to_file(codeToAdd)
         
def add_to_file(data):
    file_object = open('TestFile.txt', 'a')
    file_object.write(data)
    file_object.write("\n")
    file_object.close()
    print('Добавил в файл')

 


t1 = Thread(target=get_pictrure)
t2 = Thread(target=showing)
t3 = Thread(target=decoder)


t1.start()
time.sleep(1)
t2.start()
time.sleep(1)
t3.start()


t1.join()
t2.join()

