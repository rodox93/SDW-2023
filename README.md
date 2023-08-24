# Desafio SDW 2023!

Olá.
Este desafio foi feito pensando em um sistema de mensagens no setor bancário, utilizando a API Rest desenvolvida pela DIO para simular um banco de dados bancário.
Com os scripts iremos extrair as informações com base na ID criada, solicitar ao chatGPT umas frases sobre importância de investimentos e retornar ao banco, para futuramente enviar aos usuários.


# Arquivos

Há 3 arquivos, são eles:
Extract.py - O script para extração dos dados da API solicitando pela ID do usuário
Transform.py - Nesse caso pegamos as informações como o nome do usuário e usando a API da OpenAi solicitamos ao ChatGPT que faça algumas frases personalizadas com no máximo 100 caracteres.
Load.py - Nesse arquivo enviamos para a API do SDW2023 os usuários atualizados com a frase gerada pelo chatGPT

## Usuários

São 4 usuários que foram criados por mim:
[368, 369, 370, 371]

## Arquivos CSV
Foi utilizado somente um arquivos CSV, nele consta as informações em uma coluna das ids dos usuários para serem carregadas no script extract

## JSON dos usuários [sem edição]


[368, 369, 370, 371]
[
  {
    "id": 368,
    "name": "Falafino de Sao Paulo",
    "account": {
      "id": 377,
      "number": "195959-1",
      "agency": "00001",
      "balance": 0.0,
      "limit": 0.0
    },
    "card": {
      "id": 356,
      "number": "**** **** 1322 1322",
      "limit": 1000.0
    },
    "features": [],
    "news": []
  },
  {
    "id": 369,
    "name": "Joaozinho alexandro de goiania",
    "account": {
      "id": 378,
      "number": "195960-1",
      "agency": "00001",
      "balance": 0.0,
      "limit": 0.0
    },
    "card": {
      "id": 357,
      "number": "**** **** 1322 1323",
      "limit": 1500.0
    },
    "features": [],
    "news": []
  },
  {
    "id": 370,
    "name": "Miri\u00e3 Oliveira de Sergipe",
    "account": {
      "id": 379,
      "number": "195961-1",
      "agency": "00001",
      "balance": 0.0,
      "limit": 0.0
    },
    "card": {
      "id": 358,
      "number": "**** **** 1322 1324",
      "limit": 1500.0
    },
    "features": [],
    "news": []
  },
  {
    "id": 371,
    "name": "Fabinho de Santos",
    "account": {
      "id": 380,
      "number": "195962-1",
      "agency": "00001",
      "balance": 0.0,
      "limit": 0.0
    },
    "card": {
      "id": 359,
      "number": "**** **** 1322 1325",
      "limit": 1500.0
    },
    "features": [],
    "news": []
  }
]
