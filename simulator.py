#! /usr/bin/env python3
import sys

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

def r_sll(data):
    return None

def r_slt(data):
    return None

def r_sltu(data):
    return None

def r_xor(data):
    return None

def r_srl(data):
    return None

def r_or(data):
    return None

def r_and(data):
    return None

def i_lw(data):
    return None

def i_addi(data):
    return None

def i_sltiu(data):
    return None

def i_jalr(data):
    return None

def s_sw(data):
    return None

def b_beq(data):
    return None

def b_bne(data):
    return None

def b_blt(data):
    return None

def b_bge(data):
    return None

def b_bltu(data):
    return None

def b_bgeu(data):
    return None

def u_aupic(data):
    return None

def u_lui(data):
    return None

def j_jal(data):
    return None

pc = 0
while pc < len(data):
    if data[pc][-7:] == '0110011' and data[pc][-15:-12] == '000' and data[pc][-32:-25] == '0000000':
        r_add(data[pc])
    
    elif data[pc][-7:] == '0110011' and data[pc][-15:-12] == '000' and data[pc][-32:-25] == '0100000':
        r_sub(data[pc])
        
    elif data[pc][-7:] == '0110011' and data[pc][-15:-12] == '001' and data[pc][-32:-25] == '0000000':
        r_sll(data[pc])
    
    elif data[pc][-7:] == '0110011' and data[pc][-15:-12] == '010' and data[pc][-32:-25] == '0000000':
        r_slt(data[pc])
        
    elif data[pc][-7:] == '0110011' and data[pc][-15:-12] == '011' and data[pc][-32:-25] == '0000000':
        r_sltu(data[pc])
    
    elif data[pc][-7:] == '0110011' and data[pc][-15:-12] == '100' and data[pc][-32:-25] == '0000000':
        r_xor(data[pc])
    
    elif data[pc][-7:] == '0110011' and data[pc][-15:-12] == '101' and data[pc][-32:-25] == '0000000':
        r_srl(data[pc])
        
    elif data[pc][-7:] == '0110011' and data[pc][-15:-12] == '110' and data[pc][-32:-25] == '0000000':
        r_or(data[pc])
        
    elif data[pc][-7:] == '0110011' and data[pc][-15:-12] == '111' and data[pc][-32:-25] == '0000000':
        r_and(data[pc])
    
    elif data[pc][-7:] == '0000011' and data[pc][-15:-12] == '010':
        i_lw(data[pc])

    elif data[pc][-7:] == '0010011' and data[pc][-15:-12] == '000':
        i_addi(data[pc])
        
    elif data[pc][-7:] == '0000011' and data[pc][-15:-12] == '011':
        i_sltiu(data[pc])
        
    elif data[pc][-7:] == '1100111' and data[pc][-15:-12] == '000':
        i_jalr(data[pc])
        
    elif data[pc][-7:] == '0100011' and data[pc][-15:-12] == '010':
        s_sw(data[pc])
        
    elif data[pc][-7:] == '1100011' and data[pc][-15:-12] == '000':
        b_beq(data[pc])
    
    elif data[pc][-7:] == '1100011' and data[pc][-15:-12] == '001':
        b_bne(data[pc])
        
    elif data[pc][-7:] == '1100011' and data[pc][-15:-12] == '100':
        b_blt(data[pc])
        
    elif data[pc][-7:] == '1100011' and data[pc][-15:-12] == '101':
        b_bge(data[pc])
        
    elif data[pc][-7:] == '1100011' and data[pc][-15:-12] == '110':
        b_bltu(data[pc])
        
    elif data[pc][-7:] == '1100011' and data[pc][-15:-12] == '111':
        b_bgeu(data[pc])
        
    elif data[pc][-7:] == '0110111':
        u_lui(data[pc])
        
    elif data[pc][-7:] == '0010111':
        u_aupic(data[pc])
        
    elif data[pc][-7:] == '1101111':
        j_jal(data[pc])
        
    else:
        print("Illegal instruction")
        sys.exit()
          
    pc += 1