'''
TDD: desinvolvimento dirigido a test

parte 1 -> criar o teste e ver falhar

parte2 -> criar o codigo e ver o teste passar

refactor
parte 3 -> melhorar meu codigo
'''

try:
    import os
    import sys

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except:
    raise

import unittest

from baconcomovos import bacon_com_ovos


class TestBaconComOvos(unittest.TestCase):
    def test_baconc_com_ovos_deve_levantar_assertionerror_se_nao_int(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('0')

    def test_bacon_com_ovos_deve_retornar_bacon_com_ovos_se_entrada_for_multiplo_de_3_e_5(self):
        entradas = 15, 30, 45, 60
        saida = 'Bacon com ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f'{entrada} nao retornou {saida}'
                    )
                
    def test_bacon_com_ovos_deve_retornar_passar_fome_se_entrada_nao_for_multiplo_de_3_e_5(self):
        entradas = 1, 2, 4, 7, 8
        saida = 'Passar fome'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f'{entrada} nao retornou {saida}'
                    )

    def test_bacon_com_ovos_deve_retornar_bacon_se_entrada_nao_for_multiplo_de_3(self):
        entradas = 3, 6, 9, 12
        saida = 'Bacon'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f'{entrada} nao retornou {saida}'
                    )

    def test_bacon_com_ovos_deve_retornar_ovos_se_entrada_nao_for_multiplo_de_5(self):
        entradas = 5, 10, 20, 25, 35
        saida = 'Ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f'{entrada} nao retornou {saida}'
                    )

if __name__ == '__main__':
    unittest.main(verbosity=2)
