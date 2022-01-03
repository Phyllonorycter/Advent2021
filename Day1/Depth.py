external_file = open('input.txt')

text_input = list(external_file.readlines())

a = 1
b = 0
increasing = decreasing = 0
while a < len(text_input):
	
	if text_input[a] > text_input[b]:
		increasing += 1
	else:
		decreasing += 1
	a += 1
	b += 1
print("increasing=", increasing, ' ', "decreasing=", decreasing)
