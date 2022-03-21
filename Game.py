from random import *

class Things:
    def __init__(self, name, type, defence_thing, attack_thing, thing_life):
        self.name = name
        self.type = type
        self.defence_thing = defence_thing
        self.attack_thing = attack_thing
        self.thing_life = thing_life
    
    def thing_life_reduce(self):
        if self.thing_life - 1 != 0: 
            self.thing_life = self.thing_life - 1
        else:
            print(f'!!Снаряжение {self.name} разрушено!!')
            self.attack_thing = 0
            self.thing_life = 0
            self.defence_thing = 0

class Person:
    wearpons = []
    def __init__(self, name, hp, attack_damage, defence):
        self.name = name
        self.hp = hp
        self.attack_damage = attack_damage
        self.defence = defence

        
    def set_things(self, things):
        self.wearpons = things
        if len(things) !=0:
            for thing in self.wearpons:
                print(f'{self.name} получил {thing.name}')
                self.hp = self.hp + self.hp * thing.defence_thing
        else:
            print(f'{self.name} ничего не получил')
            
            

    def calc_attack_damage(self, other):
        extra_wearpon_damage = 0
        finalProtection = 0
        for thing in other.wearpons:
            if thing.thing_life > 0:
                
                finalProtection = finalProtection + thing.defence_thing
        for thing in self.wearpons:
            if thing.thing_life > 0:
                extra_wearpon_damage = extra_wearpon_damage + thing.attack_thing

        total_attack_damage = self.attack_damage + extra_wearpon_damage
        total_attack_damage = total_attack_damage - total_attack_damage * finalProtection #Тут бубет процент защиты, который получается от всех навесов
        return total_attack_damage
        
    
    def attacks(self, other):
        other.hp = other.hp - self.calc_attack_damage(other)
        for thing in self.wearpons:
            if thing.type != 'Защита':
                thing.thing_life_reduce()
        for thing in other.wearpons:
            if thing.type == 'Защита':
                thing.thing_life_reduce()
        


class Paladin(Person):
    def __init__(self, name, hp, attack_damage, defence):
        super().__init__(name, hp, attack_damage, defence)
        self.hp = self.hp * 2
        self.defence = self.defence * 2

class Warrior(Person):
    def __init__(self, name, hp, attack_damage, defence):
        super().__init__(name, hp, attack_damage, defence)
        self.attack_damage = self.attack_damage * 2
        
    

def Arena(people, things):
    things_for_person=[]
    for person in people:
        # if len(things)>0:
        n = randint(0, 2)
        while n>len(things):
            n = randint(0, 2)
        for i in range(n):
            pos_thing = randint(0, len(things)-1)
            things_for_person.append(things[pos_thing])
            
            things.pop(pos_thing)
        person.set_things(things_for_person)
        things_for_person = []
        print('-------------------------')
        print('Осталось в оружейной: ')
        for i in things:
            print(i.name)
        print('-------------------------\n')

    for i in people:
        print(f'{i.name}: HP = {i.hp}')
    
    print('----------------БОЙ-----------------\n')
    
    for i in range(len(people)-1):
        p_index = randint(0, len(people)-1)
        w_index = randint(0, len(people)-1)
        while w_index == p_index:
            w_index = randint(0, len(people)-1)
        p = people[p_index]
        w = people[w_index]
        print(f'-------Пара: {p.name}, {w.name}-------')
    
        while p.hp > 0 and w.hp > 0:
            print(f'HP {w.name}: {w.hp}, HP {p.name}: {p.hp}')
            print(f'{w.name} нападает и наносит урон {w.calc_attack_damage(p)}')
            w.attacks(p)
            if p.hp <= 0:
                break
            print(f'HP {w.name}: {w.hp}, HP {p.name}: {p.hp}')
            print(f'{p.name} нападает и наносит урон {p.calc_attack_damage(w)}\n')
            p.attacks(w)
            if w.hp <= 0:
                break
        
        if p.hp <= 0:
            print(f'Победил {w.name}\n')
            people.pop(p_index)
        elif w.hp  <= 0:
            print(f'Победил {p.name}\n')
            people.pop(w_index)


helmet = Things('Шлем', 'Защита', 0.1, 0, 5) #0.1 - процент защиты, 0 - атака, 5 - скорько раз можно юзануть
blade = Things('Меч', 'Холодное_оружие', 0, 5, 4)
knife = Things('Нож', 'Холодное_оружие', 0, 2, 2)
ring = Things('Кольцо', 'Магический_предмет', 0, 2, 2)
brone = Things('Броня', 'Защита', 0.1, 0, 6)
things=[helmet, blade, knife, ring, brone]
    
w1 = Warrior('Алексей', 100, 10, 5) #Урон 20
p1 = Paladin('Николай', 100, 10, 5) #Урон 10
w2 = Warrior('Максим', 120, 15, 5)
p2 = Paladin('Андрей', 60, 15, 5)
p3 = Paladin('Настя', 80, 15, 5)
people = [w1, p1, w2, p2, p3]

Arena(people, things)
