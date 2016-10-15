


from PIL import Image


# This gives you an image object you can work with.
image1 = Image.open('juice.png')

# Open the image in preview
image1.show()


# Save in new format
image1.save('juice.jpg')
