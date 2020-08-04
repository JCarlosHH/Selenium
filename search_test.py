import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HomePageTest(unittest.TestCase):

	#Prepara el entorno de la prueba
	
	def setUp(self):
		self.driver = webdriver.Edge(executable_path = r'./Driver/msedgedriver.exe')
		driver = self.driver
		driver.get('http://demo.onestepcheckout.com/')
		driver.maximize_window()
		driver.implicitly_wait(15)


	#Realiza una serie de acciones
	#def test_serch_text_field(self):
	#	search_field = self.driver.find_element_by_id("search")


	#def test_serch_text_field_by_name(self):
	#	search_field = self.driver.find_element_by_name("q")


	#def test_serch_text_field_class_name(self):
	#	search_field = self.driver.find_element_by_class_name("input-text")


	#def test_serch_text_button_enabled(self):
	#	button = self.driver.find_element_by_class_name("button")


	def test_count_of_promo_banner_images(self):
		banner_list = self.driver.find_element_by_class_name("promos")
		banners = banner_list.find_element_by_tag_name('img')
		self.assertEqual(3, len(banners))


	#Realiza las acciones finales
	def tearDown(self):
		self.driver.quit()


if __name__ == "__main__":

	#Verbosity funciona para mostrar ciertos logs:
	# 0: Cuantos Tests corrió, 1: Lo mismo que 0 pero agrega el error, 2:cada test y cada resultado
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name='hello-world-report'))