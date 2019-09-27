# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/9/12
# @Desc  : 
import win32ui
import win32con
import os


def main():
    for main_dir, sub_dir, sub_file in os.walk("C:\Windows\Fonts"):
        for sub in sub_file:
            print(sub)

if __name__ == "__main__":
    main()
