
class ControllerFestival:
    def __init__(self, model_Festival, view_Festival):
        self.model_Festival = model_Festival
        self.view_Festival = view_Festival

    def add_Festival(self):
        Festival_id = self.view_Festival.get_Festival_id()
        name, price, city = self.view_Festival.get_Festival_input()
        if self.model_Festival.add_Festival(Festival_id, name, price, city):
            self.view_Festival.show_Festival_message("Festival added successfully!")
        else:
            self.view_Festival.show_Festival_message("Failed to add Festival.")

    def view_Festivals(self):
        Festivals = self.model_Festival.get_all_Festivals()
        self.view_Festival.show_Festivals(Festivals)

    def update_Festival(self):
        # Request the ID of the Festival to be updated
        Festival_id = self.view_Festival.get_Festival_id()

        # Check if there is a Festival with the specified ID
        Festival_exists = self.model_Festival.check_Festival_existence(Festival_id)

        if Festival_exists:
            # Request updated Festival data from the user
            name, price, city = self.view_Festival.get_Festival_input()
            # Call a method from the Model class to update the Festival
            success = (self.model_Festival.update_Festival(Festival_id, name, price, city))

            # Display a message about the result of the operation
            if success:
                self.view_Festival.show_Festival_message("Festival updated successfully!")
            else:
                self.view_Festival.show_Festival_message("Failed to update Festival.")
        else:
            self.view_Festival.show_Festival_message("Festival with the specified ID does not exist.")

    def delete_Festival(self):
        Festival_id = self.view_Festival.get_Festival_id()

        # Check if there is a reservation with the specified ID
        Festival_exists = self.model_Festival.check_Festival_existence(Festival_id)

        if Festival_exists:
            if self.model_Festival.delete_Festival(Festival_id):
                self.view_Festival.show_Festival_message("Festival deleted successfully!")
            else:
                self.view_Festival.show_Festival_message("Failed to delete Festival.")
        else:
            self.view_Festival.show_Festival_message("Festival with the specified ID does not exist.")

    def create_Festival_sequence(self):
        # Call the create_client_sequence method from the ModelFestival class
        self.model_Festival.create_Festival_sequence()
        self.view_Festival.show_Festival_message("Festival sequence created successfully!")

    def generate_rand_Festival_data(self, number_of_operations):
        # Call the generate_rand_Festival_data method from the ModelFestival class
        success = self.model_Festival.generate_rand_Festival_data(number_of_operations)

        if success:
            self.view_Festival.show_Festival_message(f"{number_of_operations} Festivals generated successfully!")
        else:
            self.view_Festival.show_Festival_message("Failed to generate Festivals.")

    def truncate_Festival_table(self):
        # Call the method of the corresponding model
        success = self.model_Festival.truncate_Festival_table()

        if success:
            self.view_Festival.show_Festival_message("All Festival data truncated successfully!")
        else:
            self.view_Festival.show_Festival_message("Failed to truncate Festival data.")