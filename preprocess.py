import os
import re
from PIL import Image

# to start with all I really want to do 
# is just convert everything to grey scale
sprite_dir = "./original_sprites/"
out_dir = "./processed_sprites/"
for fn in os.listdir(sprite_dir):
    if (re.search("\.png",fn)):
        infile = sprite_dir+fn
        outfile = out_dir+fn
        Image.open(infile).convert('L').save(outfile)
