#######################################################################################################
#####   STEP 1. Input PN number 																	###
#####   STEP 2. Input Seed value (should be non all-zero array)										###
#######################################################################################################

from collections import deque

PN_number = input("Input PN Number:\n")
type(PN_number)

PN_number = int(PN_number)

total_Length = 2**PN_number - 1

seed = input("Input Non-Zero Seed as an array separated by commas (only 0s and 1s are allowed) :\n")
type(seed)
seed.split(", ")

if PN_number < int((len(seed)+1)/2) :
	print("Seed length is GREATER than PN number. Quitting....")
	exit(-1)

for n in range(0,len(seed),2):
	if int(seed[n]) != 1 and int(seed[n]) != 0:
		print("Seed value is INVALID. Only 0's and 1's are allowed. Quitting....")
		exit(-1)
	
temp_seed = [None] * PN_number;
i = 0;

for n in range(0,len(seed),2):
	temp_seed[i] = (seed[n])
	i=i+1

if PN_number >= int((len(seed)+1)/2) :
	#append zeroes in the beginning	
	seed_item = deque(temp_seed)
	
	for n in range(0,PN_number - int((len(seed)+1)/2)):
		seed_item.rotate(1)
		seed_item[0] = 0


print("seed = "+str(seed_item))
temp_seed = seed_item
	
for i in range(0,total_Length):
	xor = int(temp_seed[PN_number - 1]) ^ int(temp_seed[PN_number-2])
	
	item = deque(temp_seed)
	
	item.rotate(1)
	item[0] = xor
	
	temp_seed = item
	
	print(str(xor))


	



		
				
				
				
				
				
				
				
				
				
				
	
	
	
