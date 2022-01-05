from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

class Animal(BaseModel):
    id : Optional[str]
    nome : str
    idade : int
    sexo: str
    cor : str

lista_de_animais : List[Animal] = []
app = FastAPI()

@app.post('/animais')
def cadastro_animal(animal : Animal):
    animal.id = str(uuid4())
    lista_de_animais.append(animal)
    return { 'mensagem': 'sucesso'}

@app.get('/animais')
def listar_animais():
    return lista_de_animais

@app.get('/animais/{id}')
def listar_animais_especifico(id : str):
    item_especifico = list(filter(lambda x: x.id == id, lista_de_animais))
    if item_especifico:
        return item_especifico
    else:
        return {'mensagem': 'não existe esse item'}

@app.delete('/animais/{id}')
def deletar(id : str):
    item_remover = list(filter(lambda x: x.id == id, lista_de_animais))
    if item_remover:
        lista_de_animais.remove(item_remover[0])
        return {'mensagem' : 'sucesso'}
    return {'mensagem' : 'não existe item com esse id'}
