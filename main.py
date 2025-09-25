import time
from game.player import Player
from game.world import get_location, MAP_WIDTH, MAP_HEIGHT
from game.monster import create_monster
from game.combat import CombatSystem

def main():
    """主遊戲迴圈"""
    player = Player()
    print("歡迎來到文字冒險遊戲！")
    time.sleep(1)
    print(f"你是一位名叫 {player.name} 的冒險者，旅程即將展開。")
    time.sleep(1)

    while True:
        current_location = get_location(player.x, player.y)

        if not current_location:
            print("錯誤：你走到了未知的地方。遊戲結束。")
            break

        # 顯示當前位置資訊
        print(f"\n--- {current_location['name']} ---")
        print(current_location['description'])

        # 檢查是否有怪物
        monster_name = current_location.get("monster")
        if monster_name:
            monster = create_monster(monster_name)
            if monster:
                combat = CombatSystem(player, monster)
                combat.start_combat()

                if not player.is_alive():
                    print("\n遊戲結束。")
                    break # End game loop if player is dead

                # After combat, the monster is defeated
                current_location["monster"] = None

        # 顯示玩家狀態
        print(player.get_status())

        # 提示可用指令
        print("\n你可以使用的指令：go north, go south, go east, go west, quit")
        command = input("你要做什麼？ > ").lower().strip()

        if command == "quit":
            print("感謝您的遊玩，再會！")
            break
        elif command.startswith("go "):
            direction = command.split(" ")[1]
            dx, dy = 0, 0

            if direction == "north":
                dy = -1
            elif direction == "south":
                dy = 1
            elif direction == "west":
                dx = -1
            elif direction == "east":
                dx = 1
            else:
                print("無效的方向。")
                continue

            new_x = player.x + dx
            new_y = player.y + dy

            # 檢查是否在邊界內
            if 0 <= new_x < MAP_WIDTH and 0 <= new_y < MAP_HEIGHT:
                player.move(dx, dy)
            else:
                print("你不能往那個方向走，那裡是世界的盡頭。")
                time.sleep(1)
        else:
            print("無效的指令。")
            time.sleep(1)

if __name__ == "__main__":
    main()