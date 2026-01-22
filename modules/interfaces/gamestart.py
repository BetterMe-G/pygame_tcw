
import sys
import pygame
from ..sprites import Player


'''游戏开始界面'''
def GameStartInterface(screen, sounds, cfg):
    player = Player(cfg.IMAGE_PATHS['player'])
    ground = pygame.image.load(cfg.IMAGE_PATHS['ground']).subsurface((0, 0), (83, 19))
    rect = ground.get_rect()
    rect.left, rect.bottom = cfg.SCREENSIZE[0]/20, cfg.SCREENSIZE[1]

    # 加载背景图片
    background = pygame.image.load(cfg.IMAGE_PATHS['background_start'])
    # 调整背景图片大小以适应屏幕
    background = pygame.transform.scale(background, cfg.SCREENSIZE)
    background_rect = background.get_rect()

    clock = pygame.time.Clock()
    press_flag = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    press_flag = True
                    player.jump(sounds)
        player.update()
        #screen.fill(cfg.BACKGROUND_COLOR)
        screen.blit(background, background_rect)
        screen.blit(ground, rect)
        player.draw(screen)
        pygame.display.update()
        clock.tick(cfg.FPS)
        if (not player.is_jumping) and press_flag:
            return True
