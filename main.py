import requests
import pytest

response = requests.post(url="https://api.pokemonbattle.me:9104/pokemons",
                         json={
                              "name": "Пикачу",
                              "photo": "https://dolnikov.ru/pokemons/albums/026.png" 
                              },
                            headers={"Content-Type": "application/json", "trainer_token": "0a9e5757c221c2091490bc645c5019df"}
                         )
print(response.text)

response = requests.patch(url="https://api.pokemonbattle.me:9104/pokemons",
                         json={
                              "pokemon_id": "21517", 
                              "name": "Чармандер", 
                              },
                            headers={"Content-Type": "application/json", "trainer_token": "0a9e5757c221c2091490bc645c5019df"}
                         )
print(response.text)

response = requests.post(url="https://api.pokemonbattle.me:9104/trainers/add_pokeball",
                         json={
                              "pokemon_id": "21518"
                              },
                            headers={"Content-Type": "application/json", "trainer_token": "0a9e5757c221c2091490bc645c5019df"}
                         )
print(response.text)