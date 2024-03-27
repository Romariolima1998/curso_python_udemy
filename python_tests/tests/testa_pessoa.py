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
from unittest.mock import patch
from pessoa import Pessoa



class TestPessoa(unittest.TestCase):
    def setUp(self) -> None:
        self.p1 = Pessoa('romario', 'lima')
        return super().setUp()
    
    def test_pessoa_attr_nome_tem_o_valor_correto(self):
        self.assertEqual(self.p1.nome, 'romario')
    
    def test_pessoa_attr_nome_e_str(self):
        self.assertIsInstance(self.p1.nome, str)

    def test_pessoa_attr_sobrenome_tem_o_valor_correto(self):
        self.assertEqual(self.p1.sobrenome, 'lima')

    def test_pessoa_attr_sobrenome_e_str(self):
        self.assertIsInstance(self.p1.sobrenome, str)

    def test_pessoa_attr_dados_obtidos_inicia_false(self):
        self.assertFalse(self.p1.dados_obtidos)

    def test_obter_todos_os_dados_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
    
    def test_obter_todos_os_dados_falha_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERRO 404')

    def test_obter_todos_os_dados_sucesso_e_falha_sequencial(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p1.dados_obtidos)

            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p1.dados_obtidos)


if __name__ == '__main__':
    unittest.main(verbosity=2)
