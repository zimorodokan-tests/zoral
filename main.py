import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Firefox, FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

fp: FirefoxProfile = FirefoxProfile()
driver = Firefox(firefox_profile=fp)
link = "https://www.aihitdata.com"
try:
	driver.get(link)

	login_link = driver.find_element_by_partial_link_text("LOG IN")
	login_link.click()

	login_input_email = driver.find_element_by_id("email")
	login_input_email.send_keys("zimorodokan@gmail.com")
	login_input_password = driver.find_element_by_id("password")
	login_input_password.send_keys("111111")
	login_button_submit = driver.find_element_by_id("submit")
	login_button_submit.click()

	search_input_industry = driver.find_element_by_id("industry")
	search_input_industry.send_keys("mortgage")
	search_input_location = driver.find_element_by_id("location")
	search_input_location.send_keys("US")
	search_input_industry = driver.find_element_by_css_selector("form button[type=submit]")
	search_input_industry.click()

	search_links = driver.find_elements_by_css_selector(".col-md-8 .panel-body .panel-body div a")
	output = []
	company_links = []

	for link in search_links:
		company_page_link = link.get_attribute("href")
		company_name = link.text
		print("company_page_link:", company_page_link)
		company_links.append([company_name, company_page_link])

	for company in company_links:
		link = company[1]
		print("company_current_link:", link)
		driver.get(link)
		company_name = company[0]
		company_address = ''
		company_url = ''
		company_email = ''
		company_phone = ''
		main = WebDriverWait(driver, 30).until(
			EC.presence_of_element_located((By.ID, "main"))
		)

		try:
			e = driver.find_element_by_css_selector('i.icon-sm.icon-map-marker')
			parent = e.find_element_by_xpath("..")
			company_address = parent.text.strip()
			print("\tcompany_address", company_address)
		except NoSuchElementException:
			print(
				"\t",
				time.strftime("%H:%M:%S", time.localtime()),
				f"Address for '{company_name}' was not found.",
			)

		try:
			e = driver.find_element_by_css_selector('i.icon-sm.icon-home')
			parent = e.find_element_by_xpath("..")
			company_url = parent.find_element_by_css_selector("a").get_attribute("href")
			print("\tcompany_url", company_url)
		except NoSuchElementException:
			print(
				"\t",
				time.strftime("%H:%M:%S", time.localtime()),
				f"URL for '{company_name}' was not found.",
			)

		try:
			e = driver.find_element_by_css_selector('i.icon-sm.icon-email')
			parent = e.find_element_by_xpath("..")
			company_email = parent.find_element_by_css_selector("a").text.strip()
			print("\tcompany_email", company_email)
		except NoSuchElementException:
			print(
				"\t",
				time.strftime("%H:%M:%S", time.localtime()),
				f"Email for '{company_name}' was not found.",
			)

		try:
			e = driver.find_element_by_css_selector('i.icon-sm.icon-phone')
			parent = e.find_element_by_xpath("..")
			company_phone = parent.text.strip()
			print("\tcompany_phone", company_phone)
		except NoSuchElementException:
			print(
				"\t",
				time.strftime("%H:%M:%S", time.localtime()),
				f"Phone for '{company_name}' was not found.",
			)

		company_data = {'name': company_name, 'address': company_address, 'url': company_url, 'email': company_email, 'phone': company_phone}
		print(company_data, "\n\n")
		output.append(company_data)

	print(output)

except Exception as e:
    print(type(e))
    print(e.args)
    print(e)

finally:
	driver.quit()
