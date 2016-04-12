

def power(base, exponent):

	if exponent <= 0:
		return 1
	if exponent == 1:
		return base
	
	return base * power(base, exponent-1)
	
def int_input(question):
	answer = input(question) 
	try:
		answer = int(answer)
		return answer
	except ValueError:
		return int_input("That was not an integer; Try again. ")


def float_input(question):
	answer = input(question)
	try:
		answer = float(answer)
		return answer
	except:
		return float_input("That was not an integer; Try again. ")
	
#------Test Cases---------

print("{} to the power of {} is {}. ".format( 3, 4, power(3,4))) 
print("{} to the power of {} is {}. ".format( 7, 4, power(7,4)))
print("{} to the power of {} is {}. ".format( 5, 0, power(5,0)))
print("{} to the power of {} is {}. ".format( 0, 9, power(0,9)))
print("{} to the power of {} is {}. ".format( 0, 0, power(0, 0))) 


#------Main Program--------
base = int_input("Welcome to the Power Function. \n Please enter a base. ")
exponent = float_input("Now enter a exponent. ") 

total = power(base, exponent) 

print("{} to the power of {} is {}. ".format( base, exponent, total)) 