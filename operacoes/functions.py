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

