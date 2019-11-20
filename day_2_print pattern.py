def reverse_pyramid(n):
# 	'''
# 7777777
#  55555
#   333
#    1
# 	'''
	for i in range(n,0,-2):
		print(" "*((n-i)//2),end="")
		for j in range(i):
			print(i,end="")
		print()
reverse_pyramid(7)



''' 11111
	22222
	33333
	44444
	55555'''
# for i in range(1,6):
# 	for j in range(1,6):
# 		print(i,end="")
# 	print()
# def pattern(n):
# 	'''
# 	  1 
#     1 2 
#    1 2 3 
#   1 2 3 4 
#  1 2 3 4 5 
# 	'''
# 	for i in range(1,n+1):
# 		print(" "*(n-i),end="")
# 		for j in range(1,i+1):
# 			print(j,end=" ")
# 		print()
		
# pattern(5)


# def pattern(n):
# 	'''
# 	 1
#     222
#    33333
#   4444444
#  555555555
# 66666666666

# 	'''
# 	for i in range(1,n+1):
# 		print(" "*(n-i),end="")
# 		for j in range(1,2*i):
# 			print(j,end="")
# 		print()
		
# pattern(6)





# def pattern(n):
# 	'''
# 	 1
#     222
#    33333
#   4444444
#  555555555
# 66666666666

# 	'''
# 	for i in range(1,n+1):
# 		print(" "*(n-i),end="")
# 		for j in range(1,2*i):
# 			print('*',end="")
# 		print()
		
# pattern(6)

# def pattern(n):
# 	'''
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 
# 	'''
# 	 for i in range(n,0,-1):
# 	 	for j in range(n-i):
# 	 		print(end=" ")
# 	 	for j in range(i):
# 	 		print("*",end=" ")
# 	 	print()
	 			
# pattern(5)

# def pyramid(rows):
# 	'''
# 	    * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# 	'''
# 	for i in range(rows):
# 		print((" "*(rows-i-1))+"* "*(i+1))

# pyramid(5)



