from PIL import Image, ImageTk
import cv2


def fit(img, maxwidth, maxheight):
    height, width, channels = img.shape
    ratio = min(maxwidth / width, maxheight / height)
    thumbnail = cv2.resize(img, (int(width * ratio), int(height * ratio)))
    return thumbnail
