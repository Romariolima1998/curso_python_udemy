import unittest
from calculadora import soma, subtrai


class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_retorna_10(self):
        self.assertEqual(soma(5, 5), 10)

    def test_soma_varias_entradas(self):
        a_b_saidas = (
            (5, 6, 11),
            (6, 6, 12),
            (5, 5, 10),
        )
        for a_b_saida in a_b_saidas:
            with self.subTest(a_b_saida):
                a, b, saida = a_b_saida
                self.assertEqual(soma(a, b), saida)

    def test_soma_a_nao_int_ou_float_retorna_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma('k', 4)

    def test_soma_b_nao_int_ou_float_retorna_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma(4, '5')

    def test_subtrai_300_de_200_retorna_menos_100(self):
        self.assertEqual(subtrai(300, 200), 100)

    def test_subtrai_varias_entradas(self):
        a_b_saidas = (
            (3, 5, -2),
            (1100, 500, 600)
        )
        for a_b_saida in a_b_saidas:
            with self.subTest(a_b_saida):
                a, b, saida = a_b_saida
                self.assertEqual(subtrai(a, b), saida)

    def test_subtrai_a_nao_int_ou_float_retorna_assertionerror(self):
        with self.assertRaises(AssertionError):
            subtrai('f', 1)

    def test_subtrai_b_nao_int_ou_float_retorna_assertionerror(self):
        with self.assertRaises(AssertionError):
            subtrai(1, 'f')


if __name__ == '__main__':
    unittest.main(verbosity=2)
