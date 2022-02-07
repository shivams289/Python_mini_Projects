number = 21 # .....00000010101
print('Mask:', bin(1 << 4))
#find ith bit
def find_ith_bit(number, i):
	mask = 1 << i #so that 1 is at the ith bit position and every other bit will be 0
	return number & mask # if ith bit in the number is 1, this will return 1, else 0

print(f'5th bit of {number} is -->{find_ith_bit(number, 4)} --> bit format:{bin(find_ith_bit(number, 4))}')

#set ith bit
def set_bit(number, i):
	mask = 1 << i # so that 1 is at the ith bit position and every other bit is 0
	return (number | mask) # if ith bit is o or 1, it will set it to 1, leaving others as it is

print(f'Set 5th bit of {number}-->{set_bit(number, 4)} --> bit format:{bin(set_bit(number, 4))}')

def clear_bit(number, i):
	mask = 1 << i #if i =4 --> .....0000010000
	mask = ~mask # --> ....11111101111

	return number & mask #ith bit will be changed to 0, others left as it is

print(f'Clear 5th bit of {number}-->{clear_bit(number, 4)} --> bit format:{bin(clear_bit(number, 4))}')
count = 0
while(number & (number -1)):
	count +=1

print(count)


