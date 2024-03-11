#! /usr/bin/env python3
import re
import sys

def registerSext(r):
    return ('0'*(5-len(bin(int(r[1:]))[2:])))+bin(int(r[1:]))[2:]

def immExt_for12bits(i):
    if int(i) >= 0:
        return ('0'*(12-len(bin(int(i))[2:])))+bin(int(i))[2:]
    else:
        return ('1'*(12-len(bin(int(i))[3:])))+bin(int(i))[3:]

def immExt_for32bits(i):
    if int(i) >= 0:
        return ('0'*(32-len(bin(int(i))[2:])))+bin(int(i))[2:]
    else:
        return ('1'*(32-len(bin(int(i))[3:])))+bin(int(i))[3:]

def immExt_for20bits(i):
    if int(i) >= 0:
        return ('0'*(20-len(bin(int(i))[2:])))+bin(int(i))[2:]
    else:
        return ('1'*(20-len(bin(int(i))[3:])))+bin(int(i))[3:] 

def isLabel(dataline):
    if dataline.strip()[-1] == ':':
        return True
    else:
        return False
    
def err(offset,n):
    if int(offset)>=0:
        if len(bin(offset)[2:]) > n:
            return False
        else:
            return True
    else:
        if len(bin(offset)[3:]) > n:
            return False
        else:
            return True 

def R_add(rd, rs1, rs2):
    funct7 = '0000000'
    funct3 = '000'
    opcode = '0110011'
    rd = registerSext(rd)
    rs1 = registerSext(rs1)
    rs2 = registerSext(rs2)
    return funct7+rs2+rs1+funct3+rd+opcode

def R_sub(rd, rs1, rs2):
    funct7 = '0100000'
    funct3 = '000'
    opcode = '0110011'
    rd = registerSext(rd)
    rs1 = registerSext(rs1)
    rs2 = registerSext(rs2)
    return funct7+rs2+rs1+funct3+rd+opcode

def R_sll(rd, rs1, rs2):
    funct7 = '0000000'
    funct3 = '001'
    opcode = '0110011'
    rd = registerSext(rd)
    rs1 = registerSext(rs1)
    rs2 = registerSext(rs2)
    return funct7+rs2+rs1+funct3+rd+opcode

def R_slt(rd, rs1, rs2):
    funct7 = '0000000'
    funct3 = '010'
    opcode = '0110011'
    rd = registerSext(rd)
    rs1 = registerSext(rs1)
    rs2 = registerSext(rs2)
    return funct7+rs2+rs1+funct3+rd+opcode
    
def R_sltu(rd, rs1, rs2):
    funct7 = '0000000'
    funct3 = '011'
    opcode = '0110011'
    rd = registerSext(rd)
    rs1 = registerSext(rs1)
    rs2 = registerSext(rs2)
    return funct7+rs2+rs1+funct3+rd+opcode

def R_xor(rd, rs1, rs2):
    funct7 = '0000000'
    funct3 = '100'
    opcode = '0110011'
    rd = registerSext(rd)
    rs1 = registerSext(rs1)
    rs2 = registerSext(rs2)
    return funct7+rs2+rs1+funct3+rd+opcode

def R_srl(rd, rs1, rs2):
    funct7 = '0000000'
    funct3 = '101'
    opcode = '0110011'
    rd = registerSext(rd)
    rs1 = registerSext(rs1)
    rs2 = registerSext(rs2)
    return funct7+rs2+rs1+funct3+rd+opcode

def R_or(rd, rs1, rs2):
    funct7 = '0000000'
    funct3 = '110'
    opcode = '0110011'
    rd = registerSext(rd)
    rs1 = registerSext(rs1)
    rs2 = registerSext(rs2)
    return funct7+rs2+rs1+funct3+rd+opcode

