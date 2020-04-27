from PIL import Image, ImageTk
import cv2


def fit(img, maxwidth, maxheight):
    height, width, channels = img.shape
    ratio = min(maxwidth / width, maxheight / height)
    thumbnail = cv2.resize(img, (int(width * ratio), int(height * ratio)))
    return thumbnail


def fit_tk(img, maxwidth, maxheight):
    height, width, channels = img.shape
    ratio = min(maxwidth / width, maxheight / height)
    thumbnail = cv2.resize(img, (int(width * ratio), int(height * ratio)))
    im = Image.fromarray(thumbnail)
    imgtk = ImageTk.PhotoImage(image=im)
    return imgtk


def array_to_tk(array):
    image = cv2.cvtColor(array, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(image)
    imgtk = ImageTk.PhotoImage(image=im)
    return imgtk
