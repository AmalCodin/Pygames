import pygame

#constant and variables

WHITE = (255, 255, 255)

BLACK = (0, 0, 0)

WIDTH = 600

HEIGHT = 600

pygame.init()
game_font = pygame.font.SysFond('Arial', 40)

delay = 30

paddle_speed = 20

paddle_width = 10

paddle_height = 100

p1_x_pos = 10

p1_y_pos = HEIGHT / 2 - paddle_height / 2

p2_x_pos = WIDTH - paddle_width - 10

p2_y_pos = HEIGHT / 2 - paddle_height / 2

p1_score = 0

p2_score = 0

p1_up = False

p1_down = False

p2_up = False

p2_down = False

ball_x_pos = WIDTH / 2

ball_y_pos = HEIGHT / 2

ball_width = 8

ball_x_vel = -10

ball_y_vel = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_objects():
    pygame.draw.rect(screen, WHITE, (int(p1_x_pos, p1_y_pos), paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (int(p2_x_pos, p2_y_pos), paddle_width, paddle_height))
    pygame.draw.circle(screen, WHITE, (ball_x_pos, ball_y_pos), ball_width)
    score = game_font.render(f"{str(p1_score)} - {str(p2_score)}", False, WHITE)
    screen.blit(score, (WIDTH/2, 30))

def apply_player_moment():
    global p1_y_pos
    global p2_y_pos

    if p1_up:
        p1_y_pos = max(p1_y_pos - paddle_speed, 0)

    elif p1_down:
        p1_y_pos = min(p1_y_pos + paddle_speed, HEIGHT)

    if p2_up:
        p2_y_pos = max(p2_y_pos - paddle_speed, 0)

    elif p2_down:
        p2_y_pos = min(p2_y_pos + paddle_speed, HEIGHT)

def apply_ball_movement():
    global ball_x_pos
    global ball_y_pos
    global ball_x_vel
    global ball_y_vel
    global p1_score
    global p2_score


    if (ball_x_pos + ball_x_vel < p1_x_pos + paddle_width) and (p1_y_pos <  ball_y_vel + ball_width < p1_y_pos + paddle_height):
        