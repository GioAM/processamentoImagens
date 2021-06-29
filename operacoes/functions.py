
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

