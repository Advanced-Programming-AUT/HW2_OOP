from game_system import WarGameSystem

game_system = WarGameSystem()

while True:
    user_input_line = input().strip()
    if not user_input_line:
        continue

    parts = user_input_line.split()
    command = parts[0]

    if command == "CREATE_USER":
        name = parts[1]
        if game_system.create_new_player_account(name):
            print(f"Registered {name} with initial money of 100")

    elif command == "BUY":
        name = parts[1]
        soldier_type = parts[2]
        quantity = int(parts[3])

        if not game_system.process_soldier_purchase(name, soldier_type, quantity):
            print("Purchase failed")
        else:
            # Display soldier type in correct case
            display_type = {
                "Infantry": "infantry",
                "Cavalry": "Cavalry",
                "Archer": "Archers",
                "ArmoredCavalry": "Armored Cavalry"
            }.get(soldier_type, soldier_type)
            print(f"{name} bought {quantity} {display_type}")

    elif command == "ATTACK":
        attacker = parts[1]
        defender = parts[2]
        print(f"{attacker} and {defender} started a battle")

        winner = game_system.execute_battle_between_players(attacker, defender)
        if winner == attacker:
            print(f"{defender} Lost the battle")
            print(f"{attacker} has taken 50 coin from {defender}")
        else:
            print(f"{attacker} Lost the battle")
            print(f"{defender} has taken 50 coin from {attacker}")

        defender_player = game_system.all_players_dictionary[defender]
        if defender_player.money_amount <= 0 and defender_player.is_active_flag:
            print(f"{defender} is Eliminated")
            defender_player.is_active_flag = False

    elif command == "DAY" and len(parts) > 1 and parts[1] == "END":
        active_players = game_system.process_day_end()
        print("End of the day, players budgets:", end=" ")
        budgets = []
        for name, player in game_system.all_players_dictionary.items():
            if player.is_active_flag:
                budgets.append(f"{name} = {player.money_amount}")
            else:
                budgets.append(f"{name} = 0")
        print("، ".join(budgets))