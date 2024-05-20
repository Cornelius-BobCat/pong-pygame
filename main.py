import pygame
import random

# init
pygame.init()

# screen

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG")


# constantes
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PINK = (255, 0, 255)
BLACK = (0, 0, 0)
BALL_RADIUS = 10
BALL_SPEED = 5
COEF_SPEED = 1.001
PADDLE_SPEED = 5
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100

score = 0
game_active = False


class Paddle:
    def __init__(self, x):
        self.rect = pygame.Rect(
            x, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT
        )

    def move_up(self):
        self.rect.y -= PADDLE_SPEED
        if self.rect.top < 0:
            self.rect.top = 0

    def move_down(self):
        self.rect.y += PADDLE_SPEED
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def draw(self):
        pygame.draw.rect(WIN, WHITE, self.rect)


class Ball:
    def __init__(self):
        self.rect = pygame.Rect(
            WIDTH // 2 - BALL_RADIUS // 2,
            HEIGHT // 2 - BALL_RADIUS // 2,
            BALL_RADIUS,
            BALL_RADIUS,
        )
        # random vitesse
        self.speed_x = BALL_SPEED * random.choice((1, -1))
        self.speed_y = BALL_SPEED * random.choice((1, -1))

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y *= -1

    def display_speed(self):
        font = pygame.font.SysFont(None, 20)
        speed_text = font.render(f"Speed : {abs(self.speed_x)}", True, WHITE)
        WIN.blit(speed_text, (WIDTH // 2 - speed_text.get_width() // 2, 40))

    def draw(self):
        pygame.draw.ellipse(WIN, PINK, self.rect)


def save_score(score):
    with open("best_score.txt", "w") as file:
        file.write(str(score))


def best_score():
    with open("best_score.txt", "r") as file:
        return int(file.read())


def display_score():
    font = pygame.font.SysFont(None, 30)
    score_text = font.render(
        f"Score Max : {best_score()} || Score: {score}", True, WHITE
    )
    WIN.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 10))


def play_button():
    WIN.fill(RED)
    font = pygame.font.SysFont(None, 48)
    text = font.render("Play", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    margin = 20
    button_rect = text_rect.inflate(margin * 2, margin * 2)
    pygame.draw.rect(WIN, WHITE, button_rect, 2)
    WIN.blit(text, text_rect)
    return text_rect


player_paddle = Paddle(10)
computer_paddle = Paddle(WIDTH - PADDLE_WIDTH - 10)
ball = Ball()


def main():
    global score
    global game_active
    global ball_speed

    clock = pygame.time.Clock()
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if not game_active:
            play_button_rect = play_button()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_button_rect.collidepoint(mouse_pos):
                    game_active = True
            pygame.display.update()
        else:
            WIN.fill(BLACK)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                player_paddle.move_up()
            if keys[pygame.K_DOWN]:
                player_paddle.move_down()

            if ball.rect.y < computer_paddle.rect.y + PADDLE_HEIGHT // 2:
                computer_paddle.move_up()
            if ball.rect.y > computer_paddle.rect.y + PADDLE_HEIGHT // 2:
                computer_paddle.move_down()

            # collision

            if ball.rect.colliderect(player_paddle.rect) or ball.rect.colliderect(
                computer_paddle.rect
            ):
                ball.speed_x *= -1

            if ball.rect.colliderect(player_paddle.rect):
                ball.speed_x *= COEF_SPEED
                ball.speed_y *= COEF_SPEED
                score += 1

            if ball.rect.left <= 0 or ball.rect.right >= WIDTH:
                if score > best_score():
                    save_score(score)

                ball.__init__()
                score = 0
                game_active = False

            ball.draw()
            ball.move()
            player_paddle.draw()
            computer_paddle.draw()
            display_score()
            ball.display_speed()

            clock.tick(30)
            pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
