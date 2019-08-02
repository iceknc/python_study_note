# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/8/1
# @Desc  :

from selenium import webdriver
import time
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class DouYuSpider():
    def __init__(self):
        self.start_url = "https://www.douyu.com/directory/all"
        self.driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver")

    def run(self):
        self.driver.fullscreen_window()
        self.driver.get(self.start_url)

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "layout-Cover-list"))
            )
        except Exception:
            print("error")

        content_list, next_url = self.get_content_list()
        self.save_content_list(content_list)
        # 5.点击下一页元素，循环
        while next_url is not None:
            next_url.click()
            time.sleep(5)
            content_list, next_url = self.get_content_list()
            self.save_content_list(content_list)

    def save_content_list(self, content_list):
        with open("douyu.json", "a+", encoding='utf-8') as f:
            f.write(str(content_list))
            f.write("\n")

    def get_content_list(self):
        time.sleep(4)
        ul_list = self.driver.find_elements_by_xpath("//ul[@class='layout-Cover-list']")
        print(len(ul_list))

        for i in range(8):
            js = 'var action=document.documentElement.scrollTop=' + str(i * 1000)
            self.driver.execute_script(js)
            time.sleep(1)


        li_list = ul_list[1].find_elements_by_xpath("./li")
        content_list = []
        print(len(li_list))
        for li in li_list:
            item = {}
            item["room_img"] = li.find_element_by_xpath(".//div[@class='DyListCover-imgWrap']//img").get_attribute("src")
            item["room_title"] = li.find_element_by_xpath(".//h3[@class='DyListCover-intro']").text
            item["room_cate"] = li.find_element_by_xpath(".//span[@class='DyListCover-zone']").text
            item["anchor_name"] = li.find_element_by_xpath(".//h2[@class='DyListCover-user']").text
            item["watch_num"] = li.find_element_by_xpath(".//span[@class='DyListCover-hot']").text

            print(item)

            content_list.append(item)

        # 获取下一页的元素
        next_url = self.driver.find_element_by_xpath("//div[@class='ListFooter']/ul//li[last()]")
        disabled = next_url.get_attribute("aria-disabled")
        next_url = next_url if disabled == 'false' else None
        return content_list, next_url


def main():
    spider = DouYuSpider()
    spider.run()


if __name__ == "__main__":
    main()
