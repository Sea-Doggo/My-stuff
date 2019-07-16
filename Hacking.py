
from uagame import Window

# create window 

window = Window('hacking', 600, 500)
window.set_font_color('green')
window.set_font_name('couriernew')
window.set_bg_color('black')
window.set_font_size(18)

line_y = 0
string_height = window.get_font_height()

# displaying atempts left
window.draw_string("1 ATTEMPT(S) LEFT", 0, line_y)
window.update()
line_y = line_y + string_height

# displaying password list
window.draw_string('Dat-boi', 0, line_y)
window.update()
line_y = line_y + string_height

window.draw_string('Doge', 0, line_y)
window.update()
line_y = line_y + string_height

#prompt user for password
guess = window.input_string("please enter your password:",0, line_y)
window.update()
line_y = line_y + string_height

#clear window
window.clear()

# create outcome
if guess == 'Doge':
    window.draw_string('SUCCESS!!', 0, 0)
    window.update()    
else:
    window.draw_string('FAILURE!!', 0, 0)
    window.update()
    

#prompt user for password
guess = window.input_string('ENTER PASSWORD > ', 0, line_y)

# prompt for end
window.input_string('PRESS ENTER TO QUIT', 0, line_y)

# close windoww
window.close()