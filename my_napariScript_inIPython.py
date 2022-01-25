# exec(open('myScript.py').read()) #run in iPython console will execute the entire script using the current viewer

from skimage import data
from skimage.color import rgb2gray
from skimage import filters

viewer.add_image(data.immunohistochemistry(), rgb=True, blending='additive')
binary=rgb2gray(viewer.layers[0].data)>0.6
edge_sobel = filters.sobel(binary)
viewer.add_image(edge_sobel, blending='additive', colormap='yellow')
