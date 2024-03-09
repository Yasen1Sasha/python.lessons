# --------------------------------------------------- #
#   * * *   *   *  * * *      *     **    **  * * *   #
#   *   *    * *   *   *     * *    * *  * *  *       #
#   * * *    **    *         * *    *  *   *  * * *   #
#   *        *     *  **    * * *   *  *   *  *       #
#   *       *      * * *   *     *  *      *  * * *   #
# --------------------------------------------------- #

import pygame
import sys

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
# зАГОЛОВОК ВІКНА
pygame.display.set_caption("petyh")

#FPS
clock = pygame.time.Clock()
clock_tick = 60
spyder_image = pygame.image.load('images/spyder.png')

spyder_image_position = {'x':0, 'y': 0}
background_surface = pygame.Surface((screen_width, screen_height))
background_surface.fill("Black")

#===========================================================
while True:
    # Слідкуємо за подіями
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        spyder_image_position['y'] -= 50
    if keys[pygame.K_s]:
        spyder_image_position['y'] += 50
    if keys[pygame.K_a]:
        spyder_image_position['x'] -= 50
    if keys[pygame.K_d]:
        spyder_image_position['x'] += 50
    screen.blit(background_surface, (0, 0))




    screen.blit(spyder_image, (spyder_image_position['x'], spyder_image_position['y']))
   #screen
    pygame.display.update()

    clock.tick(clock_tick)