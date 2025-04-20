import random
from pathlib import Path

def create_name () -> str:
    elements = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    name = str(''.join(random.sample(elements, 8)))
    return name

directory = input('Введите имя директории, в которой будут сохранены файлы: ')
if not Path(directory).exists():
    print("Такой директории не существует!")
for i in range(10):
    file = Path(directory + '\\' + create_name() + '.txt')
    file.parent.mkdir(parents=True, exist_ok=True)
    file.touch()
    print(f'{i+1}. {file.absolute()}')