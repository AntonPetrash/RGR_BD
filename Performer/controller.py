class ControllerPerformer:
    def __init__(self, model_Performer, view_Performer):
        self.model_Performer = model_Performer
        self.view_Performer = view_Performer

    def add_Performer(self):
        # Requesting Performer data from the user

        Artist_ID = self.view_Performer.get_Artist_ID()
        name = self.view_Performer.get_Artist_name()
        surname= self.view_Performer.get_Artist_surname()
        genre = self.view_Performer.get_genre()

        if self.model_Performer.add_Performer(Artist_ID, name, surname, genre):
            self.view_Performer.show_Performer_message("Artist added successfully!")
        else:
            self.view_Performer.show_Performer_message("Failed to add Artist.")

    def view_Performers(self):
        # Call a method from the Model class to get all the Performer
        Performers = self.model_Performer.get_all_Performers()

        # Display Performers via a method from the ViewPerformer class (assuming you have such a class)
        self.view_Performer.show_Performers(Performers)

    def update_Performer(self):
        # Request the ID of the artist to be updated
        Artist_ID = self.view_Performer.get_Artist_ID()

        # Check if there is a Performer with the specified number
        Performer_exists = self.model_Performer.check_Performer_existence(Artist_ID)

        if Performer_exists:
            # Request updated Artist data from the user
            name = self.view_Performer.get_Artist_name()
            surname = self.view_Performer.get_Artist_surname()
            genre = self.view_Performer.get_genre()

            # Call a method from the Model class to update the Artist info
            success = self.model_Performer.update_Performer(Artist_ID, name, surname, genre)

            # Display a message about the result of the operation
            if success:
                self.view_Performer.show_Performer_message("Artist updated successfully!")
            else:
                self.view_Performer.show_Performer_message("Failed to update artist.")
        else:
            self.view_Performer.show_Performer_message("Artist with the specified ID does not exist.")

    def delete_Performer(self):
        # Request the ID of the Performer to be deleted
        Artist_ID = self.view_Performer.get_Artist_ID()

        # Check if there is a Performer with the specified ID
        Performer_exists = self.model_Performer.check_Performer_existence(Artist_ID)

        if Performer_exists:
            # Call a method from the Model class to delete a Performer
            success = self.model_Performer.delete_Performer(Artist_ID)

            # Display a message about the result of the operation
            if success:
                self.view_Performer.show_Performer_message("Performer deleted successfully!")
            else:
                self.view_Performer.show_Performer_message("Failed to delete Performer.")
        else:
            self.view_Performer.show_Performer_message("Performer with the specified ID does not exist.")

    def create_Performer_sequence(self):
        # Call method create_Performer_sequence from class ModelPerformer
        self.model_Performer.create_Performer_sequence()
        self.view_Performer.show_Performer_message("Performer sequence created successfully!")

    def generate_rand_Performer_data(self, number_of_operations):
        # Call the generate_rand_Performer_data method from the ModelPerformer class
        success = self.model_Performer.generate_rand_Performer_data(number_of_operations)

        if success:
            self.view_Performer.show_Performer_message(f"{number_of_operations} Performers generated successfully!")
        else:
            self.view_Performer.show_Performer_message("Failed to generate Performers.")

    def truncate_Performer_table(self):
        # Call the method of the corresponding model
        success = self.model_Performer.truncate_Performer_table()

        if success:
            self.view_Performer.show_Performer_message("All Performers data truncated successfully!")
        else:
            self.view_Performer.show_Performer_message("Failed to truncate Performer data.")