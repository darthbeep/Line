from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

#S
draw_line(screen, 120, 450, 80, 420, color)
draw_line(screen, 80, 420, 80, 380, color)
draw_line(screen, 80, 380, 140, 350, color)
draw_line(screen, 140, 350, 140, 300, color)
draw_line(screen, 70, 260, 140, 300, color)
#H
draw_line(screen, 200, 450, 200, 260, color)
draw_line(screen, 300, 260, 300, 450, color)
draw_line(screen, 300, 350, 200, 375, color)
#A
draw_line(screen, 400, 450, 350, 260, color)
draw_line(screen, 400, 450, 450, 260, color)
draw_line(screen, 375, 355, 425, 355, color)
#I
draw_line(screen, 100, 50, 100, 240, color)
#N
draw_line(screen, 200, 50, 200, 240, color)
draw_line(screen, 300, 50, 300, 240, color)
draw_line(screen, 200, 240, 300, 50, color)
#A
draw_line(screen, 350, 50, 400, 240, color)
draw_line(screen, 450, 50, 400, 240, color)
draw_line(screen, 425, 145, 375, 145, color)
#draw_line(screen, 300, 200, 100, 500, color)



display(screen)


save_extension(screen, 'img.png')
