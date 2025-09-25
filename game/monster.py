# This file will contain the Monster class and related functions.

class Monster:
    def __init__(self, name, hp, attack, defense, exp_reward):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.exp_reward = exp_reward

    def is_alive(self):
        """Checks if the monster is still alive."""
        return self.hp > 0

# A dictionary to hold monster templates
MONSTER_TEMPLATES = {
    "slime": {
        "name": "史萊姆",
        "hp": 20,
        "attack": 3,
        "defense": 1,
        "exp_reward": 10
    }
}

def create_monster(name):
    """Creates a monster instance from the template."""
    template = MONSTER_TEMPLATES.get(name.lower())
    if not template:
        return None
    return Monster(
        name=template["name"],
        hp=template["hp"],
        attack=template["attack"],
        defense=template["defense"],
        exp_reward=template["exp_reward"]
    )