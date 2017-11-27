from PIL import Image, ImageFilter

test = Image.open('test.jpg')
blurryTest = test.filter(ImageFilter.GaussianBlur)
blurryTest.save('test_blurred.jpg')
blurryTest.show()
