class Hero():
  count_hero = 0
  def __init__(self, name, life, mana):
    self.count_hero + 1
    self.name = name
    self.life = life
    Hero.count_hero += 1
    print('Создан персонаж ', name, 'под номером ', Hero.count_hero)
    


class Human_magic(Hero):
  def say(self):
    print(self.name, 'говорит: "Hello, i am Human magic!"')
    print()


class Orc_magic(Hero):
  def say(self):
    print(self.name, 'говорит: "Hello, i am Human magic!"')
    print()

class Human_war(Hero):
  def say(self):
    print(self.name, 'говорит: "Hello, i am Human war!"')    
    print()


class Orc_war(Hero):
  def say(self):
    print(self.name, 'говорит: "Hello, i am Human war!"')

    print()

human_war = Human_war('Gref', 120, 80)
human_war.say()


human_magic = Human_magic('Solve', 82, 150)
human_magic.say()


orc_magic = Orc_magic('Petro', 80, 120)
orc_magic.say()


orc_war = Orc_war('Dretor', 140, 50)
orc_war.say()

print("Животный и растительный мир сгенерирован...")
print('Квестовые персонажи сгенерированны...')
print('Все созданные персонажи заселены по своим стартовым локациям')
print()
print(    "Добро пожаловать в Four sides of fate")







