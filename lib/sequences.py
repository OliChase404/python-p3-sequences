#!/usr/bin/env python3

def print_fibonacci(length):
    if(length == 0):
        print([])
    elif(length == 1):
        print([0])
    elif(length > 1):
        responce = [0,1]
        while(len(responce) < length):
            next_number = responce[-2] + responce[-1]
            responce.append(next_number)
        print(responce)
            
print_fibonacci(1)