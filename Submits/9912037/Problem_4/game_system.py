from player import PlayerAccount
from soldier import SoldierType
import random


class WarGameSystem:
    def __init__(self):
        self.all_players_dictionary = {}
        self.soldier_types_dictionary = {
            "Infantry": SoldierType("Infantry", 10, 1, 0.8, 3),
            "Cavalry": SoldierType("Cavalry", 25, 2, 0.6, 5),
            "Archer": SoldierType("Archer", 20, 1.5, 0.75, 2),
            "ArmoredCavalry": SoldierType("ArmoredCavalry", 50, 4, 0.4, 10)
        }

    def create_new_player_account(self, player_name):
        if player_name in self.all_players_dictionary:
            return False
        new_player = PlayerAccount(player_name)
        self.all_players_dictionary[player_name] = new_player
        return True

    def process_soldier_purchase(self, player_name, soldier_type_name, quantity_number):
        if player_name not in self.all_players_dictionary:
            return False
        if soldier_type_name not in self.soldier_types_dictionary:
            return False
        player_object = self.all_players_dictionary[player_name]
        soldier_type_object = self.soldier_types_dictionary[soldier_type_name]
        return player_object.purchase_soldiers(soldier_type_object, quantity_number)

    def execute_battle_between_players(self, attacker_name, defender_name):
        if attacker_name not in self.all_players_dictionary or defender_name not in self.all_players_dictionary:
            return None

        attacker = self.all_players_dictionary[attacker_name]
        defender = self.all_players_dictionary[defender_name]

        while True:
            if not attacker.list_of_soldiers_owned:
                defender.add_money_to_account(50)
                attacker.add_money_to_account(-50)
                return defender_name

            if not defender.list_of_soldiers_owned:
                transfer_amount = min(50, defender.money_amount)
                attacker.add_money_to_account(transfer_amount)
                defender.add_money_to_account(-transfer_amount)
                return attacker_name

            attacker_soldier = random.choice(attacker.list_of_soldiers_owned)
            defender_soldier = random.choice(defender.list_of_soldiers_owned)

            if random.random() < attacker_soldier.soldier_type_info.hit_probability:
                defender_soldier.current_health_status -= attacker_soldier.soldier_type_info.attack_strength

            defender.remove_defeated_soldiers()

            if defender.list_of_soldiers_owned:
                defender_soldier = random.choice(defender.list_of_soldiers_owned)
                attacker_soldier = random.choice(attacker.list_of_soldiers_owned)

                if random.random() < defender_soldier.soldier_type_info.hit_probability:
                    attacker_soldier.current_health_status -= defender_soldier.soldier_type_info.attack_strength

                attacker.remove_defeated_soldiers()

    def process_day_end(self):
        active_players = []
        for player in self.all_players_dictionary.values():
            if player.is_active_flag:
                player.add_money_to_account(50)
                active_players.append(player.name_of_player)
        return active_players