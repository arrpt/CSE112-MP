#! /usr/bin/env python3
import re

def R_add(rd, rs1, rs2):
    funct7 = '0000000'
    funct3 = '000'
    opcode = '0110011'


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

f = open('test.s', 'r')
data = f.readlines()
for x in data:
    print(x.split())

registers = {
    "x0": '00000',
    "x1": '00001',

}