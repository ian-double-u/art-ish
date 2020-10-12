# Sierpiński Carpet 

import numpy as np
from PIL import Image
import imageio

w, h = 729, 729 # easy powers of three
carpet_color = [157, 130, 232] # default-grey = [235, 238, 242]
carpet = np.asarray([[carpet_color for i in range(w)] for j in range(h)], dtype=np.uint8)  
carpet_files = []

image_initial = Image.fromarray(carpet, 'RGB')
image_name = 'sierpinski_carpet_0.png'
image_initial.save(image_name)
carpet_files.append(image_name)

# < - - - 
m = 5 # how many iterations of the Sierpiński Carpet
# < - - - 

for n in range(1,m+1): # perform iterations of the Sierpiński Carpet
    holes = 9**(n-1) # number of holes for this iteration    
    sqr_holes = int(holes**0.5) # number of holes per row/col for this iteration

    for j in range(1,sqr_holes+1):
        for k in range(1,sqr_holes+1):
            j_1 = int(h*((1 + (3*(j-1)))/(3**n)))
            j_2 = int(h*((2 + (3*(j-1)))/(3**n)))
            k_1 = int(w*((1 + (3*(k-1)))/(3**n)))
            k_2 = int(w*((2 + (3*(k-1)))/(3**n)))

            carpet[j_1:j_2, k_1:k_2] = [255,255,255] # [0,0,0]
      
    image_iteration = Image.fromarray(carpet, 'RGB')
    image_name = f'sierpinski_carpet_{n}.png'
    image_iteration.save(image_name)
    carpet_files.append(image_name)
    
images = []
for filename in carpet_files:
    images.append(imageio.imread(filename))
imageio.mimsave('sierpinski_carpet.gif', images, duration=0.35)
