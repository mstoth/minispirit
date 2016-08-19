# Spirit web site

# When i go to the home page, I should see the title, "Spirit" 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import os

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		if os.name=='nt':
			self.browser = webdriver.Chrome()
		else:
			self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_for_home_page_items(self):
		# When I go to the home page
		self.browser.get('http://localhost:8000')

		# I should see the title as "Spirit"
		self.assertIn("Spirit",self.browser.title)

		# The heading on the page should also say "Spirit"
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Spirit',header_text)


		# The heading should be a link
		element = self.browser.find_element_by_link_text("Spirit")
		
		# There should be the far away image displayed
		e=self.browser.find_element_by_id('portrait')
		self.assertIn('portrait4close.png',e.get_attribute('src'))

		# I should see a link to the credits
		e=self.browser.find_element_by_link_text("Credits")
		


		# The link should take me to the start page
		element.click()
		windowHandles = self.browser.window_handles
		self.browser.switch_to.window(windowHandles[1])
		self.assertIn("Bewildering Guides for a Deserted Wife",\
			      self.browser.title)

		# After 8 seconds, the page will refresh to "Logotherapy"
		time.sleep(10)
		self.assertIn("Logotherapy",self.browser.title)
		
		# The image should be through the leaves after that
		e=self.browser.find_element_by_id('throughleaves')
		self.assertIn('throughleaves.jpg',e.get_attribute('src'))
		


if __name__=="__main__":
	unittest.main()
