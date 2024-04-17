#! /usr/bin/env python3
import sys

f = open('test1.txt', 'r')
data = f.readlines()
abi2register = {
    "x0": 0,#hard wired zero
    "x1": 0,#return address
    "x2": 0,#stack pointer
    "x3": 0,#global pointer
    "x4": 0,#thread pointer
    "x5": 0,#temporary/alternate link register
    "x6": 0,#temporaries
    "x7": 0,#temporaries
    "x8": 0,#saved register/frame pointer
    "x9": 0,#saved register
    "x10": 0,#function arguments/return values
    "x11": 0,#function arguments/return values
    "x12": 0,#function arguments
    "x13": 0,#function arguments
    "x14": 0,#function arguments
    "x15": 0,#function arguments
    "x16": 0,#function arguments
    "x17": 0,#function arguments
    "x18": 0,#saved register
    "x19": 0,#saved register
    "x20": 0,#saved register
    "x21": 0,#saved register
    "x22": 0,#saved register
    "x23": 0,#saved register
    "x24": 0,#saved register
    "x25": 0,#saved register
    "x26": 0,#saved register
    "x27": 0,#saved register
    "x28": 0,#temporaries
    "x29": 0,#temporaries
    "x30": 0,#temporaries
    "x31": 0,#temporaries
}

def func(r):#binary in string -> x(int) in string
    return f"x{int(r,2)}"#"100" 100 

def sign_extend(value, bits):
    mask = 1 << (bits - 1)
    return (value & ((1 << bits) - 1)) - (value & mask)

def r_add(data):
    rd = func(data[-12:-7])
    rs1 = func(data[-20:-15])
    rs2 = func(data[-25:-20])
    abi2register[rd] = abi2register[rs1] + abi2register[rs2]
    return None

def r_sub(data):
    rd = func(data[-12:-7])
    rs1 = func(data[-20:-15])
    rs2 = func(data[-25:-20])
    abi2register[rd] = abi2register[rs1] - abi2register[rs2]
    return None

def r_sll(data):

    return None

def r_slt(data):
    rd = func(data[-12:-7])
    rs1 = func(data[-20:-15])
    rs2 = func(data[-25:-20])
    if abi2register[rs1]<abi2register[rs2]:
        abi2register[rd]=1
    return None

def r_sltu(data):
    rd = func(data[-12:-7])
    rs1 = func(data[-20:-15])
    rs2 = func(data[-25:-20])
    if abi2register[rs1] < abi2register[rs2] :
        abi2register[rd] = 1 
    return None

def r_xor(data):
    rd = func(data[-12:-7])
    rs1 = func(data[-20:-15])
    rs2 = func(data[-25:-20])
    abi2register[rd] = abi2register[rs1] ^ abi2register[rs2]
    return None

def r_srl(data):
    return None

def r_or(data):
    rd = func(data[-12:-7])
    rs1 = func(data[-20:-15])
    rs2 = func(data[-25:-20])
    abi2register[rd] = abi2register[rs1] | abi2register[rs2]
    return None

def r_and(data):
    rd = func(data[-12:-7])
    rs1 = func(data[-20:-15])
    rs2 = func(data[-25:-20])
    abi2register[rd] = abi2register[rs1] & abi2register[rs2]
    return None

def i_lw(data):#doubt
    immd = sign_extend(int(data[-31:-20],2),12)
    rs1 = func(data[-20:-15])
    rd = func(data[-12:-7])
    abi2register[rd] = abi2register[rs1] + immd
    return None

def i_addi(data):
    imm = sign_extend(int(data[-31:-20], 2), 12) 
    rs1 = func(data[-20:-15]) 
    rd = func(data[-12:-7]) 
    abi2register[rd] = abi2register[rs1] + imm  
    return None

def i_sltiu(data):
    imm = sign_extend(int(data[-31:-20], 2), 12) 
    rs1 = func(data[-20:-15]) 
    rd = func(data[-12:-7]) 
    if abi2register[rs1] < imm :# not unsigned
        abi2register[rd] =1
    return None

