import requests
from PIL import Image, ImageTk
from io import BytesIO

def convert(link):
    response = requests.get(link)
    img = Image.open(BytesIO(response.content))

    resize_img = img.resize((300, 200))
    image = ImageTk.PhotoImage(resize_img)
    return image