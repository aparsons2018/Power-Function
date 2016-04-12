

def power(base, exponent): 
	''' Takes a base and puts it to the power of the input exponant
	and then returns the product'''
	
	tally = 0
	answer = 1
	while tally < exponent:
		answer = base * answer
		tally += 1
	
	return answer

#--------------MAIN PROGRAM--------------

base = int(input("What will the base be?"))
exponent = int(input("What will the exponent be?"))

answer = power(base, exponent) 

print("{} to the power of {} is {}".format(base,exponent,answer))
