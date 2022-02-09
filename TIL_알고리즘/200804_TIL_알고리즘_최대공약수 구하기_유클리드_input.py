def gcd(a,b):
	if b==0:
		return a
	return gcd(b, a % b)

# a = int(input('input the first number :'))
# b = int(input('input the first number :'))

i = input('input the first number :').split(',')
print(i[0], i[1])
print(gcd(int(i[0]), int(i[1])))




