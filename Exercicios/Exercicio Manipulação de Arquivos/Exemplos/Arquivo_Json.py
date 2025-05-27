import json

dicionario = {
    "nome": "João",
    "idade": 25
}

with open("dados.json", "w", encoding="utf-8") as f:
    json.dump(dicionario, f, indent=4, ensure_ascii=False, sort_keys=True)

with open("dados.json", "r", encoding="utf-8") as f:
    conteudo = json.load(f)
    print(json.dumps(conteudo, indent=4, ensure_ascii=False, sort_keys=True))