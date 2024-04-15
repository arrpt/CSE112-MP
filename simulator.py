#! /usr/bin/env python3
f = open('test1.txt', 'r')
data = f.readlines()
abi2register = {
    "x0": 0,
    "x1": 0,
    "x2": 0,
    "x3": 0,
    "x4": 0,
    "x5": 0,
    "x6": 0,
    "x7": 0,
    "x8": 0,
    "x8": 0,
    "x9": 0,
    "x10": 0,
    "x11": 0,
    "x12": 0,
    "x13": 0,
    "x14": 0,
    "x15": 0,
    "x16": 0,
    "x17": 0,
    "x18": 0,
    "x19": 0,
    "x20": 0,
    "x21": 0,
    "x22": 0,
    "x23": 0,
    "x24": 0,
    "x25": 0,
    "x26": 0,
    "x27": 0,
    "x28": 0,
    "x29": 0,
    "x30": 0,
    "x31": 0,
}

def r_add(data):
    return None

def r_sub(data):
    return None

pc = 0
while pc < len(data):
    if data[pc][-7:] == '0110011' and data[pc][-15:-12] == '000' and data[pc][-32:-25] == '0000000':
        r_add(data[pc])
    
    elif data[pc][-7:] == '0110011' and data[pc][-15:-12] == '000' and data[pc][-32:-25] == '0100000':
        r_sub(data[pc])
    
    pc += 1