import unittest
import requests

class TestStringMethods(unittest.TestCase):

     def test_000_cria_user(self):
        r = requests.post('http://localhost:5000/user', json={"name": "Impacta", "cnpj": "92810392813982012", "email": "renoir@impacta.com.br", "celular": "11965011785", "password":"1426"})

        if r.status_code == 404:
            self.fail("Página /user não definida no servidor para o método POST.")
        
def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


if __name__ == '__main__':
    runTests()