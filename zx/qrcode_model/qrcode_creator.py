__author__ = 'zx'
# coding£ºutf-8
from PIL import Image
import qrcode
import qrcode.image.svg
import os

qr = qrcode.QRCode(version=5, error_correction=qrcode.ERROR_CORRECT_M, box_size=5, border=1)
qr.add_data('http://192.168.1.110:8000/auth/')
qr.make(fit=True)

img = qr.make_image()
img = img.convert("RGBA")

if os.path.exists('E:/untitled1') and os.path.isfile('E:/untitled1/alipay.png'):
    print('write path')
else:
    print('wrong path')


logo = 'E:/untitled1/alipay.png';
icon = Image.open(logo)
# print(icon)
img_w, img_h = img.size
factor = 5
size_w = int(img_w / factor)
size_h = int(img_h / factor)

icon_w, icon_h = icon.size
if icon_w > size_w:
    icon_w = size_w
if icon_h > size_h:
    icon_h = size_h
icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
w = int((img_w - icon_w) / 2)
h = int((img_h - icon_h) / 2)

icon = icon.convert("RGBA")
img.paste(icon, (w, h), icon)

img.save('1.jpg')