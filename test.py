# -*- coding: utf-8 -*-
from app import app
import unittest
import docker as docker_py
import pytest

class Test(unittest.TestCase):
    def setUp(self):
        # cria uma instância do unittest, precisa do nome "setUp"
        self.app = app.test_client()

        # envia uma requisicao GET para a URL
        self.result = self.app.get('/')

    def test_requisicao(self):
        # compara o status da requisicao (precisa ser igual a 200)
        self.assertEqual(self.result.status_code, 200)

    def test_conteudo(self):
        # verifica o retorno do conteudo da pagina
        self.assertEqual(self.result.data.decode('utf-8'), "Hello Kaique Fonseca") 

    def generate_container(request):
    """ Create a container for all tests within class to run inside of """

    con = docker.containers.run(image="test_image", tty=True, detach=True)
    request.cls.container = con
    
 
    def run_tests_in_container(request):
        """
        Not sure how to get the contents of request.function 
        to execute inside of the docker container
        """

        output = request.cls.container.exec_run('0.0.0.0') 

        exit_code = output[0]
        assert exit_code == 0    
