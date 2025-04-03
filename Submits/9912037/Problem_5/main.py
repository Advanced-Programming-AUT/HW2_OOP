from logistics import LogisticsManagementSystemClass

logistics_system_instance = LogisticsManagementSystemClass()

while True:
    print("\nLogistics Management System")
    print("1. Add Vehicle")
    print("2. Set Fuel Price")
    print("3. Add Trip")
    print("4. End Month")
    print("5. Exit")

    user_choice_input = input("Enter your choice: ")

    if user_choice_input == "1":
        vehicle_type = input("Enter vehicle type (CAR/PICKUP/TRUCK/PLANE): ")
        fixed_cost = int(input("Enter fixed cost: "))
        variable_cost = int(input("Enter variable cost per km: "))
        fuel_consumption = float(input("Enter fuel consumption per km: "))

        new_vehicle = logistics_system_instance.add_vehicle_method(vehicle_type, fixed_cost, variable_cost,
                                                                   fuel_consumption)
        print("Vehicle " + vehicle_type + " added with ID: " + str(new_vehicle.id_number_of_vehicle_attribute))

    elif user_choice_input == "2":
        fuel_type = input("Enter fuel type (GASOLINE/DIESEL/JET_FUEL): ")
        price = int(input("Enter price per liter: "))
        if logistics_system_instance.set_fuel_price_method(fuel_type, price):
            print("Fuel price for " + fuel_type + " set to " + str(price) + " per liter.")
        else:
            print("Invalid fuel type!")

    elif user_choice_input == "3":
        vehicle_id = int(input("Enter vehicle ID: "))
        origin = input("Enter origin city (A/B/C/D/E): ")
        destination = input("Enter destination city (A/B/C/D/E): ")
        cargo_weight = int(input("Enter cargo weight: "))

        if logistics_system_instance.add_trip_method(vehicle_id, origin, destination, cargo_weight):
            print("Trip registered successfully!")
        else:
            print("Failed to register trip!")

    elif user_choice_input == "4":
        report = logistics_system_instance.generate_monthly_report_method()
        print(report)

    elif user_choice_input == "5":
        break

    else:
        print("Invalid choice!")