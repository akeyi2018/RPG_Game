import random, os, re
from data_config import Config
from glob import glob

class Enemy():
    def __init__(self) -> None:
        self.enemy_setting_path ='./enemy_settings'

    def generate_random_enemy(self):
        
        file_list = glob(os.path.join(os.getcwd(), self.enemy_setting_path, '*.json'))
        choice = random.choice(file_list)
        id = re.search(r'\d+', choice).group()
        config = Config(id)
        return config.get_json_info()

if __name__ == '__main__':
    instance = Enemy()
    print(instance.generate_random_enemy())


        