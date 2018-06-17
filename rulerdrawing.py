def draw_line(length, label = ''):
	stri = ''
	for i in range(length):
		stri += '-'
	if label:
		stri += label
	print(stri)

def draw_interval(center_length):
	if(center_length > 0):
		draw_interval(center_length - 1)
		draw_line(center_length)
		draw_interval(center_length - 1)

def draw_ruler(num_inches, major_length):
	draw_line(major_length, '0')
	for i in range(1, num_inches + 1):
		draw_interval(major_length - 1)
		draw_line(major_length, str(i))

draw_ruler(5, 4)
