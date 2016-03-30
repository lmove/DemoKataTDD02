from unittest import  TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class FunctionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)

    def test_register(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('linkRegistrarse')
        link.click()

        nombre = self.browser.find_element_by_id('nombre')
        nombre.send_keys('Francisco')

        apellidos = self.browser.find_element_by_id('apellidos')
        apellidos.send_keys('Saenz')

        self.browser.implicitly_wait(3)
        self.browser.find_element_by_xpath("//select[@id='idServicio']/option[text()='Pintura']").click()

        aniosExperiencia = self.browser.find_element_by_id('aniosExperiencia')
        aniosExperiencia.send_keys('4')

        telefono = self.browser.find_element_by_id('telefono')
        telefono.send_keys('3111111')

        correoElectronico = self.browser.find_element_by_id('correoElectronico')
        correoElectronico.send_keys('pacho4@buscoayuda.com')

        contrasenia = self.browser.find_element_by_id('contrasenia')
        contrasenia.send_keys('clave1234')

        foto = self.browser.find_element_by_id('foto')
        foto.send_keys('http://es.fakenamegenerator.com/images/sil-male.png')

        botonGuardar = self.browser.find_element_by_id('butGuardar')
        botonGuardar.click()

        self.browser.implicitly_wait(30)
        p = self.browser.find_element_by_xpath("//p[text()='Francisco Saenz']")

        self.assertIn('Francisco Saenz', p.text)

    def test_view_detail(self):
        self.browser.get('http://localhost:8000')
        self.browser.implicitly_wait(30)
        p = self.browser.find_element_by_xpath("//p[text()='Francisco Saenz']")
        p.click()

        nombre = self.browser.find_element_by_id('nombreCompleto')

        self.assertIn('Francisco Saenz', nombre.text)