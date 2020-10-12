import numpy as np
from PIL import Image
import imageio
import random

def get_rand_color():
    g = lambda: int(random.uniform(0, 1)*255)
    return [g(),g(),g()]

grid_list = []

for i in range(1,10):
    w, h = 512, 512
    grid = np.asarray([[get_rand_color() for i in range(w)] for j in range(h)], dtype=np.uint8)  
    img = Image.fromarray(grid, 'RGB')
    name = f'fuzzy_grid{i}.png'
    img.save(name)
    grid_list.append(name)
    
images = [imageio.imread(filename) for filename in grid_list]
imageio.mimsave('fuzzy_gif.gif', images, duration=0.05)
