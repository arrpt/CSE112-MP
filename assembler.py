#! /usr/bin/env python3
import re
import sys

def registerSext(r):
    return ('0'*(5-len(bin(int(r[1:]))[2:])))+bin(int(r[1:]))[2:]

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

def R_sll(rd, rs1, rs2):
    funct7 = '0000000'
    funct3 = '001'
    opcode = '0110011'

def R_slt(rd, rs1, rs2):
    funct7 = '0000000'
    funct3 = '010'
    opcode = '0110011'
    
def R_sltu(rd, rs1, rs2):
    funct7 = '0000000'
    funct3 = '011'
    opcode = '0110011'

def R_xor(rd, rs1, rs2):
    funct7 = '0000000'
    funct3 = '100'
    opcode = '0110011'

def R_srl(rd, rs1, rs2):
    funct7 = '0000000'
    funct3 = '101'
    opcode = '0110011'

def R_or(rd, rs1, rs2):
    funct7 = '0000000'
    funct3 = '110'
    opcode = '0110011'

def R_and(rd, rs1, rs2):
    funct7 = '0000000'
    funct3 = '111'
    opcode = '0110011'

def S_sw(rs2, imm):
    funct3 = '010'
    opcode = '0100011'

def B_beq(rs1, rs2, imm):
    funct3 = '000'
    opcode = '1100011'

def B_bne(rs1, rs2, imm):
    funct3 = '001'
    opcode = '1100011'

def B_blt(rs1, rs2, imm):
    funct3 = '100'
    opcode = '1100011'

def B_bge(rs1, rs2, imm):
    funct3 = '101'
    opcode = '1100011'

def B_bltu(rs1, rs2, imm):
    funct3 = '110'
    opcode = '1100011'

def B_bgeu(rs1, rs2, imm):
    funct3 = '111'
    opcode = '1100011'

def U_auipc(rd, imm):
    opcode = '0110111'

def U_lui(rd, imm):
    opcode = '0010111'

def J_jal(rd, imm):
    opcode = '1101111'

def Bonus_mul(rd, rs1, rs2):
    opcode = ''

def Bonus_rst():
    opcode = ''

def Bonus_halt():
    opcode = ''

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

# REMOVING EMPTY LINES
k = 0
while k < len(data):
    if data[k].isspace():
        data.pop(k)
    k += 1

# CALCULATING LABEL ADDRESSES
currAddress = 0
for j in range(len(data)):
    if data[j].strip()[-1] == ':':
        symTable[data[j].strip()[:-1]] = currAddress

currAddress = 0
for i in range(len(data)):
    temp = re.sub(",", " ", data[i].lower())
    instruction = temp.split()
    #print(instruction)
    if len(instruction) > 4:
        print(f'ILLEGAL INSTRUCTION AT LINE {i+1}')
        sys.exit()
    
    operation = instruction[0]
    match operation:
        case "add":
            try:
                rd = abi2register[instruction[1]]
                rs1 = abi2register[instruction[2]]
                rs2 = abi2register[instruction[3]]
                output[currAddress] = R_add(rd, rs1, rs2)
                currAddress += 4
            except Exception as e:
                print(f'ERROR {e}')
                sys.exit()

        case "sub":
            R_sub()
        case "sll":
            R_sll()
        case "slt":
            R_slt()
        case "sltu":
            R_sltu()
        case "xor":
            R_xor()
        case "srl":
            R_srl()
        case "or":
            R_or()
        case "and":
            R_and()
        case "sw":
            S_sw()
        case "beq":
            B_beq()
        case "bne":
            B_bne()
        case "blt":
            B_blt()
        case "bge":
            B_bge()
        case "bltu":
            B_bltu()
        case "bgeu":
            B_bgeu()
        case "auipc":
            U_auipc()
        case "lui":
            U_lui()
        case "jal":
            J_jal()
        case "mul":
            Bonus_mul()
        case "halt":
            Bonus_halt()
        case "rvrs":
            Bonus_rvrs()   
        case _:
            print(f'ILLEGAL INSTRUCTION AT LINE {i+1}')
            sys.exit()



print(output)