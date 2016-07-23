from info_tests import *
from pycomedoresugr import *

import unittest

class Test(unittest.TestCase):


    def test_get_menu_semana(self):
        
        menu_semana_obtenido = get_menu_semana("Test/test.html")
        
        
        self.assertEqual(menu_semana_obtenido, menu_semana)

    def test_menu_semana_diccionario(self):
    
        menu_semana_diccionario_obtenido = menu_semana_diccionario("Test/test.html")
        
        self.assertEqual(menu_semana_diccionario_info, menu_semana_diccionario_obtenido)

    
    def test_menu_dia(self):
    
        menu_dia_obtenido = menu_dia("Lunes","Test/test.html")
    
        self.assertEqual(menu_dia_info, menu_dia_obtenido)
        


if __name__ == '__main__':
    unittest.main() 
