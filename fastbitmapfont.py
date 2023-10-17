import pygame
import os


class FontParams:
    directory = ''
    fontname = ''
    width = 8
    height = 16
    horizontal_offs = 0
    vertical_offs = 0
    char_per_line = 16
    char_start_offset = 0x20

    def __init__(self, dir, fontname, width, height, horizoffs, vertoffs, charpline, charoffs):
        self.directory = dir
        self.fontname = fontname
        self.width = width
        self.height = height
        self.horizontal_offs = horizoffs
        self.vertical_offs = vertoffs
        self.char_per_line = charpline
        self.char_start_offset = charoffs
        pass


class FastBitmapFont:
    bitfont = pygame.Surface((0, 0))
    fontparams = ()

    def __init__(self, fontparams):
        self.fontparams = fontparams

    def load_font(self):
        filename = os.path.join(self.fontparams.directory, self.fontparams.fontname)
        self.bitfont = pygame.image.load(filename).convert_alpha()

    def get_size(self, text):
        text = text.replace('\n', '')
        return self.fontparams.width * len(text), self.fontparams.height

    def render_to(self, surface, point, text):
        text = text.replace('\n', '')
        srcrect = pygame.Rect(0, 0, 0, 0)
        x0, y0 = point
        srcrect.w = self.fontparams.width
        srcrect.h = self.fontparams.height
        char = pygame.Surface(srcrect.size, pygame.SRCALPHA)
        trans_color = self.bitfont.get_at((0, 0))
        for i in text:
            q = ord(i) - self.fontparams.char_start_offset
            x = (q % self.fontparams.char_per_line) * self.fontparams.width
            y = int(q / self.fontparams.char_per_line) * self.fontparams.height
            srcrect.x = x + self.fontparams.horizontal_offs
            srcrect.y = y + self.fontparams.vertical_offs
            char.fill(trans_color)
            char.blit(self.bitfont, (0, 0), srcrect)
            surface.blit(char, (x0, y0))
            x0 += self.fontparams.width
