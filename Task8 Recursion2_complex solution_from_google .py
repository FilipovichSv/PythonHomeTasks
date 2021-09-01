import collections as col
import matplotlib.ticker as ticker
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
import collections as col
import random


def cutRect(p):
    rect = plt.Rectangle((p.x, p.y), p.l, p.h, linewidth=3, edgecolor='r', facecolor='g',
                         alpha=0.2)  # нижний левый край, длина, высота, цвет, насыщенность
    return rect


def createPach(rect, ax):
    global iteration
    # find tho longest side
    short = 0
    if (rect.l != 0 and rect.h != 0):
        if rect.h > rect.l:
            short = rect.l
            newRect = Rectangle(x=rect.x, y=rect.y + short, h=rect.h - short, l=rect.l)
        else:
            short = rect.h
            newRect = Rectangle(x=rect.x + short, y=rect.y, h=rect.h, l=rect.l - short)
        iteration += 1
        print("Итерация {} c длиной стороны квадрата {}".format(iteration, short))
        print(newRect)
        currSqr = Rectangle(x=rect.x, y=rect.y, h=short, l=short)
        ax.add_patch(cutRect(currSqr))
        createPach(newRect, ax)


# create orig rectangle
x = random.randint(5, 50)
y = random.randint(5, 50)
l = random.randint(5, 50)
h = random.randint(5, 50)
global iteration
iteration = 0

Rectangle = col.namedtuple('Rectangle', ['x', 'y', 'l', 'h'])
rect = Rectangle(x=x, y=y, h=h, l=l)
print(rect)

# im = np.array(Image.open('/home/katherine/Desktop/DeepinScreenshot_select-area_20200428142319.png'), dtype=np.uint8)
im = np.full((100, 100, 3), [255, 255, 255])
# im= np.flip(im, axis=0)

# Create figure and axes
fig, ax = plt.subplots(1)

# Display the image
ax.imshow(im)
ax.grid()

# Create a Rectangle patch
# Add the patch to the Axes
# rect = Rectangle(x=20, y=20, h=20, l=20)
ax.add_patch(cutRect(rect))
createPach(rect, ax)

#  Устанавливаем интервал основных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
#  Устанавливаем интервал вспомогательных делений:
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))

fig.set_figwidth(20)
fig.set_figheight(20)

plt.gca().invert_yaxis()

plt.show()