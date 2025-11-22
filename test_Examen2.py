import unittest
from Examen2 import MiClase

class testExamen2(unittest.TestCase):
    
    def setUp(self):
        self.objeto = MiClase(
            Valencia=5,
            Tempo=120,
            Tonos=12,
            listaCanciones=["Canción 1", "Canción 2", "Canción 3"],
            listaBailabilidad=[0.8, 0.9, 0.7]
        )
    
    # Pruebas para ObtieneValencia
    def test_ObtieneValencia_con_digitos_impares(self):
        resultado = self.objeto.ObtieneValencia(1234567)
        self.assertEqual(resultado, 4)
    
    def test_ObtieneValencia_sin_digitos_impares(self):
        resultado = self.objeto.ObtieneValencia(2468)
        self.assertEqual(resultado, 0)
    
    # Pruebas para DivisibleTempo
    def test_DivisibleTempo_numero_diez(self):
        resultado = self.objeto.DivisibleTempo(10)
        self.assertEqual(resultado, [1, 2, 5, 10])
    
    def test_DivisibleTempo_numero_primo(self):
        resultado = self.objeto.DivisibleTempo(7)
        self.assertEqual(resultado, [1, 7])

    # Pruebas para ObtieneMasBailable
    def test_ObtieneMasBailable_lista_con_valores(self):
        resultado = self.objeto.ObtieneMasBailable([0.5, 0.9, 0.3, 0.7])
        self.assertEqual(resultado, 0.9)

    def test_ObtieneMasBailable_lista_vacia(self):
        resultado = self.objeto.ObtieneMasBailable([])
        self.assertIsNone(resultado)

    # Pruebas para VerificaListaCanciones
    def test_VerificaListaCanciones_sin_nulos(self):
        resultado = self.objeto.VerificaListaCanciones(["Canción A", "Canción B", "Canción C"])
        self.assertTrue(resultado)

    def test_VerificaListaCanciones_con_nulos(self):
        resultado = self.objeto.VerificaListaCanciones(["Canción A", None, "Canción C"])
        self.assertFalse(resultado)
    
    # Pruebas para Encuentra
    def test_Encuentra_elemento_presente(self):
        resultado = self.objeto.Encuentra([1, 5, 3, 7, 9], 7)
        self.assertTrue(resultado)

    def test_Encuentra_elemento_ausente(self):
        resultado = self.objeto.Encuentra([2, 4, 6, 8, 10], 5)
        self.assertFalse(resultado)


if __name__ == '__main__':
    unittest.main()
