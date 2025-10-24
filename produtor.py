from kafka import KafkaProducer
import json
import time
import random
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
cidades=["Barbalha", "Juazeiro do Norte", "Crato", "Rio de Janeiro", "São Paulo", "João Pessoa", "Missão Velha", "Brejo Santo"]
paises = ["Brasil", "Estados Unidos", "Canadá", "Argentina", "Uruguai", "Chile", "Equador", "Japão", "China"]
def corpo_transacao():
    id_transacao = random.randint(1, 1_000_000_000)
    id_cliente = random.randint(1, 1_000_000_000)
    valor = random.randint(1, 1_000_000_000)
    cidade = random.choice(cidades)
    pais = random.choice(paises)
    hora = time.time()

    return {
        'id_transacao' : id_transacao,
        'id_cliente': id_cliente,
        'valor': valor,
        'cidade': cidade,
        'pais': pais,
        'hora': hora
    }