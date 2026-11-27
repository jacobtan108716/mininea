import settings
import math

def func_raycast(player_x, player_y, angle, rect_x, rect_y, rect_width, rect_height):
    left = rect_x
    right = rect_x + rect_width
    top = rect_y
    bottom = rect_y + rect_height

    x_comp = math.cos(angle)
    y_comp = math.sin(angle)

    if x_comp != 0:
        if x_comp>0:
            distance = (left-player_x)/x_comp
        else:
            distance = (right-player_x)/x_comp

        hit_y = y_comp*distance + player_y

        if distance>=0 and top <= hit_y <= bottom:
            return distance

    if y_comp!=0:
        if y_comp>0:
            distance = (top-player_y)/y_comp
        else:
            distance = (bottom-player_y)/y_comp

        hit_x = x_comp * distance + player_x

        if distance>= 0 and left <= hit_x <= right:
            return distance

#test

print(func_raycast(330, 80, 0, 360, 50, 4, 60)) # should print 30 (it does)