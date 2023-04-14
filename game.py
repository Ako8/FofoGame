import pygame
import sys

pygame.init()


def animation():
    global kata_index, kata_surf
    if kata_rect.bottom < 300:
        kata_surf = kata_walk[0]
    else:
        kata_index += 0.1
        if kata_index >= len(kata_walk):
            kata_index = 0
        kata_surf = kata_walk[int(kata_index)]


def menu():
    screen.blit(startbutt_scl, startbutt_rect)
    bestscr = text_1.render(f"Best score: {bestscore}", False, 'black').convert_alpha()
    bestscr_rect = bestscr.get_rect(center=(200, 150-30))
    screen.blit(bestscr, bestscr_rect)
    score = text_1.render(f"Score: {i}", False, 'black').convert_alpha()
    score_rect = score.get_rect(center=(200, 100-30))
    screen.blit(score, score_rect)


def draw_scores():
    global a, i
    # score
    if a == 60:
        i += 1
        a = 0
    score = text.render(f"{i}", False, 'black').convert_alpha()
    score_rect = score.get_rect(topleft=(10, 10))
    screen.blit(score, score_rect)


def draw_kata():
    global gravity
    keys = pygame.key.get_pressed()
    if kata_rect.left >= 0:
        if keys[pygame.K_LEFT]:
            kata_rect.x -= 4
    if kata_rect.right <= 700:
        if keys[pygame.K_RIGHT]:
            kata_rect.x += 4
    gravity += 1
    kata_rect.y += gravity
    if kata_rect.bottom > 350:
        kata_rect.bottom = 350
    animation()
    screen.blit(kata_surf, kata_rect)


def gameover():
    global x, x1, bestscore, game
    if kata_rect.colliderect(fofo_rect) or kata_rect.colliderect(fofo_rect1):
        kata_rect.x = 100
        fofo_rect.x = 800
        fofo_rect1.x = 800+360
        x = 0
        x1 = 1600
        if i > bestscore:
            bestscore = i
        game = False


screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
pygame.display.set_caption('Phopho')
FPS = 60
room = pygame.image.load('room.jpg').convert_alpha()
room_scl = pygame.transform.scale(room, (1600, 400))
x = 0
x1 = 800
fofo = pygame.image.load('phopho.png').convert_alpha()
fofo_scl = pygame.transform.scale(fofo, (70, 70))
fofo_rect = fofo_scl.get_rect(bottomright=(800, 350))
fofo_rect1 = fofo_scl.get_rect(bottomright=(800+400, 350))

kata = pygame.image.load("kata_1.png").convert_alpha()
kata1 = pygame.image.load('kata_2.png').convert_alpha()
kata_scaled = pygame.transform.scale(kata, (117 * 1.2, 75 * 1.2))
kata1_scaled = pygame.transform.scale(kata1, (117 * 1.2, 75 * 1.2))
kata_walk = [kata_scaled, kata1_scaled]
kata_index = 0
kata_surf = kata_walk[kata_index]
kata_rect = kata_surf.get_rect(midbottom=(100, 350))
gravity = 0
game = False
startbutt = pygame.image.load('start_button.png').convert_alpha()
startbutt_scl = pygame.transform.scale(startbutt, (200, 200))
startbutt_rect = startbutt_scl.get_rect(center=(600, 200 / 2))
text = pygame.font.Font(None, 30)
text_1 = pygame.font.Font(None, 70)
i = 0
a = 0
bestscore = 0


while True:
    screen.blit(room_scl, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and kata_rect.bottom >= 300:
                gravity = -20
                # if not game:
                #     game = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0] and startbutt_rect.collidepoint(mx, my):
                i = 0
                game = True
    if game:
        a += 1
        if x1 == 0:
            x = 1600
        if x == 0:
            x1 = 1600
        screen.blit(room_scl, (x, 0))
        screen.blit(room_scl, (x1, 0))
        x -= 4
        x1 -= 4
        draw_scores()

        fofo_rect.x -= 4
        fofo_rect1.x -= 4
        if fofo_rect.right <= 0:
            fofo_rect.x = 800
        if fofo_rect1.right <= 0:
            fofo_rect1.x = 800
        screen.blit(fofo_scl, fofo_rect)
        screen.blit(fofo_scl, fofo_rect1)

        draw_kata()
        gameover()
    else:
        # screen.blit(room_scl, (0, 0))
        menu()
    clock.tick(FPS)
    pygame.display.update()