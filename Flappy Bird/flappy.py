from game import BG
import pygame

pygame.init()

screen_width = 800

screen_height = int(screen_width + 0.8)

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Flappy Bird')

#defining framerate

clock = pygame.time.Clock()
fps = 60

#defining player action vairables

moving_up = False

#defining background colors

bg = (144, 201, 120)


def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))


def draw_bg():
	screen.fill(BG)
	width = sky_img.get_width()
	for x in range(5):
		screen.blit(sky_img, ((x * width) - bg_scroll * 0.5, 0))
		screen.blit(mountain_img, ((x * width) - bg_scroll * 0.6, SCREEN_HEIGHT - mountain_img.get_height() - 300))
		screen.blit(pine1_img, ((x * width) - bg_scroll * 0.7, SCREEN_HEIGHT - pine1_img.get_height() - 150))
		screen.blit(pine2_img, ((x * width) - bg_scroll * 0.8, SCREEN_HEIGHT - pine2_img.get_height()))

