from django.shortcuts import resolve_url
import numpy as np

def negative(image):
    height, width, _ = image.shape

    for i in range(0, height - 1):
        for j in range(0, width - 1):
            pixel = image[i, j]
            pixel[0] = 255 - pixel[0]
            pixel[1] = 255 - pixel[1]
            pixel[2] = 255 - pixel[2]
            image[i, j] = pixel
    return image


def rgbtobit(image, limiar):
    height, width = image.shape
    for i in range(0, height):
        for j in range(0, width):
            pixel = image[i, j]
            if pixel <= limiar:
                pixel = 0
            else:
                pixel = 255
            image[i, j] = pixel
    return image


def f_and(image1, image2):
    height, width, _ = image1.shape
    new_image = image1
    for i in range(0, height):
        for j in range(0, width):
            pixel1 = image1[i, j]
            pixel2 = image2[i, j]
            pixel = pixel1[0] and pixel2[0]
            new_image[i, j] = pixel
    return new_image


def f_or(image1, image2):
    height, width, _ = image1.shape
    new_image = image1
    for i in range(0, height):
        for j in range(0, width):
            pixel1 = image1[i, j]
            pixel2 = image2[i, j]
            pixel = pixel1[0] or pixel2[0]
            new_image[i, j] = pixel
    return new_image


def f_xor(image1, image2):
    height, width, _ = image1.shape
    new_image = image1
    for i in range(0, height):
        for j in range(0, width):
            pixel1 = image1[i, j]
            pixel2 = image2[i, j]
            if pixel1[0] == pixel2[0]:
                pixel = 0
            else:
                pixel = 255
            new_image[i, j] = pixel
    return new_image


def f_not(image):
    height, width, _ = image.shape
    for i in range(0, height):
        for j in range(0, width):
            pixel1 = image[i, j]
            if pixel1[0] > 0:
                pixel = 0
            else:
                pixel = 255
            image[i, j] = pixel
    return image

def rgbtogray(image, luma=False):
    if luma:
        params = [0.299, 0.589, 0.114]
    else:
        params = [0.2125, 0.7154, 0.0721]    
    image = np.ceil(np.dot(image[...,:3], params))
 
    image[image > 255] = 255
    return image

def adicao(image1, image2):
    image1= np.int32(image1)

    image2= np.int32(image2)

    new_image = image1 + image2
    return new_image

def subtracao(image1, image2):
    image1 = np.int32(image1)

    image2 = np.int32(image2)

    new_image = image1 - image2
    return new_image

def blending(image):

    return image

def equalizacao(image1, z_max=255):

    height, witdth = image1.shape
    total = height * witdth  * 1.
 
    out = image1.copy()
 
    sum_h = 0.
 
    for i in range(1, 255):
    	ind = np.where(image1 == i)
    	sum_h += len(image1[ind])
    	z_prime = z_max / total * sum_h
    	out[ind] = z_prime
 
    out = out.astype(np.uint8)

    return out

def divisao(image, limiar):
    
    image = np.int32(image)

    image = image / limiar

    return image