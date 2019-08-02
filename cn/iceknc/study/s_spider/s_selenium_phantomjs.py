# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/7/31
# @Desc  : 
"""
Selenium
    Selenium是一个Web的自动化测试工具，最初是为网站自动化测试而开发的，类型像我们玩游戏用的按键精灵，可以按指定的命令自动操作，
    不同是Selenium 可以直接运行在浏览器上，它支持所有主流的浏览器（包括PhantomJS这些无界面的浏览器）。
    Selenium 可以根据我们的指令，让浏览器自动加载页面，获取需要的数据，甚至页面截屏，或者判断网站上某些动作是否发生。
    Selenium 自己不带浏览器，不支持浏览器的功能，它需要与第三方浏览器结合在一起才能使用。但是我们有时候需要让它内嵌在代码中运行，
    所以我们可以用一个叫 PhantomJS 的工具代替真实的浏览器。

PhantomJS
    PhantomJS 是一个基于Webkit的“无界面”(headless)浏览器，它会把网站加载到内存并执行页面上的 JavaScript，因为不会展示图形界面，
    所以运行起来比完整的浏览器要高效。
    如果我们把 Selenium 和 PhantomJS 结合在一起，就可以运行一个非常强大的网络爬虫了，这个爬虫可以处理 JavaScrip、Cookie、headers，
    以及任何我们真实用户需要做的事情。
        PhantomJS 是一个功能完善(虽然无界面)的浏览器而非一个 Python 库，所以它不需要像 Python 的其他库一样安装，
        但我们可以通过Selenium调用PhantomJS来直接使用。
        在Ubuntu16.04中可以使用命令安装：sudo apt-get install phantomjs
        如果其他系统无法安装，可以从它的官方网站http://phantomjs.org/download.html) 下载。

定位UI元素 (WebElements)
    find_element_by_id
        <div id="coolestWidgetEvah">...</div>
            element = driver.find_element_by_id("coolestWidgetEvah")
            ------------------------ or -------------------------
            from selenium.webdriver.common.by import By
            element = driver.find_element(by=By.ID, value="coolestWidgetEvah")

    find_elements_by_name
        <input name="cheese" type="text"/>
            cheese = driver.find_element_by_name("cheese")
            ------------------------ or -------------------------
            from selenium.webdriver.common.by import By
            cheese = driver.find_element(By.NAME, "cheese")

    find_elements_by_xpath
        <input type="text" name="example" />
        <INPUT type="text" name="other" />
            inputs = driver.find_elements_by_xpath("//input")
            ------------------------ or -------------------------
            from selenium.webdriver.common.by import By
            inputs = driver.find_elements(By.XPATH, "//input")

    find_elements_by_link_text
        <a href="http://www.google.com/search?q=cheese">cheese</a>
            cheese = driver.find_element_by_link_text("cheese")
            ------------------------ or -------------------------
            from selenium.webdriver.common.by import By
            cheese = driver.find_element(By.LINK_TEXT, "cheese")

    find_elements_by_partial_link_text
        <a href="http://www.google.com/search?q=cheese">search for cheese</a>>
            cheese = driver.find_element_by_partial_link_text("cheese")
            ------------------------ or -------------------------
            from selenium.webdriver.common.by import By
            cheese = driver.find_element(By.PARTIAL_LINK_TEXT, "cheese")

    find_elements_by_tag_name
        <iframe src="..."></iframe>
            frame = driver.find_element_by_tag_name("iframe")
            ------------------------ or -------------------------
            from selenium.webdriver.common.by import By
            frame = driver.find_element(By.TAG_NAME, "iframe")

    find_elements_by_class_name
        <div class="cheese"><span>Cheddar</span></div><div class="cheese"><span>Gouda</span></div>
            cheeses = driver.find_elements_by_class_name("cheese")
            ------------------------ or -------------------------
            from selenium.webdriver.common.by import By
            cheeses = driver.find_elements(By.CLASS_NAME, "cheese")

    find_elements_by_css_selector
        <div id="food"><span class="dairy">milk</span><span class="dairy aged">cheese</span></div>
            cheese = driver.find_element_by_css_selector("#food span.dairy.aged")
            ------------------------ or -------------------------
            from selenium.webdriver.common.by import By
            cheese = driver.find_element(By.CSS_SELECTOR, "#food span.dairy.aged")

弹窗处理
    当你触发了某个事件之后，页面出现了弹窗提示，处理这个提示或者获取提示信息方法如下：
    alert = driver.switch_to_alert()

页面切换
    一个浏览器肯定会有很多窗口，所以我们肯定要有方法来实现窗口的切换。切换窗口的方法如下：
        driver.switch_to.window("this is window name")
    也可以使用 window_handles 方法来获取每个窗口的操作对象。例如：
        for handle in driver.window_handles:
            driver.switch_to_window(handle)
页面前进和后退

操作页面的前进和后退功能：
    driver.forward()     #前进
    driver.back()        # 后退

Cookies
    获取页面每个Cookies值，用法如下
    for cookie in driver.get_cookies():
        print "%s -> %s" % (cookie['name'], cookie['value'])
    删除Cookies，用法如下
        # By name
        driver.delete_cookie("CookieName")

        # all
        driver.delete_all_cookies()

页面等待
    现在的网页越来越多采用了 Ajax 技术，这样程序便不能确定何时某个元素完全加载出来了。如果实际页面等待时间过长导致某个dom元素还没出来，
    但是你的代码直接使用了这个WebElement，那么就会抛出NullPointer的异常。
    为了避免这种元素定位困难而且会提高产生 ElementNotVisibleException 的概率。所以 Selenium 提供了两种等待方式，
    一种是隐式等待，一种是显式等待。

    显式等待
        显式等待指定某个条件，然后设置最长等待时间。如果在这个时间还没有找到元素，那么便会抛出异常了。
        下面是一些内置的等待条件，你可以直接调用这些条件，而不用自己写某些等待条件了。
            title_is
            title_contains
            presence_of_element_located
            visibility_of_element_located
            visibility_of
            presence_of_all_elements_located
            text_to_be_present_in_element
            text_to_be_present_in_element_value
            frame_to_be_available_and_switch_to_it
            invisibility_of_element_located
            element_to_be_clickable – it is Displayed and Enabled.
            staleness_of
            element_to_be_selected
            element_located_to_be_selected
            element_selection_state_to_be
            element_located_selection_state_to_be
            alert_is_present

    隐式等待
        等待特定的时间，显式等待是指定某一条件直到这个条件成立时继续执行。如果不设置，默认等待时间为0。
            driver.implicitly_wait(10) # seconds
"""

