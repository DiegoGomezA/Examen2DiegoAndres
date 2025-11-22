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


if __name__ == '__main__':
    unittest.main()
