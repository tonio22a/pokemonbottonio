from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.hp = randint(900, 1100)
        self.power = randint(100, 250)

        Pokemon.pokemons[pokemon_trainer] = self

    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['sprites']['front_default']
        else:
            return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"

    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}, Урон покемона: {self.power}, Кол-во здоровья: {self.hp}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def attack(self, enemy):
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
        
class Fighter(Pokemon):

    def __init__(self, pokemon_trainer):
        super().__init__(pokemon_trainer)

        self.hp -= randint(100, 250)
        self.power += randint(100, 250)
        self.name += " Fighter"

class Wizard(Pokemon):

    def __init__(self, pokemon_trainer):
        super().__init__(pokemon_trainer)

        self.hp += randint(100, 250)
        self.power -= randint(50, 100)
        self.name += " Wizard"
