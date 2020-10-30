import pygame
import os
from fastbitmapfont import FastBitmapFont, FontParams

size = (640, 480)

pygame.init()

screen = pygame.display.set_mode(size)

# directory, bitmapfilename, width / char(px), height / char(px), xofs, yofs, char/line(in bitmap), char offs(starting char)
font = FontParams('data', 'defaultfont1.bmp', 8, 16, 0, 0, 16, 0x20)

# make new bitmapfont object
ff = FastBitmapFont(font)

#load the font file, everytime you change the font need to call
ff.load_font()


# load background image to demonstrate transparency
background = pygame.image.load(os.path.join('data', 'background.jpg')).convert()
background = pygame.transform.smoothscale(background, screen.get_size())

clock = pygame.time.Clock()

lines = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit,',
         'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
         'Ut enim ad minim veniam, quis nostrud exercitation ullamco',
         'laboris nisi ut aliquip ex ea commodo consequat.',
         'Duis aute irure dolor in reprehenderit in voluptate velit',
         'esse cillum dolore eu fugiat nulla pariatur.',
         'Excepteur sint occaecat cupidatat non proident,',
         'sunt in culpa qui officia deserunt mollit anim id est laborum.')

hellostr = "Hello world with bitmaps!"
ffsize = ff.get_size(hellostr)
ffsurface = pygame.Surface((ffsize[0], ffsize[1]), pygame.SRCALPHA)
#ffsurface.fill(pygame.Color('black'))
ff.render_to(ffsurface, (0, 0), hellostr)
ffsurface = pygame.transform.smoothscale(ffsurface, (ffsize[0] * 2, ffsize[1] * 2))
#ffsurface.set_colorkey(ffsurface.get_at((0, 0)))

k = 0
d = 1
line_space = 2
done = False
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # blit background image to screen
    screen.blit(background, (0, 0))

    q = k
    for i in lines:
        # render 1 line at time in uppercase
        ff.render_to(screen, (10, q), i.upper())
        # increment line position with text height + additional line space
        q += ff.fontparams.height + line_space
    k = k + d
    if 0 > k:
        d *= -1
    elif k > 300:
        d *= -1

    screen.blit(ffsurface, (0, 0))

    # lock pygame framerate to 60 fps
    clock.tick(30)
    pygame.display.flip()

pygame.quit()
