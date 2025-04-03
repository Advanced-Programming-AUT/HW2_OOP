from soldier import SoldierInstance

class PlayerAccount:
    def __init__(self, player_name_string):
        self.name_of_player = player_name_string
        self.money_amount = 100
        self.list_of_soldiers_owned = []
        self.is_active_flag = True

    def add_money_to_account(self, amount_to_add):
        self.money_amount = self.money_amount + amount_to_add

    def purchase_soldiers(self, soldier_type_object, number_to_buy):
        total_cost_value = soldier_type_object.cost_of_soldier * number_to_buy
        if total_cost_value > self.money_amount:
            return False
        self.money_amount = self.money_amount - total_cost_value
        for i in range(number_to_buy):
            new_soldier = SoldierInstance(soldier_type_object)
            self.list_of_soldiers_owned.append(new_soldier)
        return True

    def remove_defeated_soldiers(self):
        temp_list = []
        for soldier in self.list_of_soldiers_owned:
            if soldier.current_health_status > 0:
                temp_list.append(soldier)
        self.list_of_soldiers_owned = temp_list