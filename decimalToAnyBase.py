# Given a decimal number A and a base B, convert it into its equivalent number in base B.

# Input
# A = 4
# B = 3

# Output
# 11

def decimal(number,base):
    binary=""
    while number>0:
        binary+=str(number%base)
        number=number//base
    return binary[::-1]

number=int(input())
base=int(input())
print(decimal(number,base))
