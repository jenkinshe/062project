from appium import webdriver
import unittest
import os
import time

class AndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='5.1.1'
        desired_caps['deviceName']='Android Emulator'
        desired_caps['noReset']='true'
        desired_caps['appPackage']='cn.xiaochuankeji.tieba'
        desired_caps['appActity']='.ui.base.SplashActivity 3823da00 pid=845'

        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        # self.driver.find_element_by_id('cn.xiaochuankeji.tieba:id/topic_name').click()
        # time.sleep(2)



# def test_element_by_id(self):
#     self.driver.implicitly_wait(60)
#     el=self.driver.find_element_by_id('cn.xiaochuankeji.tieba:id/topic')
#     el.click()

def test_element_by_xpath(self):
    self.driver.implicitly_wait(60)
    ele02=self.driver.find_element_by_xpath('//android.widget.TextView[@cn.xiaochuankeji.tieba:id/expand_content_view"]')
    ele02.click()
#      获取包名和包界面方法：   在cmd界面下输入 adb shell dumpsys activity top|findstr 'ACTIVITY'
#  注意appPackage是包名。包名是唯一的，appAvtviivity 包界面，注意此时快速进入界面，界面跳转之后会改变


# def test_elemnt_by_xpath(self):
#     self.driver.implicitly_wait(60)


# 通过xpath查找
# 通过单个id定位控件
# ele01=self.driver.find_element_by_xpath('//android.widget.TextView[@resource-id="cn.xiaochuankeji.tieba:id/option_tv1"]')
# ele01.click()
# # 通过多个id定位控件
# ele01=self.driver.find_elements_by_xpath('//android.widget.TextView[@resource-id="cn.xiaochuankeji.tieba:id/option_tv1"]')
# ele01.click()


# 三、通过text文本定位
# 四、xpath通过text文本定位，无控件属性*代表
# El04=self.driver.find_element_by_xpath(‘//*[@text=“图文”]’)
# Ele04.click()

# 五、xpath通过class查找单个元素（定位发布话题中的edittext）
# Ele05=self.driver.find_element_by_xpath(‘//*[@class=“android.widget.EditText”]’)
# Ele05.click()
#
# Ele051=self.driver,find_element_by_xpath(‘//android.widget.EditText’)
# Ele051.click()


# 六、组合定位（定位视频，定位搜索）and
# Ele06=self.driver.find_element_by_xpath(‘//*[@class="cn.xiaochuankeji.tieba:id/title” and @text="图文"]’).click()

# 七、搜索（按钮/个人头像）通过父级找子级定位控件

# 八、我的按钮 通过子级找父级定位控件 ../ 返回
# Ele08=self.driver.find_element_by_xpath(‘//*[@text="我的"]/../android.widget.ImageView’)
# Ele08.click()

