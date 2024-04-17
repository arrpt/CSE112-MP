#! /usr/bin/env python3
import sys

f = open('test1.txt', 'r')
data = f.readlines()
register = {
    "00000": '00000000000000000000000000000000',
    "00001": '00000000000000000000000000000000',
    "00010": '00000000000000000000000000000000',
    "00011": '00000000000000000000000000000000',
    "00100": '00000000000000000000000000000000',
    "00101": '00000000000000000000000000000000',
    "00110": '00000000000000000000000000000000',
    "00111": '00000000000000000000000000000000',
    "01000": '00000000000000000000000000000000',
    "01001": '00000000000000000000000000000000',
    "01010": '00000000000000000000000000000000',
    "01011": '00000000000000000000000000000000',
    "01100": '00000000000000000000000000000000',
    "01101": '00000000000000000000000000000000',
    "01110": '00000000000000000000000000000000',
    "01111": '00000000000000000000000000000000',
    "10000": '00000000000000000000000000000000',
    "10001": '00000000000000000000000000000000',
    "10010": '00000000000000000000000000000000',
    "10011": '00000000000000000000000000000000',
    "10100": '00000000000000000000000000000000',
    "10101": '00000000000000000000000000000000',
    "10110": '00000000000000000000000000000000',
    "10111": '00000000000000000000000000000000',
    "11000": '00000000000000000000000000000000',
    "11001": '00000000000000000000000000000000',
    "11010": '00000000000000000000000000000000',
    "11011": '00000000000000000000000000000000',
    "11100": '00000000000000000000000000000000',
    "11101": '00000000000000000000000000000000',
    "11110": '00000000000000000000000000000000',
    "11111": '00000000000000000000000000000000',
}

def int2binary(num: int) -> str:
    return format(2**32 + num, 'b')[-32:]

def binary2uint(binary: str) -> int:
    return int(binary, 2)

def binary2sint(binary: str) -> int:
    if binary[0] == '0':
        return int(binary, 2)
    else:
        return int(binary, 2) - (1 << 32)

def sext(binary: str) -> str:
    if binary[0] == 0:
        return 0*(32-len(binary)) + binary
    else:
        return 1*(32-len(binary)) + binary

def r_add(data):
    rd = data[-12:-7]
    rs1 = data[-20:-15]
    rs2 = data[-25:-20]
    out = binary2sint(register[rs1]) + binary2sint(register[rs2])
    register[rd] = int2binary(out)
    return

def r_sub(data):
    rd = data[-12:-7]
    rs1 = data[-20:-15]
    rs2 = data[-25:-20]
    out = binary2sint(register[rs1]) - binary2sint(register[rs2])
    register[rd] = int2binary(out)
    return

def r_slt(data):
    rd = data[-12:-7]
    rs1 = data[-20:-15]
    rs2 = data[-25:-20]
    if binary2sint(register[rs1]) < binary2sint(register[rs2]):
        register[rd] = int2binary(1)
    else:
        register[rd] = int2binary(0)
    return

def r_sltu(data):
    rd = data[-12:-7]
    rs1 = data[-20:-15]
    rs2 = data[-25:-20]
    if binary2uint(register[rs1]) < binary2uint(register[rs2]):
        register[rd] = int2binary(1)
    else:
        register[rd] = int2binary(0)
    return

def r_sll(data):
    rd = data[-12:-7]
    rs1 = data[-20:-15]
    rs2 = data[-25:-20]
    register[rd] = (register[rs1] + '0'*binary2uint(register[rs2][-5:]))[-32:]
    return

def r_srl(data):
    rd = data[-12:-7]
    rs1 = data[-20:-15]
    rs2 = data[-25:-20]
    register[rd] = ('0'*binary2uint(register[rs2][-5:]) + register[rs1])[:32]
    return

def r_xor(data):
    rd = data[-12:-7]
    rs1 = data[-20:-15]
    rs2 = data[-25:-20]
    out = ""
    for i in range(32):
        out += str(int(register[rs1][i]) ^ int(register[rs2][i]))
    register[rd] = out
    return

def r_or(data):
    rd = data[-12:-7]
    rs1 = data[-20:-15]
    rs2 = data[-25:-20]
    out = ""
    for i in range(32):
        out += str(int(register[rs1][i]) | int(register[rs2][i]))
    register[rd] = out
    return

def r_and(data):
    rd = data[-12:-7]
    rs1 = data[-20:-15]
    rs2 = data[-25:-20]
    out = ""
    for i in range(32):
        out += str(int(register[rs1][i]) & int(register[rs2][i]))
    register[rd] = out
    return

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
    global pc
    rs1 = data[-20:-15]
    rs2 = data[-25:-20]
    imm = data[-32]+data[-8]+data[-31:-25]+data[-12:-8]
    if binary2sint(register[rs1]) == binary2sint(register[rs2]):
        pc += binary2sint(sext(imm))//4 - 1
    return

def b_bne(data):
    global pc
    rs1 = data[-20:-15]
    rs2 = data[-25:-20]
    imm = data[-32]+data[-8]+data[-31:-25]+data[-12:-8]
    if binary2sint(register[rs1]) != binary2sint(register[rs2]):
        pc += binary2sint(sext(imm))//4 - 1
    return

def b_blt(data):
    global pc
    rs1 = data[-20:-15]
    rs2 = data[-25:-20]
    imm = data[-32]+data[-8]+data[-31:-25]+data[-12:-8]
    if binary2sint(register[rs1]) < binary2sint(register[rs2]):
        pc += binary2sint(sext(imm))//4 - 1
    return

def b_bge(data):
    global pc
    rs1 = data[-20:-15]
    rs2 = data[-25:-20]
    imm = data[-32]+data[-8]+data[-31:-25]+data[-12:-8]
    if binary2sint(register[rs1]) >= binary2sint(register[rs2]):
        pc += binary2sint(sext(imm))//4 - 1
    return

def b_bltu(data):
    global pc
    rs1 = data[-20:-15]
    rs2 = data[-25:-20]
    imm = data[-32]+data[-8]+data[-31:-25]+data[-12:-8]
    if binary2uint(register[rs1]) < binary2uint(register[rs2]):
        pc += binary2sint(sext(imm))//4 - 1
    return

def b_bgeu(data):
    rs1 = data[-20:-15]
    rs1 = data[-25:-20]
    imm = data[-32]+data[-8]+data[-31:-25]+data[-12:-8]
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