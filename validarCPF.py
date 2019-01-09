import re

class verificarCPF(object):
    def __init__(self, cpf):
        self.cpf = re.sub(r'[^\d]+', '', cpf)

    def verificaTamanho(self):
        """Verifica se  o cpf tem  11 dígitos.
            Retorna False caso não tenha 11 dígitos"""
    
        if len(self.cpf) == 11:
            return True
        else:
            return False
    
    def calcula(self, contDown, digitoVerificador):
        """Calcula os dígitos do CPF para comparar com os dígitos verificadores
            contDown = 10, digitoVerificador = 9, para o primeiro digito verificador
            contDown = 11, digitoVerificador = 10, para o segundo digito verificador.
            Retorna False caso  a  soma do produto não seja igual ao digito  verificador."""

        contUp = 0
        somaProduto = 0

        for num in self.cpf:
            if contUp < digitoVerificador:
                somaProduto = somaProduto + (int(num) * contDown)
                contDown -= 1
                contUp   += 1 

        resto = somaProduto * 10 % 11

        if resto == 10:
            resto = 0
        
        if int(resto) != int(self.cpf[digitoVerificador]):
            return False
        
        return True

    def casosEspeciais(self):
        """Verifica se há casos em que passam no cálculo de verificação.
            Retorna False caso haja um cpf inválido"""

        if re.match(r'(?!(\d)\1{10})\d{11}', self.cpf) == None:
            return False
        
        return True

    def verificar(self, ):
        """Verifica se é um cpf válido.
        Retorna True se for válido, senão False."""

        if self.verificaTamanho():
            if self.casosEspeciais():
                if self.calcula(10,9):
                    if self.calcula(11,10):
                        return True
        
        return False