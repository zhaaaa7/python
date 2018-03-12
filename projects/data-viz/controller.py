import pygame
import view
import model
import button
from view import BarChart
from button import Button

BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (127, 127, 127)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)

clickedbuttons=['dem', 'up', 'raw']


class DataChangeButton(Button):

	def __init__(self, text, rect, chart, party='dem',ascend=True,raw=True):
		Button.__init__(self, text, rect)
		self.chart=chart
		self.party=party
		self.ascend=ascend
		self.raw=raw
	

	def handle_event(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			(x, y) = pygame.mouse.get_pos()
			if x >= 1000 and x <= 1150 and y >= 100 and y <= 140:
				self.party='dem'
				clickedbuttons[0]='dem'

			if x >= 1000 and x <= 1150 and y >140 and y <= 180:
				self.party='gop'
				clickedbuttons[0]='gop'

			if x >= 1000 and x <= 1150 and y >= 300 and y <= 340:
				self.ascend=True
				clickedbuttons[1]='up'

			if x >= 1000 and x <= 1150 and y > 340 and y <= 380:
				self.ascend=False
				clickedbuttons[1]='down'

			if x >= 1000 and x <= 1150 and y >= 500 and y <= 540:
				self.raw=True
				clickedbuttons[2]='raw'

			if x >= 1000 and x <= 1150 and y > 540 and y <= 580:
				self.raw=False
				clickedbuttons[2]='%'



		data=model.get_data(party=self.party, raw=self.raw, sort_ascending=self.ascend, year=2016)
		self.chart.set_values(data)
	







pygame.init()

screen = pygame.display.set_mode((1200, 800))

pygame.display.set_caption("Election Data Viewer")
pygame.display.update()
screen_rect=screen.get_rect()

bc=BarChart(rect=screen.get_rect(),values=model.get_data(party='dem', raw=True, sort_ascending=True, year=2016),ticks=4)	

button1 = DataChangeButton("dem",pygame.Rect(1000, 100, 150, 40),bc)
button2 = DataChangeButton("gop",pygame.Rect(1000, 140, 150, 40),bc)
button3 = DataChangeButton("up",pygame.Rect(1000, 300, 150, 40),bc)
button4 = DataChangeButton("down",pygame.Rect(1000, 340, 150, 40),bc)
button5 = DataChangeButton("raw",pygame.Rect(1000, 500, 150, 40),bc)
button6 = DataChangeButton("%",pygame.Rect(1000, 540, 150, 40),bc)

allbuttons=[button1,button2,button3,button4,button5,button6]

# display loop
done = False
while not done:
	screen.fill(view.BLACK)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		else:

			button1.handle_event(event)
			button2.handle_event(event)
			button3.handle_event(event)
			button4.handle_event(event)
			button5.handle_event(event)
			button6.handle_event(event)

	bc.draw(screen)
	for i in allbuttons:
		if i.text in clickedbuttons:
			i.draw(screen,RED)
		else:
			i.draw(screen,GRAY)
	pygame.display.update()	

pygame.quit()


