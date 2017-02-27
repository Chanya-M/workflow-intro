#Declaration of function compare; its arguments are the two arrays to compare
def compare(a, b):
	alice_score = 0
	bob_score = 0
	#Compare corresponding values of the arrays
	for i, j in zip(a, b):       
	    if i > j:
	        alice_score += 1
	    elif i < j:
	        bob_score += 1
	#Return the scores
	return alice_score, bob_score