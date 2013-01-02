import os
import re
from PIL import Image
from numpy import *
from pylab import *

sprite_dir = "./processed_sprites/"
sprite_names = os.listdir(sprite_dir)
sprite_files = map(lambda x: sprite_dir+x,sprite_names)
m,n = array(Image.open(sprite_files[0])).shape
images = []
for sprite in sprite_files:
    i = array(Image.open(sprite)).flatten()
    if len(i) != m*n:
        print(sprite+" looks odd")
    else:
        images.append(i)

I = array(images)



if __name__ == "__main__":
    print('creating mean man')
    mean_image = Image.fromarray(reshape(I.mean(axis=0),[m,n]))
    mean_image.convert('L').save("./final/mean_man.png")
    print('now trying eigen man')
    U,S,V = linalg.svd(I)
    #maybe we'll find one that works?
    for i in xrange(0,4):
        image_scaled = (abs(V[i]/max(abs(V[i])))*255)
        new_image = Image.fromarray(reshape(image_scaled,[m,n]))
        new_image.convert('L').save('./final/eigen_'+str(i)+'.png')
        


    
