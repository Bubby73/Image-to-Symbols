import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button as btn
import glob

# img = image in the same directory of any name, jpg or png

# Get a list of image files in the current directory
image_files = glob.glob("*.jpg") + glob.glob("*.png")

# Select the first available image, if any
if image_files:
    img = plt.imread(image_files[0])  # Read image as an array



ascii = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']
scale = 1

def image_compress(img, x, y): # compress the image
    global img_comp
    img = img[::x, ::y] 
    print(x, y)
    return img
    
def convert_to_ascii(event):
    gray = np.dot(image_compress(img, scale * 2, scale)[...,:3], [0.2989, 0.5870, 0.1140])
    temp_list = []
    for i in range(len(gray)):
        for j in range(len(gray[i])):
            temp_list.append(ascii[int(np.round((gray[i][j] * (9 / np.max(gray))), 0))])
        print(''.join(temp_list))
        #print(int(np.round((gray[i][j]))))
        temp_list = []

# show the image
plt.imshow(img)
plt.axis('off')

# Button to generate picture
gen_button = plt.axes([0.8, 0.025, 0.12, 0.06])
button = btn(gen_button, 'Generate', color='tomato', hovercolor='lightgreen')
button.on_clicked(convert_to_ascii)

# plus minus buttons to change scale
plus_button = plt.axes([0.1, 0.025, 0.05, 0.04])
minus_button = plt.axes([0.15, 0.025, 0.05, 0.04])

def plus(event):
    global scale
    if scale > 1:
        scale -= 1
    print("Scale:", scale)

def minus(event):
    global scale
    scale += 1
    print("Scale:", scale)


plus_btn = btn(plus_button, '+', color='tomato', hovercolor='lightgreen')
plus_btn.on_clicked(plus)

minus_btn = btn(minus_button, '-', color='tomato', hovercolor='lightgreen')
minus_btn.on_clicked(minus)


def inverse(event):
    global ascii
    ascii = ascii[::-1]
    #c change button colour
    if inverse_button.color == 'violet':
        inverse_button.color = 'skyblue'
    else:
        inverse_button.color = 'violet'

# inverse button
inv_btn = plt.axes([0.2, 0.025, 0.1, 0.04])
inverse_button = btn(inv_btn, 'Inverse', color='skyblue', hovercolor='lightgreen')
inverse_button.on_clicked(inverse)


plt.show()


