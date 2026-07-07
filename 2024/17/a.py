#0: adv (num A register, den 2^combo operand ... truncated to integer and placed into A)
#1: bxl (B XOR literal operand ... stored in B)
#2: bst (combo operand mod 8 ... keeps lowest three bits and stored in B)
#3: jnz (nothing if A is 0, else jump by setting instruction pointer to the value of the literal operand ... if it jumps, the instruction pointer is not increased by two after this operation)
#4: bxc (B XOR C, stores in B. reads operand but ignores it
#5: out (calculate value of combo operand mod 8 then outputs it)
#6: bdv (like adv but result is stored in B instead)
#7: cdv (like adv but result is stored in C instead)

registers = {
  "A": 0,
  "B": 0,
  "C": 0
}

with open(input(), "r") as f:
  lines = f.readlines()

for line in lines:
  if not line.strip(): continue
  line=line.strip().split()
  print(line)
  if line[0]=="Register":
    registers[line[1][0]]=int(line[2])
  if line[0]=="Program:": program=list(map(int, line[1].split(",")))

print(registers, program)


def combo(x):
  if x in range(0, 4): return x
  if x == 4: return registers["A"]
  if x == 5: return registers["B"]
  if x == 6: return registers["C"]

def literal(x):
  return x

def adv(operand, pointer):
  registers["A"]=int(registers["A"]/(2**combo(operand)))
  return pointer+2

def bxl(operand, pointer):
  registers["B"]=registers["B"]^literal(operand)
  return pointer+2

def bst(operand, pointer):
  registers["B"]=combo(operand)%8
  return pointer+2

def jnz(operand, pointer):
  if registers["A"] == 0: return pointer+2
  return literal(operand)

def bxc(operand, pointer):
  registers["B"]=registers["B"]^registers["C"]
  return pointer+2

def out(operand, pointer):
  print(combo(operand)%8, end=",")
  return pointer+2

def bdv(operand, pointer):
  registers["B"]=int(registers["A"]/(2**combo(operand)))
  return pointer+2

def cdv(operand, pointer):
  registers["C"]=int(registers["A"]/(2**combo(operand)))
  return pointer+2

pointer=0
funcmap = {
  0: adv,
  1: bxl,
  2: bst,
  3: jnz,
  4: bxc,
  5: out,
  6: bdv,
  7: cdv
}

while pointer < len(program) and pointer >= 0:
  pointer=funcmap[program[pointer]](program[pointer+1], pointer)

