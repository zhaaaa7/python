import pygame
import math

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE=(255,255,255)

class Bar:

	def __init__(self, color, length, height, padding=0.1):
		self.length = length
		self.color = color
		self.height = height
		self.padding = padding

	def draw(self, surface, x, y):
		padding_height = self.height * self.padding
		adjusted_height = self.height - 2 * padding_height
		pygame.draw.rect(surface, self.color, 
		  [x, y + padding_height, self.length, adjusted_height])

# a class to display a horizontal bar chart in pygame
class BarChart:


	# rect: a pygame.rect encoding size and position
	def __init__(self, rect=pygame.Rect(0,0,600,400), values=[], ticks=10, plot_area_width_ratio=0.8, 
		plot_area_height_ratio=0.8, bar_color=GREEN, max_val=0):
		self.rect=rect
		self.ticks=ticks

		self.plot_area_width_ratio = plot_area_width_ratio
		self.plot_area_height_ratio = plot_area_height_ratio

		self.label_area_width_ratio = (1-self.plot_area_width_ratio)/2
		self.scale_area_height_ratio = 1-self.plot_area_height_ratio

		self.scale_area=pygame.Rect(
			rect.x+rect.width*self.label_area_width_ratio,
			rect.y + rect.height * self.plot_area_height_ratio,  
			rect.width * self.plot_area_width_ratio,
			rect.height * self.scale_area_height_ratio)

		self.label_area = pygame.Rect(
			rect.x,
			rect.y,
			rect.width * self.label_area_width_ratio,
			rect.height * self.plot_area_height_ratio
			)

		self.plot_area = pygame.Rect(
			rect.x + self.label_area.width,
			rect.y,
			rect.width * self.plot_area_width_ratio,
			rect.height * self.plot_area_height_ratio
			)

		self.color=bar_color
		self.val=max_val
		self.set_values(values)

	def set_values(self,values):
		self.values=values
		max=0
		for i in self.values:
			if i[1]>max:
				max=i[1]
		self.numerica_max=max

		if self.val!=0:
			self.max_val=self.val
		else:
			self.max_val=self.numerica_max


	

	def get_bar_height(self):
		return self.plot_area.height / len(self.values)

	def draw_labels(self,screen):
		count=0	
		for i in self.values:
			label_text=i[0]
			font=pygame.font.Font(None,15)
			label_view=font.render(label_text,False, WHITE)
			label_pos=label_view.get_rect()
			label_pos.centery=self.rect.y+self.get_bar_height()*count+self.get_bar_height()/2
			label_pos.x=self.label_area.width*self.label_area_width_ratio
			screen.blit(label_view,label_pos)
			count+=1
	def draw_scale(self,screen):
		scale_label_spacing=self.scale_area.width/self.ticks

		for i in range(self.ticks+1):
			f=pygame.font.Font(None,25)

			if self.max_val<1:
				text=1/self.ticks*i
			else:
				text=round(self.max_val/self.ticks*i,1)

			scale_label_view=f.render(str(text),False,WHITE)
			scale_label_pos=scale_label_view.get_rect()
			scale_label_pos.y=self.scale_area.y+10
			scale_label_pos.x=self.scale_area.x+i*scale_label_spacing-10
			screen.blit(scale_label_view,scale_label_pos)

	def draw_bars(self,screen):
		bar_num=0
		for i in self.values:
			if self.numerica_max<1:
				bar_length=self.plot_area.width*i[1]/1
			else:
				bar_length=self.plot_area.width*i[1]/self.numerica_max				
			b=Bar(self.color, bar_length,self.plot_area.height/len(self.values))
			y_pos=self.plot_area.y+bar_num*b.height
			bar_num+=1
			b.draw(screen,self.plot_area.x,y_pos)


	def draw(self,screen):
		self.draw_bars(screen)                
		self.draw_labels(screen)
		self.draw_scale(screen)
		




# SELF-TESTING MAIN
if __name__ == "__main__":

	pygame.init()

	screen = pygame.display.set_mode((1000,700))

	pygame.display.set_caption("Bar Chart Test")
	pygame.display.update()

	data =	[
			("apples", 6), 
			("bananas", 7), 
			("grapes", 4),
			("pineapple", 1),
			("cherries", 15)
			]   

	# display using default values			
	bc = BarChart(values=data)
	


	data2 = [
			('Jenny', 80),
			('Stanley', 90),
			('Timothy', 92)
			]

	# override all of the defaults
	bc2 = BarChart(
		rect=pygame.Rect(0,400,800,150), 
		values=data2, 
		ticks=5, 
		plot_area_width_ratio=0.85, 
		plot_area_height_ratio=0.9, 
		bar_color=RED,
		max_val=100
		)

	# display loop
	done = False
	while not done:
		screen.fill(BLACK)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

		bc.draw(screen)
		bc2.draw(screen)
		pygame.display.update()


	pygame.quit()
	quit()


