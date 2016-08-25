from utilities import *

def flood(color_of_tile, flooded_list, screen_size):
	i = 0;
	while (i<len(flooded_list)):
		if in_bounds(down(flooded_list[i]),screen_size):
			if (down(flooded_list[i])) not in flooded_list :
				if color_of_tile[flooded_list[i]] == color_of_tile[down(flooded_list[i])]:
					flooded_list.append(down(flooded_list[i]))
		
		if in_bounds(left(flooded_list[i]),screen_size):
			if (left(flooded_list[i])) not in flooded_list :
				if color_of_tile[flooded_list[i]] == color_of_tile[left(flooded_list[i])]:
					flooded_list.append(left(flooded_list[i]))
		if in_bounds(up(flooded_list[i]),screen_size):
			if (up(flooded_list[i])) not in flooded_list :
				if color_of_tile[flooded_list[i]] == color_of_tile[up(flooded_list[i])]:
					flooded_list.append(up(flooded_list[i]))
		if in_bounds(right(flooded_list[i]),screen_size):
			if right(flooded_list[i]) not in flooded_list :
				if color_of_tile[flooded_list[i]] == color_of_tile[right(flooded_list[i])]:
					flooded_list.append(right(flooded_list[i]));
		
		i = 1 + i
	
