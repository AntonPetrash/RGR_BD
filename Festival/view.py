class ViewFestival:
    def show_Festivals(self, Festivals):
        print("Festivals:")
        for Festival in Festivals:
            print(f"ID: {Festival[0]}, Name: {Festival[1]}, Price: {Festival[2]}, City: {Festival[3]}")

    def get_Festival_input(self):
        name = input("Enter Festival name: ")
        price = input("Enter Festival price: ")
        city = input("Enter Festival city: ")
        return name, price, city

    def get_Festival_id(self):
        return int(input("Enter Festival id: "))

    def show_Festival_message(self, message):
        print(message)