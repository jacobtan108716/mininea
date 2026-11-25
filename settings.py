#this file is for all the settings of the game
#it is a python file
#one setting per line, then =, then its value

#we always write settings before the actual code for anything else is written
#this has several benefits: we don't make numbers up on the fly and have everything preplanned
#everything else also uses import settings so everything is dependent on this file

grid_columns = 10
grid_rows = 10
tile_size = 60
board_left_edge_x = 300 #x coordinate of the left edge of the board
board_top_edge_y = 50 #y coordinate of the top edge of the board
fps = 60 #fps = 60
window_w = 1200
window_h = 700


#menu

menu_text_colour = (255,255,255)

#maze
wall_thickness = 4
wall_num_of_walls_to_remove = 10
wall_chance_to_remove = 0.02
wall_colour = (255,255,255)

floor_colour = (200,200,200) 

maze_border_thickness = 6
maze_border_colour = (255,255,255)



#player
player_colour = (0,0,255) #player is completely blue (for now)
player_size_area = 20