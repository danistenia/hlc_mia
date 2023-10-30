from sklearn import datasets
import cv2 as cv
import numpy as np

# Pregunta 1
data = datasets.load_sample_images()
china, flower = data.images

class Convolution:

    def __init__(self, img):
        self.img = img

    def show_img(self):
        cv.imshow('', self.img)
        cv.waitKey(0)

    def show_dimensions(self):
        print(self.img.shape)
    
    def img_matrix(self):
        img_array = np.array(self.img)
        print(f'--- Shape of image {img_array.shape} ----')
        print(img_array[0].shape)
        #print(img_array)



if __name__ == '__main__':

    # Pregunta 2 - China
    conv = Convolution(img=china)
    conv.show_dimensions()
    
    # Pregunta 2 - Flowers
    conv = Convolution(img=flower)
    conv.show_dimensions()