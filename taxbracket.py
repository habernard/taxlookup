def tax(income: int)->int:
	"""Return tax owed given supplied income."""
	incomeCap = [0,10000,30000,100000,9999999]
	taxRates = [0.00,0.10,0.25,0.40]
	tax = 0.0
	for i in range(len(incomeCap)-1):
		tax = (max(int(income) - incomeCap[i],0) - max(int(income) - incomeCap[i+1],0)) * taxRates[i] + tax

	return int(tax)