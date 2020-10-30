# bitmapfont
Minimal bitmap font class for pygame

load and display bitmap fonts on pygame surface
only single line strings, usage below and test_text.py file

Usage:
from fastbitmapfont import FontParams, FastBitmapFont

# data directory, fontfile name, char width in px, char height in px, horizontal offs (px), vertical offs(px), char per line in bitmap file, start offset of ascii
fonparams = FontParams('data', 'defaultfont1.bmp', 8, 16, 0, 0, 16, 0x20)
# initialize FastBitmapFont object
font = FastBitmapFont(fontparams)
# load the font file
font.LoadFont()

# blit string to your surface
font.renderto(my_surface, (x, y), 'My text')

# get target surface size for string
widt,height = font.get_size('My text')


