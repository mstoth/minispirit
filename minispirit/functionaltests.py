# Miniature Spirit web site

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

		"""
		The Spirit web site explores a history of a family
		through the exploration of the house the family lived in.

		Before the exploration, a home page gives the following
		choices;

		1. entry into the exploration, the link says "Spirit" 
		2. Credits to acknowledge others, that link just says "Credits"

		"""
		# Testing
		# Going to the home page
		self.browser.get('http://localhost:8000')

		# The home page displays a ghostly pair in the background.
		e=self.browser.find_element_by_id('portrait')
		self.assertIn('portrait4close.png',e.get_attribute('src'))

		# Testing the choices on the home page
		entry_element = self.browser.find_element_by_link_text("Spirit")
		credit_element = self.browser.find_element_by_link_text("Credits")
		
		# When the Spirit link is chosen, the house image is displayed in a new window.
		entry_element.click()
		e=self.browser.find_element_by_id('faraway') # (to make things easy i attach an id to things)
		self.assertIn('ofaraway.jpg',e.get_attribute('src'))


		windowHandles = self.browser.window_handles
		self.browser.switch_to.window(windowHandles[1])
		self.assertIn("Bewildering Guides for a Deserted Wife",\
			      self.browser.title)

		# To add a feeling of spontaneity to the experince, if I dawtle, the image of the house
		# changes to an image through the trees.
		
		time.sleep(10)
		e=self.browser.find_element_by_id('throughleaves')
		self.assertIn('throughleaves.jpg',e.get_attribute('src'))
		


if __name__=="__main__":
	unittest.main()
