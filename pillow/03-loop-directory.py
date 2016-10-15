# https://www.youtube.com/watch?v=6Qs3wObeWwc&index=7&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU


from PIL import Image
import os


# print the names of each file in the directory
for f in os.listdir('.'):
    if f.endswith('.png'):
        i = Image.open(f)
        # need to split the name from the extension to keep there names
        fn, fext = os.path.splitext(f)
        # print fn
        # print fext
        i.save('jpgs/{}.jpg'.format(fn))


# This gives you an image object you can work with.
image1 = Image.open('juice.png')