def R_and(rd, rs1, rs2):
    funct7 = '0000000'
    funct3 = '111'
    opcode = '0110011'
    rd = registerSext(rd)
    rs1 = registerSext(rs1)
    rs2 = registerSext(rs2)
    return funct7+rs2+rs1+funct3+rd+opcode

def I_lw(rd, rs1, imm):
    funct3 = '010'
    opcode = '0000011'
    return immExt_for12bits(imm)+registerSext(rs1)+funct3+registerSext(rd)+opcode

def I_addi(rd, rs1, imm):
    funct3 = '000'
    opcode = '0010011'
    return immExt_for12bits(imm)+registerSext(rs1)+funct3+registerSext(rd)+opcode

def I_sltiu(rd, rs1, imm):
    funct3 = '011'
    opcode = '0010011'
    return immExt_for12bits(imm)+registerSext(rs1)+funct3+registerSext(rd)+opcode

def I_jalr(rd, rs1, offset):    
    funct3 = '000'
    opcode = '1100111'
    return immExt_for12bits(imm)+registerSext(rs1)+funct3+registerSext(rd)+opcode

def S_sw(rs2, imm, rs1):
    funct3 = '010'
    opcode = '0100011'
    immf = immExt_for12bits(imm)
    return immf[0:8]+registerSext(rs2)+registerSext(rs1)+funct3+immf[8:]+opcode
    
def B_beq(rs1, rs2, offset):
    funct3 = '000'
    opcode = '1100011'
    offset = immExt_for12bits(offset)
    return offset[-12]+offset[-10:-4]+registerSext(rs2)+registerSext(rs1)+funct3+offset[-4:]+offset[-11]+opcode

def B_bne(rs1, rs2, offset):
    funct3 = '001'
    opcode = '1100011'
    offset = immExt_for12bits(offset)
    return offset[-12]+offset[-10:-4]+registerSext(rs2)+registerSext(rs1)+funct3+offset[-4:]+offset[-11]+opcode

def B_blt(rs1, rs2, offset):
    funct3 = '100'
    opcode = '1100011'
    offset = immExt_for12bits(offset)
    return offset[-12]+offset[-10:-4]+registerSext(rs2)+registerSext(rs1)+funct3+offset[-4:]+offset[-11]+opcode

def B_bge(rs1, rs2, offset):
    funct3 = '101'
    opcode = '1100011'
    offset = immExt_for12bits(offset)
    return offset[-12]+offset[-10:-4]+registerSext(rs2)+registerSext(rs1)+funct3+offset[-4:]+offset[-11]+opcode

def B_bltu(rs1, rs2, offset):
    funct3 = '110'
    opcode = '1100011'
    offset = immExt_for12bits(offset)
    return offset[-12]+offset[-10:-4]+registerSext(rs2)+registerSext(rs1)+funct3+offset[-4:]+offset[-11]+opcode

def B_bgeu(rs1, rs2, offset):
    funct3 = '111'
    opcode = '1100011'
    offset = immExt_for12bits(offset)
    return offset[-12]+offset[-10:-4]+registerSext(rs2)+registerSext(rs1)+funct3+offset[-4:]+offset[-11]+opcode

def U_auipc(rd, imm):
    opcode = '0110111'
    immf = immExt_for20bits(imm)
    return immf+registerSext(rd)+opcode
    
def U_lui(rd, imm):
    opcode = '0010111'
    immf = immExt_for20bits(imm)
    return immf+registerSext(rd)+opcode

def J_jal(rd, imm):
    opcode = '1101111'
    immf = immExt_for20bits(imm)
    return immf[-20]+immf[-10:]+immf[-11]+immf[-19:-11]+registerSext(rd)+opcode

def Bonus_mul(rd, rs1, rs2):
    opcode = ''

def Bonus_rst():
    opcode = ''

def Bonus_halt():
    return B_beq('x0', 'x0', '0')

def Bonus_rvrs(rd, rs):
    opcode = ''

