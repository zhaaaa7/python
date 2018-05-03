import pygame

pygame.init()

Display = pygame.display.set_mode((600,300))

pygame.display.set_caption("Bar Graph")
pygame.display.update()

white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)

# You will be visualizing this data. 
# (Label, Color of the bar, Length of the bar)
data = [('Apple',red,150), ('Banana',yellow,450), ('Melon',green,280)]

# Design your own Class
# The class should be initialized with the label, color, and length of each item in the 'data' list.

class Bar:
	def __init__(self, tuple1):
		self.label = tuple1[0]
		self.color=tuple1[1]
		self.length=tuple1[2]

# The class should have a function(or multiple functions) to draw a bar graph.
	def writelabel(self,y):
	# Creating a string object.
		f = pygame.font.Font(None, 25)
	# Rendering this string object.
		t = f.render(self.label, False, black)
	# Displaying this text on the window.
		Display.blit(t, (5,y))

	def drawbar(self,y):
		pygame.draw.rect(Display, self.color, [70,y, self.length,50])

gameExit = False
while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		Display.fill(white)
	# Write the codes to draw a graph based on 'data' list.
		y=10
		for i in data:
			b=Bar(i)	
			b.writelabel(y+15)	
			b.drawbar(y)
			y+=60
		pygame.display.update()	


pygame.quit()
quit()