def i_jalr(data):#doubt
    rd = func(data[-12:-7])
    abi2register[rd] = pc
    offset = sign_extend(int(data[-31:-20], 2), 12) 
    pc = abi2register["x6"] + offset
    val = str(pc)
    val = val[:-1]
    val = val+"0"
    pc = int(val)
    run(pc)
    pc = abi2register[rd]
    return None

def s_sw(data):#doubt 
    imm = sign_extend(int(data[-31:-25]+data[-12:-7], 2), 12) 
    rs2 = func(data[-25:-20])
    rs1 = func(data[-20:-15]) 
    return None

def b_beq(data):
    rs1 = func(data[-20:-15])
    rs2 = func(data[-25:-20])
    imm = sign_extend(int(data[-31:-25]+data[-12:-7], 2), 12) #alterations required
    if abi2register[rs1]==abi2register[rs2]:
        abi2register["x1"] = pc
        pc += imm
        run(pc)
        pc = abi2register["x1"]
    return None

def b_bne(data):
    rs1 = func(data[-20:-15])
    rs2 = func(data[-25:-20])
    imm = sign_extend(int(data[-31:-25]+data[-12:-7], 2), 12) #alterations required
    if abi2register[rs1]!=abi2register[rs2]:
        abi2register["x1"] = pc
        pc += imm
        run(pc)
        pc = abi2register["x1"]
    return None

def b_blt(data):
    rs1 = func(data[-20:-15])
    rs2 = func(data[-25:-20])
    imm = sign_extend(int(data[-31:-25]+data[-12:-7], 2), 12)#alterations required 
    if abi2register[rs1]<abi2register[rs2]:
        abi2register["x1"] = pc
        pc += imm
        run(pc)
        pc = abi2register["x1"]
    return None

def b_bge(data):
    rs1 = func(data[-20:-15])
    rs2 = func(data[-25:-20])
    imm = sign_extend(int(data[-31:-25]+data[-12:-7], 2), 12) #alterations required
    if abi2register[rs1]>abi2register[rs2]:
        abi2register["x1"] = pc
        pc += imm
        run(pc)
        pc = abi2register["x1"]
    return None

def b_bltu(data):#unsigned 
    return None

def b_bgeu(data):#unsigned
    return None

def u_aupic(data):
    rd = func(data[-12:-7])
    imm = sign_extend(int(data[-31:-12], 2), 12) 
    abi2register[rd] = pc + imm
    return None

def u_lui(data):
    rd = func(data[-12:-7])
    imm = sign_extend(int(data[-31:-12], 2), 12) 
    abi2register[rd] =  imm
    return None

def j_jal(data):
    rd = func(data[-12:-7])
    imm = sign_extend(int(data[-31:-12], 2), 12)
    abi2register[rd] = pc
    pc+= imm
    val = str(pc)
    val = val[:-1]
    val = val+"0"
    pc = int(val)
    run(pc)
    pc = abi2register[rd]
    return None

def Bonus_mul(data):
    rs1 = func(data[-20:-15])
    rs2 = func(data[-25:-20])
    rd = func(data[-12:-7])
    num1 = str(abi2register[rs1])
    num2 = str(abi2register[rs2])
    abi2register[rd] = bin(int(num1,2)*int(num2,2))
    return None

def Bonus_rst(data):
    for i in abi2register:
        if(i==pc):
            continue
    abi2register[i]=1
    return None

def Bonus_rvrs(data):#check
    rs1 = func(data[-20:-15])
    rd = func(data[-12:-7])
    val = abi2register[rs1]
    abi2register[rd] = int(str(val)[::-1])
    return None

ra = "x1"
pc =0

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

    elif data[pc][-7:] == '0110011' and data[pc][-15:-12] == '000' and data[pc][-32:-25] == '0000001':
        Bonus_mul(data[pc])
    
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

    elif data[pc] == '00000000000000000000000000000000':
        Bonus_rst(data[pc])

    elif data[pc][-7:] == '0001011':
        Bonus_rvrs(data[pc])
        
    else:
        print("Illegal instruction")
        sys.exit()
          
    pc += 1

def run(pc):
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