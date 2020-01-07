import io
import urllib
from os import PathLike
from PIL import Image


# 判断文件是否为有效（完整）的图片
# 从网络上判断图片是否损坏
def IsValidImage_remote_img(url):
    b_valid = True
    try:
        buf = urllib.request.urlopen(url).read()  # bytearray
        img_buffer = io.BytesIO(buf)  # 转换为字符串
        if not buf.startswith(b'\xff\xd8'):  # 是否以\xff\xd8开头
            b_valid = False
        elif buf[6:10] in (b'JFIF', b'Exif'):  # “JFIF”的ASCII码
            if not buf.rstrip(b'\0\r\n').endswith(b'\xff\xd9'):  # 是否以\xff\xd9结尾
                b_valid = False
        else:
            try:
                Image.open(img_buffer).verify()
            except Exception as e:
                b_valid = False
                print(e)
    except Exception as e:
        print(e)

    return b_valid


# 从本地判断图片是否损坏
def IsValidImage_native_img(file):
    try:
        b_valid = True
        if isinstance(file, (str, PathLike)):  # 文件路径
            fileObj = open(file, 'rb')  # 以二进制形式打开
        else:
            fileObj = file  # 文件对象
        buf = fileObj.read()
        if not buf.startswith(b'\xff\xd8'):  # 是否以\xff\xd8开头
            b_valid = False
        elif buf[6:10] in (b'JFIF', b'Exif'):  # “JFIF”的ASCII码
            if not buf.rstrip(b'\0\r\n').endswith(b'\xff\xd9'):  # 是否以\xff\xd9结尾
                b_valid = False
        else:
            try:
                Image.open(fileObj).verify()
            except Exception as e:
                b_valid = False
                print(e)
    except Exception as e:
        print(e)
    return b_valid


if __name__ == '__main__':
    print(IsValidImage_native_img('/Users/ltb/Desktop/微信图片/d277eb36d885a2ceab8d2d0e75bab556.jpg'))
    print(IsValidImage_native_img('/Users/ltb/Desktop/微信图片/WechatIMG3790.jpeg'))
