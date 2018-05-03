import pygame
from barchart import BarChart
from button import Button
import fruitmodel


pygame.init()

screen = pygame.display.set_mode((1000,600))

pygame.display.set_caption("Bar Chart Viewer")
pygame.display.update()

data1 = fruitmodel.get_data()
data2=fruitmodel.get_sorted_data()

screen_rect = screen.get_rect()
bc1_rect = pygame.Rect(screen_rect.x, screen_rect.y, 
  screen_rect.width, screen_rect.height) # make it the full height again

bc1 = BarChart(bc1_rect, data1)

bc2=BarChart(bc1_rect, data2)

button = Button("Change", pygame.Rect(10, screen_rect.height - 70, 150, 60))

# display loop
done = False
flag=0
while not done:
	screen.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		else:
			button.handle_event(event)
			if flag%2==0:
				bc1.draw(screen)
			else:
				bc2.draw(screen)
	button.draw(screen)
	pygame.display.update()
	flag+=1

pygame.quit()