abi2register = {
    "zero": "x0",
    "ra": "x1",
    "sp": "x2",
    "gp": "x3",
    "tp": "x4",
    "t0": "x5",
    "t1": "x6",
    "t2": "x7",
    "s0": "x8",
    "fp": "x8",
    "s1": "x9",
    "a0": "x10",
    "a1": "x11",
    "a2": "x12",
    "a3": "x13",
    "a4": "x14",
    "a5": "x15",
    "a6": "x16",
    "a7": "x17",
    "s2": "x18",
    "s3": "x19",
    "s4": "x20",
    "s5": "x21",
    "s6": "x22",
    "s7": "x23",
    "s8": "x24",
    "s9": "x25",
    "s10": "x26",
    "s11": "x27",
    "t3": "x28",
    "t4": "x29",
    "t5": "x30",
    "t6": "x31",
}

f = open('test.s', 'r')
data = f.readlines()
output = {}
symTable = {}

if "beq zero,zero,0" not in data[-1]:
    print("ERROR: MISSING VIRTUAL HALT AT LAST!")
    sys.exit()

# REMOVING EMPTY LINES
k = 0
vHault = False
while k < len(data):
    if data[k].isspace():
        data.pop(k)
    if "beq zero,zero,0x00000000" in data[k] or "beq zero,zero,0" in data[k]:
        vHault = True
    k += 1
if vHault == False:
    print("HALT INSTRUCTION NOT USED AS LAST INSTRUCTION")




# CALCULATING LABEL ADDRESSES
currAddress = 0
j = 0
while j < len(data):
    if isLabel(data[j].split()[0]) == True:
        symTable[data[j].split()[0].strip()[:-1]] = currAddress
        data[j] = data[j].replace(data[j].split()[0], '')
    j += 1
    currAddress += 4

