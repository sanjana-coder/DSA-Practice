#given 4 digit int, determine if the number is a special number
#number is special if sum of first 2 digits == sum of last 2 digits

num = int(input())
digit = []
i = 0

while num>0:
	digit.append(num%10)
	num = num//10
	i+=1

if digit[0]+digit[1] == digit[2]+digit[3]:
	print(True)
else:
	print(False)