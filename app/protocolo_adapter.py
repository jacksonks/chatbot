from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
import requests
import json


class ProtocoloLogicAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        """
        Retorna true se o statement conter
        as palavras 'status' e 'protocolo'
        seguido do número e senha
        """
        words = ['status', 'protocolo']
        if all(x in statement.text.split() for x in words):
            return True
        else:
            return False

    def process(self, input_statement, additional_response_selection_parameters):
        
        words = input_statement.text.split()
        num_protocolo = ''
        senha_protocolo = ''
        for i in range (len(words)):
            if(words[i] == "protocolo" and len(words) > i+2):
                num_protocolo = words[i+1]
                senha_protocolo = words[i+2]
                break
                
        API_PROTOCOLO = "http://protocolo:5056/protocolo"
        
        data = {
            'num_protocolo': num_protocolo,
            'senha_protocolo': senha_protocolo
        }
        
        r=requests.post(url = API_PROTOCOLO, data = data)
        resp = r.json()
        
        if resp['status_code'] == 200:
            confidence = 1
            mensagem = 'O status atual é: ' + str(resp['status'])
        else:
            confidence = 0
            mensagem = 'Não foi possível verificar status'
            

        response_statement = Statement(mensagem)
        response_statement.confidence = confidence

        return response_statement
