# Failed to execute, maybe tesseract's question
from PIL import Image
import subprocess


def cleanFile(filePath, newFilePath):
    image = Image.open(filePath)

    # Set a threshold value for the image, and save
    image = image.point(lambda x: 0 if x < 143 else 255)
    image.save(newFilePath)

    # call tesseract to do OCR on the newly created image
    subprocess.call(["D:\\Tesseract-OCR\\tesseract", newFilePath, "output"])

    # Open and read the resulting data file
    outputFile = open("output.txt", 'r')
    print(outputFile.read())
    outputFile.close()


cleanFile("test.png", "text_2_clean.png")