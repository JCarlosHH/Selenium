import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

	#Prepara el entorno de la prueba
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Edge(executable_path = r'./Driver/msedgedriver.exe')
		driver = cls.driver
		driver.implicitly_wait(10)


	#Realiza una serie de acciones
	def test_hello_worl(cls):
		driver=cls.driver
		driver.get('https://www.platzi.com')
		driver.get('https://www.wikipedia.org')


	@classmethod
	#Realiza las acciones finales
	def tearDownClass(cls):
		cls.driver.quit()

if __name__ == "__main__":

	#Verbosity funciona para mostrar ciertos logs:
	# 0: Cuantos Tests corrió, 1: Lo mismo que 0 pero agrega el error, 2:cada test y cada resultado
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name='hello-world-report'))