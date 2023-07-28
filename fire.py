# integrando o firebase ao python
import requests
from datetime import datetime
import json

data_hoje = datetime.today()
data_created = data_hoje.strftime("%d/%m/%Y")
data_update = data_hoje.strftime("%d/%m/%Y")
data_concluido = data_hoje.strftime("%d/%m/%Y")


link = "https://tokamban-65719-default-rtdb.firebaseio.com/"

# metodo (post)
dados = {
    "mensagem":"mensagem criada",
    "status":True,
    "homologacao":"desenv",
    "created":data_created,
    "update":data_update,
    "concluida":data_concluido,
    "user":'0rakul0'
}

requisicao_mensagem = requests.post(f'{link}/lista/.json', data=json.dumps(dados))
print(requisicao_mensagem)
print(requisicao_mensagem.text)


# metodo get por bloco vendedores
requisicao = requests.get(f'{link}/lista/.json')
dicio_link = requisicao.json()
print(dicio_link)


# metodo get por bloco produtos
requisicao = requests.get(f'{link}/lista/.json')
dic_requisicao = requisicao.json()
id_item = None
for item in dic_requisicao:
    id_item = item

# metodo para atualizar pacth
dados = {"mensagem": "mensagem atualizada", "atualizada_em":data_update}
requisicao = requests.patch(f'{link}/lista/{id_item}/.json', data=json.dumps(dados))
print(requisicao.text)


# Deletar uma venda (DELETE)
requisicao = requests.delete(f'{link}/lista/{id_item}/.json')
print(requisicao)
print(f"id apagado: {id_item}")
print(requisicao.text)