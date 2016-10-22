"""This is the entry point of the program."""
def create_box(height, width, character):
    box = ''
    for i in range(height):
        for j in range(width):
            box += character
        box += '\n'
    return box

def create_box_empty(height, width, character):
	s = ""

	height = int(height)
	width = int(width)
		
	for i in range(height):
		#print("*", end="")
		for j in range(width):
			if j == 0 or j == width-1 or i == 0 or i == height-1:
				s += "*" + ""
			else:
				s += " " + ''
		s += "\n"

	return(s)
                
       
            
    
    



if __name__ == '__main__':
    
        
    print(create_box(3,4, '*'))


