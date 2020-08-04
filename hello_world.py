import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

	#Prepara el entorno de la prueba
	def setUp(self):
		self.driver = webdriver.Edge(executable_path = r'C://Users/N0S4A2/Documents/Platzi/Python/Selenium/Driver/msedgedriver')
		driver = self.driver
		driver.implicitly_wait(10)


	#Realiza una serie de acciones
	def test_hello_worl(self):
		driver=self.driver
		driver.get('https://www.platzi.com')

	#Realiza las acciones finales
	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name='hello-world-report'))