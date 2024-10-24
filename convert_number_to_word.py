#Write a program that converts a 2-digit integer (between 10 and 99) into its word representation using if-else statements.

def convert_num_to_word(num):
	eleven_to_nineteen = ["Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
	tens = ["Ten","Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
	one_to_nine = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
	if num < 10 or num > 99:
		print("Enter a valid number")
		return
	if num%10 == 0:
		num = num//10
		num -=1
		print(tens[num])
	elif 11<=num<=19:
		num = num-11
		print(eleven_to_nineteen[num])
	else:
		first_digit = num//10
		last_digit = num%10
		
		first_digit-=1
		last_digit-=1
		print(tens[first_digit]+one_to_nine[last_digit])
		
	
	
num = int(input())
convert_num_to_word(num)