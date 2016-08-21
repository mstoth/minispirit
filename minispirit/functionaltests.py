# Miniature Spirit web site


################################
# BOILER PLATE GIVEN TO STUDENTS
################################


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


#####################
# END OF BOILER PLATE
#####################


	def test_for_home_page_items(self):

		"""
		The Spirit web site explores a history of a family
		through the exploration of the house the family lived in.

		Before the exploration, a home page gives the following
		choices:

		1. entry into the exploration, the link says "Spirit" 
		2. Credits to acknowledge others, that link just says "Credits"

		There is ominous music in the background on the home page. 
		The background of the page is a ghostly image of two people
		representing the parents of the family. 

		"""

		#########
		# Testing
		#########

		# Going to the home page
		# Note: This is in itself a test, an exception error will occur if there is no file
		
		self.browser.get('http://localhost:8000/elizabeth/index.html')

		# Testing for the Ominous music.  You just need to know the name of the audio file.
		# This doesn't check if it's playing.  We assume that part works.

		m=self.browser.find_element_by_tag_name('audio')
		self.assertIn('OppressiveGloom.mp3',m.get_attribute('src'))

		# The home page displays a ghostly pair in the background.
		# We use the name of the file to verify it's there.
		
		e=self.browser.find_element_by_tag_name('img')
		self.assertIn('portrait4close.png',e.get_attribute('src'))

		# Testing the choices on the home page
		# We get the two links we said we should have.
		
		entry_element = self.browser.find_element_by_link_text("Spirit")
		credit_element = self.browser.find_element_by_link_text("Credits")
		
		# When the Spirit link is chosen, the house image is displayed in a new window.
		# Click on the link

		entry_element.click()

		# Since a new window is displayed, we need to get that.  This is more complicated
		# but i will help them with these problems.
		
		# We get the window handles for all the windows displayed
		windowHandles = self.browser.window_handles

		# We know the second window (index = 1) will be the new window
		self.browser.switch_to.window(windowHandles[1])

		# This uses the title of the page, You can also use other tests if you prefer like heading, etc. 
		self.assertIn("Bewildering Guides for a Deserted Wife",\
			      self.browser.title)

		e=self.browser.find_element_by_tag_name('img') 
		self.assertIn('ofaraway.jpg',e.get_attribute('src'))

		# To give the feeling of travel, footsteps are heard in the background for 8 seconds
		# and new image appears seeing the house through the trees. 

		# test for the footsteps
		s = self.browser.find_element_by_tag_name('audio')

		# wait for 8 seconds
		time.sleep(8)

		# see if throughleaves.jpg is now displayed. 

		e=self.browser.find_element_by_tag_name('img')
		self.assertIn('throughleaves.jpg',e.get_attribute('src'))
		


if __name__=="__main__":
	unittest.main()
