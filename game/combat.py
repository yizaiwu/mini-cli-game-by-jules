import time
import threading

class CombatSystem:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster
        self.is_fighting = False
        self.player_command = None

    def start_combat(self):
        """Starts the real-time combat loop."""
        print(f"\n--- 戰鬥開始！---")
        self.is_fighting = True

        # Start auto-attack threads
        player_attack_thread = threading.Thread(target=self._auto_attack, args=(self.player, self.monster, 2)) # Player attacks every 2 seconds
        monster_attack_thread = threading.Thread(target=self._auto_attack, args=(self.monster, self.player, 3)) # Monster attacks every 3 seconds

        player_attack_thread.start()
        monster_attack_thread.start()

        # Main combat loop for player input
        while self.is_fighting:
            self._show_status()

            # Non-blocking input would be ideal, but for a simple CLI, a timeout is tricky.
            # We will use a simple input prompt. The auto-attacks will continue in the background.
            try:
                # We can't use a real non-blocking input easily in a cross-platform way.
                # So we'll just ask for input. The threads will keep running.
                self.player_command = input("戰鬥指令 (e.g., use 'power strike') > ").strip()
                self._process_player_command()
            except (EOFError, KeyboardInterrupt):
                # For non-interactive testing, treat as an empty command and continue.
                self.player_command = ""
                self._process_player_command()


            if not self.player.is_alive() or not self.monster.is_alive():
                self.is_fighting = False
                # A short delay to allow final attack messages to print
                time.sleep(0.1)

        player_attack_thread.join()
        monster_attack_thread.join()
        self._end_combat()

    def _auto_attack(self, attacker, target, interval):
        """A loop where the attacker automatically attacks the target."""
        while self.is_fighting:
            time.sleep(interval)
            if not self.is_fighting or not attacker.is_alive() or not target.is_alive():
                break

            damage = max(1, attacker.attack - target.defense)
            target.hp -= damage
            print(f"{attacker.name} 攻擊了 {target.name}，造成 {damage} 點傷害。")

    def _process_player_command(self):
        """Processes the command entered by the player."""
        if self.player_command == "use 'power strike'":
            print("你使用了強力一擊！")
            damage = self.player.attack * 2 # Double damage
            damage = max(1, damage - self.monster.defense)
            self.monster.hp -= damage
            print(f"你對 {self.monster.name} 造成了 {damage} 點巨大傷害！")
            self.player_command = None # Reset command
        elif self.player_command == "flee":
            print("你決定逃離戰鬥！")
            self.is_fighting = False
        # Other commands can be added here

    def _show_status(self):
        """Displays the current HP of player and monster."""
        # The \r and end='' help to overwrite the line for a cleaner look.
        status_line = f"\r{self.player.name}: {self.player.hp}/{self.player.max_hp} HP | {self.monster.name}: {self.monster.hp}/{self.monster.max_hp} HP"
        print(status_line, end="", flush=True)

    def _end_combat(self):
        """Handles the end of combat."""
        print() # Add a newline for cleaner output
        if self.player.is_alive():
            print(f"你擊敗了 {self.monster.name}！")
            self.player.add_exp(self.monster.exp_reward)
        else:
            print("你不幸被擊敗了...")
        print("--- 戰鬥結束 ---")
        time.sleep(2)