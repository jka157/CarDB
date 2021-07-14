import dataDB

#commit and push testing through PyCharm

MENU_PROMPT = """ --- Car Database ---

Following options are available:

1) Add new car to db
2) See all cars in db
3) Find a car by name
4) See which car is most expensive
5) Delete car with name from the db
6) Exit menu

Your selection: """

def menu():
    connection = dataDB.connect()
    dataDB.create_tables(connection)

    user_input = input(MENU_PROMPT)

    while user_input != "6":

        if user_input == "1":
            name = input("Enter car name: ")
            hp = int(input("Enter the horsepower rating of the car: "))
            tq = int(input("Enter the torque rating of the car: "))
            price = int(input("Enter the price of the car: "))

            dataDB.add_car(connection, name, hp, tq, price)

        elif user_input == "2":
            cars = dataDB.get_all_cars(connection)

            if len(cars) == 0:
                print("No cars in the database")

            else:
                for car in cars:
                    print(f"{car[1]} | {car[2]} | {car[3]} | {car[4]}")

        elif user_input == "3":
            name = input("Enter car name to find: ")
            cars = dataDB.get_cars_by_name(connection, name)

            if len(cars) == 0:
                print(f"No car {name} in the database")

            else:
                for car in cars:
                    print(f"{car[1]} | {car[2]} | {car[3]} | {car[4]}")

        elif user_input == "4":
            name = input("Enter car name to find: ")
            best_method = dataDB.get_best_preparation_for_bean(connection, name)

            print(f"The most expensive car is: {name}")

        elif user_input == "5":
            name = input("Enter name of car to delete: ")
            dataDB.delete_car(connection, name)
            print(f"The car {name} has been deleted from the database!")

        else:
            print("Invalid Option, please enter a valid option")

        user_input = input(MENU_PROMPT)



if __name__ == "__main__":
    menu()