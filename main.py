import json
import requests 
from time import sleep


def age_guesser(name):
    link = 'https://api.agify.io/?name=' + name
    request = requests.get(link)
    dictio = json.loads(request.text)
    age = dictio['age']
    print(f'Your age, according to your name is: {age}')

if __name__ == '__main__':
    name = input('What is your name? ')
    print('*'*5 + 'Guessing your age' + '*'*5)
    sleep(2)
    age_guesser(name)
    input('Press enter to exit')