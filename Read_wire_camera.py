import cv2 
import time, threading
import os
from time import sleep, perf_counter
from threading import Thread
from pylibdmtx.pylibdmtx import decode

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

cap1 = cv2.VideoCapture(1)
cap1.set(3,1280)
cap1.set(4,1024)

global ret
global img

global ret1
global img1

codes =[]
i = 0

def task1():
    global ret
    global img
    while True:        
        ret,img = cap.read()
        cv2.waitKey(1)
        t0 = time.time()
        
        cv2.imshow('Result',img)    
        
        if cv2.waitKey(1) == 27:
            break


def task3():
    while True:
        cv2.imshow('Result',img)    


def task2():
    global ret
    global img
    i=0
    while True:
        code = decode(img, timeout=100, max_count=1, corrections=3)
        if(code):
            print(i, code[0].data.decode('utf-8'))
            i=i+1







def task11():
    global ret1
    global img1
    while True:        
        ret1,img1 = cap1.read()
        cv2.waitKey(1)
        t0 = time.time()
        
        cv2.imshow('Result1',img1)    
        
        if cv2.waitKey(1) == 27:
            break


def task33():
    while True:
        cv2.imshow('Result1',img1)    


def task22():
    global ret1
    global img1
    i=0
    while True:
        code = decode(img1, timeout=100, max_count=1, corrections=3)
        if(code):
            print(i, code[0].data.decode('utf-8'))
            i=i+1
            check_and_append(code[0].data.decode('utf-8'))


def check_and_append(codeToAdd):
    global codes
    
    if codeToAdd[18:25] in codes:
        print('Такой код уже имеется')
        print(len(codes))
        print(codes)
        if len(codes)==16:
            printer()
        
    else:
        codes.append(codeToAdd[18:25])
        print(codeToAdd[18:25])
        print('добавил!, Количество элементов: ')
        print(len(codes))
        print(codes)
        add_to_file(codeToAdd[18:25])
        add_to_file(codeToAdd)
        if len(codes)==16:
            printer()
            

            
            


            
    
def add_to_file(data):
    file_object = open('TestFile.txt', 'a')
    file_object.write(data)
    file_object.write("\n")
    file_object.close()
    print('Добавил в файл')


def printer():
    global i
    
    if i ==0:
        print('Печатаю')
        
        #os.startfile("TestFile.txt", "print")
        i=1
    else:
        print('уже печатал')
        
        
    
        
    
                                                










# create two new threads
#t1 = Thread(target=task1)
#t2 = Thread(target=task2)
#t3 = Thread(target=task3)

t11 = Thread(target=task11)
t22 = Thread(target=task22)
t33 = Thread(target=task33)



# start the threads
#t1.start()
#time.sleep(5)
#t2.start()
#t3.start()

t11.start()
time.sleep(3)
t22.start()
t33.start()


# wait for the threads to complete
#t1.join()
#t2.join()
#t3.join()

t11.join()
t22.join()
t33.join()





