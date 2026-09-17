from xmlrpc.server import SimpleXMLRPCServer

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

servidor = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)

servidor.register_function(soma, "soma")
servidor.register_function(subtracao, "subtracao")
servidor.register_function(multiplicacao, "multiplicacao")
servidor.register_function(divisao, "divisao")

print("Servidor RPC ativo na porta 8000...")
servidor.serve_forever()
