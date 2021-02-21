from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')

time.sleep(5)
#
# # 键盘事件
# from selenium.webdriver.common.keys import Keys
# driver.find_element_by_xpath('//div[@class="schbox"]/form/input').send_keys('男装女装')
# time.sleep(2)
# driver.find_element_by_xpath('//div[@class="schbox"]/form/input').send_keys(Keys.BACKSPACE)
# time.sleep(2)


# 等待时间三种
# # 隐式等待
# driver.implicitly_wait(10)
# driver.find_element_by_xpath('//div[@class="schbox"]/form/input').send_keys('男装女装')

# 显示等待时间WebDriverWait
# # 第一步导入
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from  selenium.webdriver.support import expected_conditions as EC

# driver.find_element_by_xpath('div[@class="schbox"]//form/input')
# 最大等待时间是5秒。每隔0.5秒检测一次。直到定位当前的指定控件
# ele=WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,'//div[@class="schbox"]/form/input')))
# ele.send_keys('123456')
# time.sleep(2)
#

# 直到当前路径没有这个控件until_not
# ele2=WebDriverWait(driver,5,0.5).until_not(EC.presence_of_element_located((By.XPATH,'//div[@class="schbox"]/form/input')))
# ele2.send_keys('123')
# time.sleep(2)
# driver.quit()

# # 窗体切换driver.window_handles
# driver.find_element_by_link_text('夏天最热').click()
# driver.maximize_window()
# print(driver.window_handles)
# time.sleep(2)
#
# driver.find_element_by_link_text('优惠券').click()
# print(driver.window_handles)
# time.sleep(2)

# 定位当前窗口current_window_handle
# print(driver.current_window_handle)
# time.sleep(2)
# driver.close()

# 切换到指定窗体 第一个窗口switch_to.windows
# driver.switch_to.window(driver.window_handles[0])
# time.sleep(2)
# driver.quit()

# # 弹出框处理
# driver.switch_to.send_keys('男装女装')
# time.sleep(2)
# # 输出文本框
# print(driver.switch_to.alert.text)
# time.sleep(2)
# # 接受文本
# driver.switch_to.alert.accept()
# time.sleep(2)
# #关闭文本框
# driver.switch_to.alert.dismiss()



# driver.find_element_by_xpath('html/body/div[5]/div/div[2]/div[2]/div[3]/dl[1]/dd/a[1]/img')
# time.sleep(2)