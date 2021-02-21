# web端自动化测试 webdriver
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')

time.sleep(5)



#
# driver = webdriver.Chrome()
# webdriver.Chrome().get('http://101.133.169.100/yuns/index.php/goods/4.html')


# # 直接定位到url浏览地址指定网页
# driver=webdriver.Chrome()
# driver.get('http://101.133.169.100/yuns/index.php/goods/4.html')
# time.sleep(5)


driver.find_element_by_xpath("//input[@class='but1']").send_keys('女装')
driver.find_element_by_xpath('//div[@class="schbox"]/form/input[2]').click()
driver.find_element_by_xpath('/html/body/div[4]/div/div[4]/div[2]/div[1]/div[1]/a/img').click()
time.sleep(2)
url=driver.current_url
print(url)
# driver.get('http://101.133.169.100/yuns/index.php/goods?key=%E5%A5%B3%E8%A3%85')
# driver.find_element_by_xpath('/html/body/div[4]/div/div[4]/div[1]/a[5]').click()
# time.sleep(2)
# driver.back()



# from selenium.webdriver.common.keys import Keys
# driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/a[1]').send_keys(Keys.CONTROL,'a')
# driver.quit(5)





# driver=webdriver.Chrome()
# driver.get('http://101.133.169.100/yuns/index.php/goods/seckill.html')
# time.sleep(5)
# driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/a[4]').click()
# driver.quit()

# 定位标题栏中head部分，
# title=driver.title
# print(title)
# # 定位head中url地址栏
# url=driver.current_url
# print(url)
# time.sleep(5)



# driver.find_element_by_name("key").send_keys("乔丹") .seng_keys("乔丹")输入乔丹
# driver.quit()

# driver.find_element_by_id('首页')
# ele_01=driver.find_element_by_name('key').send_keys('女装')
# driver.quit()





# xpath相对路径有@有and
# driver.find_element_by_xpath("//div[@class='schbox']/form/input").send_keys('女装')
# # 直接定位?
# driver.find_element_by_xpath('//input[@class="but2"]').click()
# time.sleep(2)

# 绝对路径用左斜杠表示
# driver.find_element_by_xpath(" /html/body/div[2]/div/div[2]/div[1]/form/input[1]").send_keys('nishi')
# /html/body/div[2]/div/div[2]/div[1]/form/input[1]


# 文本框
# driver.find_element_by_partial_link_text("夏天").click()


# 联系xpath定位控件
# 绝对路径
# driver.find_elemennt_by_xpath('html/body/div/div/div/div/a.header').click()
# driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/a[2]').click()
# 相对路径
# driver.find_element_by_xpath('//div[@class="nav_bar"]/div/div[2]/a[2]').click()
# driver.find_element_by_xpath('//div[@class="nav_bar"]/div/div[@class="nav_pub"]/a[2]').click()
# driver.find_element_by_xpath('//div[@class="nav_pub"]/a[2]').click()
# 直接定位
# driver.find_element_by_xpath('//input[@class="but2"]').click()

# 浏览器操作
# driver.find_element_by_link_text("口红").click()
# driver.refresh()
# time.sleep(2)
# driver.back()
# time.sleep(2)
# driver.forward()
# time.sleep(2)
# # driver.quit() 表示返回pycharm界面并停止后续动作

# 设置窗口大小
# driver.maximize_window()展示全屏
# time.sleep(2)
# 设置你想要的窗口大小
# driver.set_window_size(200,300)
# time.sleep(2)


# driver.maximize_window()
# time.sleep(2)
# driver.find_element_by_id('cart_num').click()

# 查找定义控件的宽度高度
# driver.find_element_by_xpath('//div[@class="schbox"]/form/input').send_keys('香水')
# driver.find_element_by_xpath('//div[@class="schbox"]/form/input').size
# heqing=driver.find_element_by_xpath('//div[@class="schbox"]/form/input').size
# 这里的heqing是定义的量，也可以选择size表示
# print(type(heqing))
# print(heqing['height'])
# print(heqing['width'])

# 获取定义控件的文本信息
# driver.find_element_by_link_text('联系客服')
# wenben=driver.find_element_by_link_text('联系客服').text
# print(wenben)


# driver.find_element_by_xpath('//a[@herf='http://101.133.169.100/yuns/index.php/news/help/id/4")
# # 若要获取定义控件的里面的某个属性，需要用.get_attribute('placeholder')
# # driver.find_element_by_link_text('夏天最热').get_attribute('target')


# driver.find_element_by_link_text('男装女装').click()


# 鼠标事件ActionChains
# from selenium.webdriver.common.action_chains import ActionChains
# import time
# ele=driver.find_element_by_link_text('家电数码')
# time.sleep(2)
# ActionChains(driver).move_to_element(ele).perform()
# time.sleep(2)
# driver.quit()

# 练习鼠标事件
# driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/dl[3]/dt/div/span/a').click()
# time.sleep(2)
# ele2=driver.find_element_by_xpath('//div[@class="allcats allcats_show"]/span/em')
# time.sleep(2)
# ActionChains(driver).move_to_element(ele2).perform()
# time.sleep(2)
# driver.quit()

# 鼠标事件右击
# ActionChains(driver).context_click(ele).perform()
# time.sleep(2)
# driver.quit()
# 鼠标事件双击double_click()
# ActionChains(driver).double_click(ele).perform()
# time.sleep(2)
# driver.quit()
