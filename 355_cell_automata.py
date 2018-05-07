from tkinter import *
import argparse

#submission  5e73c314-5d56-4382-8a09-83d48ff2d051.

parser = argparse.ArgumentParser (description='Generates any elementary cellular automata')
parser.add_argument("-rule", "--rule", required = True, help ='the rule number for an input. From 0 to 256')
parser.add_argument("-iter", "--iter", required = True, help ='the number of lines of cells you want to generate')
args = parser.parse_args()

args = vars(parser.parse_args())

#generate input cells array
MAX_ITER = int(args['iter'])
SIZE = 200
MID = SIZE/2
cells = ["0" for i in range(0,SIZE)]
cells[MID] = "1"


def dec2bin(dec):
    output = []
    output.append(str(0 if dec%2 == 0 else 1))
    while dec > 1:
        dec = dec // 2
        output.append(str(0 if dec%2 == 0 else 1) + " ")
    output.reverse()
    return ''.join(output)

def generate_states(dec):
	num = dec2bin(dec)
	temp = num.split(' ')[::-1]
	while len(temp) < 8:
		temp.append(0)
	num = temp[::-1]
	num = [str(x) for x in num]
	states = ["111", "110", "101", "100", "011", "010", "001", "000"]
	new_state = dict(zip(states, num))
	return new_state

new_state = {}
num = int(args['rule'])

new_state = generate_states(num)


color_map = {"0":"blue", "1":"green"}




size = int(args['iter']) * 10
root = Tk()
title = "Rule: " + args['rule']
root.title(title)
frame = Frame(root, width=400*5, height=size)
frame.grid(row=0,column=0)
canvas = Canvas(frame, width=400*5, height=size, scrollregion=(0,0,400*5,size))

hbar = Scrollbar(frame, orient=HORIZONTAL)
hbar.pack(side=BOTTOM,fill=X)
hbar.config(command=canvas.xview)

vbar=Scrollbar(frame,orient=VERTICAL)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=canvas.yview)

canvas.config(width=700,height=700)
canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
canvas.pack(side=LEFT,expand=True,fill=BOTH)






def new_cell(cells):
	new_cells = ["0" for i in range(0,SIZE)]
	for i in range(1, len(cells)-1):
		curr = cells[i-1] + cells[i] + cells[i+1]
		curr = new_state[curr]
		new_cells[i] = curr
	return new_cells

y = 0
def gen_new_line(cells):
	x = 0
	size = 10
	global y
	for cell in cells:
		canvas.create_rectangle(x,y, x+size , y+size, outline = "black", fill = color_map[cell])
		x = x + size
	y = y + size


#loop until we reach max_iter
for i in range(0, MAX_ITER):
	gen_new_line(cells)
	cells = new_cell(cells)







canvas.update()


root.mainloop()