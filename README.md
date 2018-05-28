# PN_Generator
Generates a PN sequence based on the user input of PN number and seed sequence.
Seed sequence should be a comma separated array, e.g., 1,0,1,1,0
The above example is for PN input of 5. If the length of seed is less than PN number value, 0's will be padded at the beginning of the sequence to make it equal to the value of PN number.    
If length of seed is greater than PN number, the program will quit. If any of the seed values is other than 0 or 1, the program will quit.
