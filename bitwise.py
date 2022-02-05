a = 15 # = .....0001111
b = 8 # = .....0001000

# a AND B
# a = 1111
# b = 1000
#result = 1000 == 8
print('a AND b -->',a & b)

# a OR B
# a = 1111
# b = 1000
#result = 1111 == 15
print('a OR b -->',a | b)

# Not a
# a = 1111
#result = .......1111110000 == out of bound
print('Not a -->', ~a)

# a XOR B
# a = 1111
# b = 1000
#result = 0111 == 7
print('a XOR b -->',a ^ b)

print('\n-----Right shift is actially a number divided by 2^(number of shifts)-----')
# a Right Shift 1 
# a = 1111 #If it is represented in all bits ....00000001111
#result = ....00000111 == 7
print('a Right Shift 1 -->',a >> 1)

# a Right Shift 2 
# a = 1111 #If it is represented in all bits ....00000001111
#result = ....0000011 == 3
print('a Right Shift 1 -->',a >> 2, '\n')

print('--------Left shift is actually multiplication of a number by 2^(number of shifts)-----')
# a Left Shift 1 
# a = 1111 #If it is represented in all bits ....00000001111
#result = ....0000011110 == 30
print('a Left Shift 1 times -->',a << 1)

# a Left Shift 2 
# a = 1111 #If it is represented in all bits ....00000001111
#result = ....00000111100 == 30
print('a Left Shift 2 times -->', a << 2)  