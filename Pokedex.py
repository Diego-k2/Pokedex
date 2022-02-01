"""
Pokedex dos principais pokemons (utilizando dicionarios)
"""

pokemons = {
    "bulbasaur": {
        "peso": "6.9kg",
        "tamanho": "0.7 m",
        "categoria": "grama",
        "evolucao": "ivysaur"
    },
    "charmander": {
        "peso": "8.5 kg",
        "tamanho": "0.6 m",
        "categoria": "fogo",
        "evolucao": "charmeleon"
    },
    "squirtle": {
        "peso": "9.0 kg",
        "tamanho": "0.5 m",
        "categoria": "agua",
        "evolucao": "wartortle"
    },
}

pesquisa_pokemon = input("Digite o nome do pokemon: ").lower()

if pesquisa_pokemon in pokemons:
    for poke_k, poke_v in pokemons[pesquisa_pokemon].items():
        print(poke_k, poke_v, sep="=")
else:
    print("Esse pokemon nao se encontra no pokedex")

