import pygame, sys, time, math
from pygame.locals import *

# User-defined classes

# User-defined functions
def update(surface, color, state, center, opaqueColor, selectColor, innerRadius, outerRadius, selectRadius, Opaque, Transparent, Selected) :
	if False:
		return True
	else:
		drawComponent(surface, color, state, center, opaqueColor, selectColor, innerRadius, outerRadius, selectRadius, Opaque, Transparent, Selected)
		return False
 
def drawComponent(surface, color, state, center, opaqueColor, selectColor, innerRadius, outerRadius, selectRadius, Opaque, Transparent, Selected) :
	if state[0] == 0:
		pygame.draw.circle(surface, opaqueColor, center, outerRadius, 0)
	elif state[0] == 1:
		pygame.draw.circle(surface, opaqueColor, center, outerRadius, 0)
		pygame.draw.circle(surface, color, center, innerRadius, 0)
	else:
		pygame.draw.circle(surface, selectColor, center, selectRadius, 0)
		pygame.draw.circle(surface, opaqueColor, center, outerRadius, 0)
		pygame.draw.circle(surface, color, center, innerRadius, 0)
    
def containsPoint(center, eventposition, outerRadius):
	xdistance = abs(center[0] - eventposition[0])
	ydistance = abs(center[1] - eventposition[1])
	distance = math.sqrt(xdistance**2 + ydistance**2)
	if distance < outerRadius:
		return True
	else:
		return False

def handleMouseUp(center, state, eventposition, Selected, Opaque, outerRadius):
	if containsPoint(center, eventposition, outerRadius) :
		return 2
	else:
		
		return 0
	return

def handleMotion(center, state, eventposition, Selected, Transparent, Opaque, outerRadius):
	if state[0] == 2 :
		return 
	if containsPoint(center, eventposition, outerRadius):
		return 1
	else :
		return 0
	return 
   	 
   	 
# Main program
def main():
	# Initialize pygame
	pygame.init()
	
	# Set window size and title, and frame delay
	surfaceSize = (500, 400) # example window size
	windowTitle = 'Bypass' # example title
	#frameDelay = 0.02 # smaller is faster game
	
	# Create the window
	surface = pygame.display.set_mode(surfaceSize, 0, 0)
	pygame.display.set_caption(windowTitle)
	
	
	# create and initialize objects
	gameOver = False
	opaqueColor = pygame.Color('blue')
	selectColor = pygame.Color('red')
	outerRadius = 15
	innerRadius = 10
	selectRadius = 17
	coverCenter = [50, 50]
	
	Opaque = 0
	Transparent = 1
	Selected = 2
	center = (50,50)
	color = pygame.Color('yellow')
	state = [0]
	
			 
	# Draw objects
	drawComponent(surface, color, state, center, opaqueColor, selectColor, innerRadius, outerRadius, selectRadius, 'Opaque', 'Transparent', 'Selected')
	
	# Refresh the display
	pygame.display.update()
	
			 
	# Loop forever
	while True:
		#Obtain cursor position
		pos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
		 # Handle events
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			# handle additional events
			if event.type == pygame.MOUSEBUTTONUP and gameOver == False:
				state[0]=handleMouseUp(center, state, pos, 'Selected', 'Opaque', outerRadius)
				if state[0]==0:
					#Fill screen with black color.
					surface.fill((0,0,0))
					drawComponent(surface, color, state, center, opaqueColor, selectColor, innerRadius, outerRadius, selectRadius, 'Opaque', 'Transparent', 'Selected')
					pygame.draw.circle(surface, (255,255,255), pos, 10)
					pygame.draw.circle(surface, (0,0,0), pos, 8)
					pygame.display.update()
					time.sleep(0.5)
					pygame.draw.circle(surface, (0,0,0), pos, 10)
					pygame.display.update()
				else: 
					print ("draw inside")
					pygame.draw.circle(surface, (0,0,0), pos, 6)
					pygame.draw.circle(surface, color, pos, 4)
					pygame.display.update()
					time.sleep(0.5)
					
			
			elif event.type == pygame.MOUSEMOTION and gameOver == False:
				state[0]=handleMotion(center, state, pos, 'Selected', 'Transparent','Opaque', outerRadius)

		pygame.display.update()
			
			
		gameOver = update(surface, color, state, center, opaqueColor, selectColor, innerRadius, outerRadius, selectRadius, 'Opaque', 'Transparent', 'Selected')
	    
	# draw a circle around the mouse pointer
		#pos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
		#    
		 
	  # Update and draw objects for the next frame
	
	
	  # Refresh the display
		#pygame.display.update()
	
	  # Set the frame speed by pausing between frames
		#time.sleep(frameDelay)
		
main()