'''
There was a teacher in a small town who loves coding
and he wants to create a program which prints out the 
whole multiplication table of an entered number for 
his students.Can you help him to wrie a program in python
'''
def multiplication_table(number):
	table = []
	for n in range(1,11):
		l =  f'{number} * {n} = {number*n}'
		table.append(l)
	return table
number = int(input('Enter a number to get table :'))
for num in multiplication_table(number):
	print(num)

