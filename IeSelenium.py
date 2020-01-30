from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time


# driver = webdriver.Ie()

driver = webdriver.Ie(executable_path = 'C:\Sanjay\IEDriver\IEDriverServer.exe')


driver.get("http://hsean196-uwfr.uesc.com/utils/security/securityhome.jsp")

driver.switch_to.frame("main")
# driver.switch_to.default_content()
uname_element = driver.find_element_by_xpath("//input[@id='username']")
uname_element.send_keys("ssg")

password_element = driver.find_element_by_xpath("//input[@id='password']")
password_element.send_keys("admin")

airline_element = driver.find_element_by_xpath("//input[@id='airline']")
airline_element.send_keys("UW")

# driver.find_element_by_name("btnLogin").click()

# driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td/table/tbody/tr[6]/td/input").click()

driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td/table/tbody/tr[6]/td/input").send_keys(Keys.ENTER);

# driver.findElement(By.id("searchMovielanding")).sendKeys(KEYS.ENTER);
time.sleep(2)

driver.switch_to.default_content()


driver.switch_to.frame("main")


# driver.find_element_by_link_text("Back Office Agent").click()
# driver.find_element_by_xpath("//html/body/table/tbody/tr/td/table[1]/tbody/tr/td[2]/table/tbody/tr[4]/td[1]/a").click()
time.sleep(2)

driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table[1]/tbody/tr/td[2]/table/tbody/tr[4]/td[1]/a").send_keys(Keys.ENTER)

time.sleep(2)

driver.switch_to.default_content()

driver.switch_to.frame("banner")

time.sleep(2)
# driver.find_element_by_partial_link_text("Utilities").click()

driver.find_element_by_partial_link_text("Utilities").send_keys(Keys.ENTER)

driver.switch_to.default_content()

driver.switch_to.frame("contents")

time.sleep(2)

driver.find_element_by_partial_link_text("Work").send_keys(Keys.ENTER)

driver.switch_to.default_content()

driver.switch_to.frame("main")


#Take the queue count

queue_count_element = driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[21]/td[2]")

queue_count_text = queue_count_element.text

print(queue_count_text)





driver.find_element_by_partial_link_text("Flights SSIM Message Error").send_keys(Keys.ENTER)

popupXpath ="/html[1]/body[1]/div[2]/table[1]/tbody[1]/tr[3]/td[1]/a[1]"

# print(dir(driver))

parentWindowHandler = driver.current_window_handle


# parentWindowHandler = driver.getWindowHandle
handles = driver.window_handles;
size = len(handles);

for x in range(size):
# 	driver.switch_to.window(handles[x]);
	subWindowHandler = handles[x]
# 	print (driver.title);

# driver.switch_to_window(subWindowHandler)

driver.switch_to.window(subWindowHandler)

driver.find_element_by_partial_link_text("Work").send_keys(Keys.ENTER)

driver.switch_to.window(parentWindowHandler)

time.sleep(2)

# driver.switch_to.default_content()

driver.switch_to.frame("main")

driver.switch_to.frame("second")

count = int(queue_count_text)
	



reason_element = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[3]/td/textarea")

reason_text = reason_element.text

print(reason_text)

# print("-------------------------------------------------------------------------------------------------------------------")

message_element = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[3]/td/textarea")

message_text = message_element.text

print(message_text)

print("-------------------------------------------------------------------------------------------------------------------")

time.sleep(2)

# driver.implicitly_wait(20) 
driver.switch_to.frame("first")



driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td/table/tbody/tr[4]/td/a[3]").send_keys(Keys.ENTER)


