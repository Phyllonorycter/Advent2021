external_file = open('input.txt', 'r')

text_input = list(external_file.readlines())

text_input = list(map(int,text_input))

a = 1
b = 0
increasing = decreasing = 0

print(type(text_input[0]))

while a < len(text_input):
	
	if sum(text_input[a:a+3]) > sum(text_input[b:b+3]):
		increasing += 1
	else:
		decreasing += 1
	a += 1
	b += 1
print("increasing=", increasing, ' ', "decreasing=", decreasing)
