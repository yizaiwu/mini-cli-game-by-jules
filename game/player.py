# This file will contain the Player class and related functions.
import time

class Player:
    def __init__(self, name="冒險者"):
        self.name = name
        self.max_hp = 50
        self.hp = 50
        self.attack = 5
        self.defense = 2
        self.level = 1
        self.exp = 0
        self.exp_to_next_level = 100

        # Player's starting position
        self.x = 1
        self.y = 1

    def move(self, dx, dy):
        """Moves the player by dx and dy."""
        self.x += dx
        self.y += dy

    def is_alive(self):
        """Checks if the player is still alive."""
        return self.hp > 0

    def add_exp(self, amount):
        """Adds experience points and handles leveling up."""
        self.exp += amount
        print(f"你獲得了 {amount} 點經驗值。")
        while self.exp >= self.exp_to_next_level:
            self._level_up()

    def _level_up(self):
        """Handles the player's level up."""
        self.level += 1
        self.exp -= self.exp_to_next_level
        self.exp_to_next_level = int(self.exp_to_next_level * 1.5) # Increase exp for next level

        # Stat increases
        self.max_hp += 10
        self.attack += 2
        self.defense += 1
        self.hp = self.max_hp # Fully heal on level up

        print(f"\n*** 等級提升！你現在是 {self.level} 級！ ***")
        print(f"生命值上限增加至 {self.max_hp}。")
        print(f"攻擊力提升至 {self.attack}。")
        print(f"防禦力提升至 {self.defense}。")
        print("你的生命值已完全恢復！")
        time.sleep(2)

    def get_status(self):
        """Returns the player's current status as a formatted string."""
        return (
            f"--- 玩家狀態 ---\n"
            f"名稱: {self.name}\n"
            f"等級: {self.level}\n"
            f"生命值: {self.hp}/{self.max_hp}\n"
            f"攻擊力: {self.attack}\n"
            f"防禦力: {self.defense}\n"
            f"經驗值: {self.exp}/{self.exp_to_next_level}\n"
            f"----------------"
        )