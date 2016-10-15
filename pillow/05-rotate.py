# https://www.youtube.com/watch?v=6Qs3wObeWwc&index=7&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU


from PIL import Image
import os

image1 = Image.open('juice.png')

image1.rotate(90).save('juicerotate.jpg')