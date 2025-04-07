class CityDistanceMatrixClass:
    def __init__(self):
        self.distance_matrix_dictionary = {
            'A': {'A': 0, 'B': 100, 'C': 200, 'D': 150, 'E': 300},
            'B': {'A': 100, 'B': 0, 'C': 250, 'D': 180, 'E': 400},
            'C': {'A': 200, 'B': 250, 'C': 0, 'D': 120, 'E': 350},
            'D': {'A': 150, 'B': 180, 'C': 120, 'D': 0, 'E': 280},
            'E': {'A': 300, 'B': 400, 'C': 350, 'D': 280, 'E': 0}
        }

    def get_distance_between_cities_method(self, origin_city_input, destination_city_input):
        if origin_city_input in self.distance_matrix_dictionary:
            if destination_city_input in self.distance_matrix_dictionary[origin_city_input]:
                return self.distance_matrix_dictionary[origin_city_input][destination_city_input]
        return 0