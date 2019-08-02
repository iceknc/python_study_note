# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/8/1
# @Desc  : 

import pytesseract
from PIL import Image


def main():
    image = Image.open("./u_tess1.png")
    string = pytesseract.image_to_string(image)
    print(string)

    image = Image.open("./u_tess2.png")
    string = pytesseract.image_to_string(image)
    print(string)


def clean_image(source_path, target_path):
    source = Image.open(source_path)

    # 对图片进行阈值过滤（低于143的置为黑色，否则为白色）
    image = source.point(lambda x: 0 if x < 143 else 255)
    # 重新保存图片
    image.save(target_path)


if __name__ == "__main__":
    main()
    clean_image("./u_tess2.png", "./u_tess2_clean.png")
