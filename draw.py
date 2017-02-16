from display import *
import math

def draw_line( screen, x0, y0, x1, y1, color ):
	octant1(screen, x0, y0, x1, y1, color)
	octant2(screen, x0, y0, x1, y1, color)
	octant3(screen, x0, y0, x1, y1, color)
	octant4(screen, x0, y0, x1, y1, color)
	upsideDown(screen, x0, y0, x1, y1, color)
	horver(screen, x0, y0, x1, y1, color)
pass

def octant1( screen, x0, y0, x1, y1, color ):
	if x1 > x0 and y1 > y0 and abs(x1 - x0) >= abs(y1 - y0):
		A = abs(y1-y0) * 2
		B = abs(x1-x0) * -2
		x=x0
		y=y0
		d = A + B
		while (x <= x1):
			plot(screen, color, x, y)
			if (d > 0):
				y = y+1
				d+=B
			x=x+1
			d+=A

def octant2( screen, x0, y0, x1, y1, color ):
	if x1 > x0 and y1 > y0 and abs(x1 - x0) < abs(y1 - y0):
		A = abs(x1-x0) * 2
		B = abs(y1-y0) * -2
		x=x0
		y=y0
		d = A + B
		while (y <= y1):
			plot(screen, color, x, y)
			if (d > 0):
				x = x+1
				d+=B
			y=y+1
			d+=A

def octant3( screen, x0, y0, x1, y1, color ):
	if x1 < x0 and y1 > y0 and abs(x1 - x0) < abs(y1 - y0):
		A = abs(x1-x0) * 2
		B = abs(y1-y0) * -2
		x=x0
		y=y0
		d = A + B
		while (y <= y1):
			plot(screen, color, x, y)
			if (d > 0):
				x = x-1
				d+=B
			y=y+1
			d+=A

def octant4( screen, x0, y0, x1, y1, color ):
	if x1 < x0 and y1 > y0 and abs(x1 - x0) >= abs(y1 - y0):
		A = abs(y1-y0) * 2
		B = abs(x1-x0) * -2
		x=x0
		y=y0
		d = A + B
		while (x >= x1):
			plot(screen, color, x, y)
			if (d > 0):
				y = y+1
				d+=B
			x=x-1
			d+=A

#It's a lazy solution but I'm proud
def upsideDown(screen, x0, y0, x1, y1, color):
	if y0 > y1:
		octant1(screen, x1, y1, x0, y0, color)
		octant2(screen, x1, y1, x0, y0, color)
		octant3(screen, x1, y1, x0, y0, color)
		octant4(screen, x1, y1, x0, y0, color)

def horver(screen, x0, y0, x1, y1, color):
	if x0 == x1:
		x=x0
		if y0 < y1:
			y = y0
			while y < y1:
				plot(screen, color, x, y)
				y = y+1
		if y0 > y1:
			y = y1
			while y < y0:
				plot(screen, color, x, y)
				y = y+1
	if y0 == y1:
		y=y0
		if x0 < x1:
			x = x0
			while x < x1:
				plot(screen, color, x, y)
				x = x+1
				#print [x, y]
		if x0 > x1:
			x = x1
			while x < x0:
				plot(screen, color, x, y)
				x = x+1
				#print [x, y]