# 导入 webdriver
from selenium import webdriver

# 调用键盘按键操作时需要引入的Keys包
from selenium.webdriver.common.keys import Keys

# 导入 ActionChains 类 移动鼠标要用
from selenium.webdriver import ActionChains

# 导入 Select 类  表单操作
from selenium.webdriver.support.ui import Select

# WebDriverWait 库，负责循环等待
from selenium.webdriver.support.ui import WebDriverWait

# expected_conditions 类，负责条件出发
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

import time


def base():
    # 调用环境变量指定的PhantomJS浏览器创建浏览器对象
    driver = webdriver.PhantomJS()
    # 如果没有在环境变量指定PhantomJS位置
    # driver = webdriver.PhantomJS(executable_path="./phantomjs"))

    # get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)
    driver.get("http://www.baidu.com/")

    # 获取页面名为 wrapper的id标签的文本内容
    print(driver.find_element_by_id("wrapper").text)
    print("^" * 30)

    # 打印页面标题
    print(driver.title)
    print("^" * 30)

    # 生成当前页面快照并保存
    # driver.set_window_size(1920, 1080)
    # driver.save_screenshot("baidu.png")

    # id="kw"是百度搜索输入框，输入字符串"长城"
    driver.find_element_by_id("kw").send_keys(u"长城")

    # id="su"是百度搜索按钮，click() 是模拟点击
    driver.find_element_by_id("su").click()

    # 获取新的页面快照
    # driver.set_window_size(1920, 1080)
    # driver.save_screenshot("长城.png")

    # ctrl+a 全选输入框内容
    driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')

    # ctrl+x 剪切输入框内容
    driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')

    # 输入框重新输入内容
    driver.find_element_by_id("kw").send_keys("美女")

    # 模拟Enter回车键
    driver.find_element_by_id("kw").send_keys(Keys.ENTER)

    # 获取新的页面快照
    # driver.set_window_size(1920, 1080)
    # driver.save_screenshot("美女.png")

    # 清除输入框内容
    driver.find_element_by_id("kw").clear()

    # 获取当前url
    print(driver.current_url)
    print("^" * 30)

    # 打印网页渲染后的源代码
    print(driver.page_source)
    print("^" * 30)

    # 获取当前页面Cookie
    print(driver.get_cookies())
    print("^" * 30)

    # 关闭当前页面，如果只有一个页面，会关闭浏览器
    # driver.close()

    # 关闭浏览器
    driver.quit()


def action():
    driver = webdriver.PhantomJS()
    driver.get("http://www.baidu.com/")

    # 鼠标移动到 element 位置
    element = driver.find_element_by_id("kw")
    ActionChains(driver).move_to_element(element).perform()

    # 在 element 位置单击
    ActionChains(driver).move_to_element(element).click(element).perform()

    # 在 element 位置单击hold住
    ActionChains(driver).move_to_element(element).click_and_hold(element).perform()

    # 在 element 位置双击
    ActionChains(driver).move_to_element(element).double_click(element).perform()

    # 在 element 位置右击
    ActionChains(driver).move_to_element(element).context_click(element).perform()

    # 将 ac1 拖拽到 ac2 位置
    # ac1 = driver.find_element_by_xpath('elementD')
    # ac2 = driver.find_element_by_xpath('elementE')
    # ActionChains(driver).drag_and_drop(ac1, ac2).perform()

    # 获取新的页面快照
    # driver.set_window_size(1920, 1080)
    # driver.save_screenshot("action.png")

    driver.quit()


def form():
    driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
    driver.get("E:\Python\workspace\study\cn\iceknc\study\s_spider\select.html")

    form = driver.find_element_by_id("status")
    select = Select(form)
    select.select_by_index(1)

    time.sleep(3)
    driver.quit()

def wait():
    driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
    driver.get("http://www.baidu.com/")

    driver.find_element_by_id("kw").send_keys(u"美女")
    driver.find_element_by_id("su").click()

    try:
        # 页面一直循环，直到 id="myDynamicElement" 出现
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "container"))
        )

        # driver.set_window_size(1920, 1080)
        # driver.save_screenshot("美女.png")
    finally:
        driver.quit()

if __name__ == "__main__":
    wait()
