class SoldierType:
    def __init__(self, type_name, cost_amount, attack_power_value, hit_chance_percentage, health_points):
        self.type_of_soldier = type_name
        self.cost_of_soldier = cost_amount
        self.attack_strength = attack_power_value
        self.hit_probability = hit_chance_percentage
        self.max_health = health_points

class SoldierInstance:
    def __init__(self, soldier_type_data):
        self.soldier_type_info = soldier_type_data
        self.current_health_status = soldier_type_data.max_health