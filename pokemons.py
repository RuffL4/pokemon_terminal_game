class Pokemon:
    def __init__(self, name):
        self.name = name

    @property
    def max_hp(self):
        return self._max_hp

    @property
    def attack(self):
        return self._attack

    @property
    def current_hp(self):
        return self._current_hp

    @property
    def defence(self):
        return self._defence

    @current_hp.setter
    def current_hp(self, other):
        self._current_hp = other

    @classmethod
    def class_info(cls):
        return f"{cls.__name__}: {cls.start_hp} hp, {cls.start_attack} attack"

    def self_info(self):
        return f"{self.__class__.__name__}: {self.name}, {self.current_hp}/{self.max_hp} hp, {self.attack} attack"

    def is_alive(self):
        return self._current_hp > 0


    def take_damage(self, damage):
        self._current_hp = max(0, self._current_hp - damage)

    def is_dead(self):
        return self._current_hp <= 0


class Bulbasaur(Pokemon):
    start_hp = 45
    start_attack = 49
    defence = 49

    def __init__(self, name="wild pokemon"):
        super().__init__(name)
        self._max_hp = Bulbasaur.start_hp
        self._attack = Bulbasaur.start_attack
        self._current_hp = Bulbasaur.start_hp
        self._defence = Bulbasaur.defence


class Charmander(Pokemon):
    start_hp = 39
    start_attack = 52
    defence = 43

    def __init__(self, name="wild pokemon"):
        super().__init__(name)
        self._max_hp = Charmander.start_hp
        self._attack = Charmander.start_attack
        self._current_hp = Charmander.start_hp
        self._defence = Charmander.defence


class Squirtle(Pokemon):
    start_hp = 44
    start_attack = 48
    defence = 65

    def __init__(self, name="wild pokemon"):
        super().__init__(name)
        self._max_hp = Squirtle.start_hp
        self._attack = Squirtle.start_attack
        self._current_hp = Squirtle.start_hp
