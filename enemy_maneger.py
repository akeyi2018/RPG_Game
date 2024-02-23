import random, os


class Enemy():
    def __init__(self) -> None:
        self.root_path = './enemy_image'

    def generate_random_enemy(self):
        enemy_name_list = ['goblin',
                           'wizard',
                           'Snake Woman'
                        ]
        enemy_gifs = [
            'enemy_01.gif',
            'enemy_02.gif',
            'enemy_03.gif'
            ]
        choice = random.choice(enemy_gifs)
        index = enemy_gifs.index(choice)
        image_path = os.path.join(os.getcwd(), self.root_path, choice)
        return enemy_name_list[index], image_path
    

if __name__ == '__main__':
    instance = Enemy()
    print(instance.generate_random_enemy())

        