# BUILDINvirtual BINARY
currAddress = 0
for i in range(len(data)):
    operation = data[i].split()[0]
    operands = data[i].split()[1].split(',')
    match operation:
        case "add":
            try:
                rd = abi2register[operands[0]]
                rs1 = abi2register[operands[1]]
                rs2 = abi2register[operands[2]]
                output[currAddress] = R_add(rd, rs1, rs2)
                currAddress += 4
            except Exception as e:
                print(f'ILLEGAL INSTRUCTION AT LINE: {i+1}')
                sys.exit()

        case "sub":
            try:
                rd = abi2register[operands[0]]
                rs1 = abi2register[operands[1]]
                rs2 = abi2register[operands[2]]
                output[currAddress] = R_sub(rd, rs1, rs2)
                currAddress += 4
            except Exception as e:
                print(f'ILLEGAL INSTRUCTION AT LINE: {i+1}')
                sys.exit()
    
        case "sll":
            try:
                rd = abi2register[operands[0]]
                rs1 = abi2register[operands[1]]
                rs2 = abi2register[operands[2]]
                output[currAddress] = R_sll(rd, rs1, rs2)
                currAddress += 4
            except Exception as e:
                print(f'ILLEGAL INSTRUCTION AT LINE: {i+1}')
                sys.exit()

        case "slt":
            try:
                rd = abi2register[operands[0]]
                rs1 = abi2register[operands[1]]
                rs2 = abi2register[operands[2]]
                output[currAddress] = R_slt(rd, rs1, rs2)
                currAddress += 4
            except Exception as e:
                print(f'ILLEGAL INSTRUCTION AT LINE: {i+1}')
                sys.exit()

        case "sltu":
            try:
                rd = abi2register[operands[0]]
                rs1 = abi2register[operands[1]]
                rs2 = abi2register[operands[2]]
                output[currAddress] = R_sltu(rd, rs1, rs2)
                currAddress += 4
            except Exception as e:
                print(f'ILLEGAL INSTRUCTION AT LINE: {i+1}')
                sys.exit()
            
        case "xor":
            try:
                rd = abi2register[operands[0]]
                rs1 = abi2register[operands[1]]
                rs2 = abi2register[operands[2]]
                output[currAddress] = R_xor(rd, rs1, rs2)
                currAddress += 4
            except Exception as e:
                print(f'ILLEGAL INSTRUCTION AT LINE: {i+1}')
                sys.exit()

        case "srl":
            try:
                rd = abi2register[operands[0]]
                rs1 = abi2register[operands[1]]
                rs2 = abi2register[operands[2]]
                output[currAddress] = R_srl(rd, rs1, rs2)
                currAddress += 4
            except Exception as e:
                print(f'ILLEGAL INSTRUCTION AT LINE: {i+1}')
                sys.exit()

        case "or":
            try:
                rd = abi2register[operands[0]]
                rs1 = abi2register[operands[1]]
                rs2 = abi2register[operands[2]]
                output[currAddress] = R_or(rd, rs1, rs2)
                currAddress += 4
            except Exception as e:
                print(f'ILLEGAL INSTRUCTION AT LINE: {i+1}')
                sys.exit()

        case "and":
            try:
                rd = abi2register[operands[0]]
                rs1 = abi2register[operands[1]]
                rs2 = abi2register[operands[2]]
                output[currAddress] = R_and(rd, rs1, rs2)
                currAddress += 4
            except Exception as e:
                print(f'ILLEGAL INSTRUCTION AT LINE: {i+1}')
                sys.exit()
        
        case "lw":
            try:
                rd = abi2register[operands[0]]
                imm = operands[1].split('(')[0]
                if err(imm,12) == False:
                    sys.exit()
                rs = abi2register[operands[1].split('(')[1][:-1]]
                output[currAddress] = I_lw(rd, rs, imm)
                currAddress += 4
            except Exception as e:
                print(f'ILLEGAL INSTRUCTION AT LINE: {i+1}')
                sys.exit()
        case "addi":
            try:
                rd = abi2register[operands[0]]
                rs = abi2register[operands[1]]
                imm = operands[2]
                if err(imm,12) == False:
                    sys.exit()
                output[currAddress] = I_addi(rd, rs, imm)
                currAddress += 4
            except Exception as e:
                print(f'ILLEGAL INSTRUCTION AT LINE: {i+1}')
                sys.exit()
        case "sltiu":
            try:
                rd = abi2register[operands[0]]
                rs = abi2register[operands[1]]
                imm = operands[2]
                if err(imm,12) == False:
                    sys.exit()
                output[currAddress] = I_sltiu(rd, rs, imm)
                currAddress += 4
            except Exception as e:
                print(f'ILLEGAL INSTRUCTION AT LINE: {i+1}')
                sys.exit()
        case "jalr":
            try:
                rd = abi2register[operands[0]]
                rs = abi2register[operands[1]]
                offset = operands[2]
                if err(offset,12) == False:
                    sys.exit()
                output[currAddress] = I_jalr(rd, rs, offset)
                currAddress += 4
            except Exception as e:
                print(f'ILLEGAL INSTRUCTION AT LINE: {i+1}')
                sys.exit()
        case "sw":
            try:
                rs2 = abi2register[operands[0]]
                imm = operands[1].split('(')[0]
                if err(imm,12) == False:
                    sys.exit()
                rs1 = abi2register[operands[1].split('(')[1][:-1]]
                output[currAddress] = S_sw(rs2, imm, rs1)
                currAddress += 4
            except Exception as e:
                print(f'ILLEGAL INSTRUCTION AT LINE: {i+1}')
                sys.exit()
        case "beq":
            try:
                rs1 = abi2register[operands[0]]
                rs2 = abi2register[operands[1]]
                if operands[2].isnumeric():
                    offset = operands[2]
                else:
                    offset = str(symTable[operands[2]]-currAddress) 
                if err(offset,12) == False:
                    sys.exit()
                output[currAddress] = B_beq(rs1, rs2, offset)
                currAddress += 4
            except Exception as e:
                print(f'ILLEGAL INSTRUCTION AT LINE: {i+1}')
                sys.exit()
        case "bne":
            try:
                rs1 = abi2register[operands[0]]
                rs2 = abi2register[operands[1]]
                if operands[2].isnumeric():
                    offset = operands[2]
                else:
                    offset = str(symTable[operands[2]]-currAddress) 
                if err(offset,12) == False:
                    sys.exit()
                output[currAddress] = B_bne(rs1, rs2, offset)
                currAddress += 4
            except Exception as e:
                print(f'ILLEGAL INSTRUCTION AT LINE: {i+1}')
                sys.exit()
        case "blt":
            try:
                rs1 = abi2register[operands[0]]
                rs2 = abi2register[operands[1]]
                if operands[2].isnumeric():
                    offset = operands[2]
                else:
                    offset = str(symTable[operands[2]]-currAddress) 
                if err(offset,12) == False:
                    sys.exit()
                output[currAddress] = B_blt(rs1, rs2, offset)
                currAddress += 4
            except Exception as e:
                print(f'ILLEGAL INSTRUCTION AT LINE: {i+1}')
                sys.exit()
        case "bge":
            try:
                rs1 = abi2register[operands[0]]
                rs2 = abi2register[operands[1]]
                if operands[2].isnumeric():
                    offset = operands[2]
                else:
                    offset = str(symTable[operands[2]]-currAddress) 
                if err(offset,12) == False:
                    sys.exit()
                output[currAddress] = B_bge(rs1, rs2, offset)
                currAddress += 4
            except Exception as e:
                print(f'ILLEGAL INSTRUCTION AT LINE: {i+1}')
                sys.exit()
        case "bltu":
            try:
                rs1 = abi2register[operands[0]]
                rs2 = abi2register[operands[1]]
                if operands[2].isnumeric():
                    offset = operands[2]
                else:
                    offset = str(symTable[operands[2]]-currAddress) 
                if err(offset,12) == False:
                    sys.exit()
                output[currAddress] = B_bltu(rs1, rs2, offset)
                currAddress += 4
            except Exception as e:
                print(f'ILLEGAL INSTRUCTION AT LINE: {i+1}')
                sys.exit()
        case "bgeu":
            try:
                rs1 = abi2register[operands[0]]
                rs2 = abi2register[operands[1]]
                if operands[2].isnumeric():
                    offset = operands[2]
                else:
                    offset = str(symTable[operands[2]]-currAddress) 
                if err(offset,12) == False:
                    sys.exit()
                output[currAddress] = B_bgeu(rs1, rs2, offset)
                currAddress += 4
            except Exception as e:
                print(f'ILLEGAL INSTRUCTION AT LINE: {i+1}')
                sys.exit()
        case "auipc":
            try:
                rd = abi2register[operands[0]]
                imm = operands[1]
                output[currAddress] = U_auipc(rd, imm)
                currAddress += 4
            except Exception as e:
                print(f'ILLEGAL INSTRUCTION AT LINE: {i+1}')
                sys.exit()
        case "lui":
            try:
                rd = abi2register[operands[0]]
                imm = operands[1]
                output[currAddress] = U_lui(rd, imm)
                currAddress += 4
            except Exception as e:
                print(f'ILLEGAL INSTRUCTION AT LINE: {i+1}')
                sys.exit()
        case "jal":
            try:
                rd = abi2register[operands[0]]
                imm = operands[1]
                output[currAddress] = J_jal(rd, imm)
                currAddress += 4
            except:
                print(f'ILLEGAL INSTRUCTION AT LINE: {i+1}')
                sys.exit()
    
        case "mul":
            Bonus_mul()
        case "halt":
            Bonus_halt()
        case "rvrs":
            Bonus_rvrs()   
        case _:
            print(f'ILLEGAL operands AT LINE {i+1}')
            sys.exit()


#print(symTable)
[print(x) for x in list(output.values())]