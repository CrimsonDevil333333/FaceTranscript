from facetranscript import UserDatabase, CaptureFace
class CaptureFaceInDataBase:
    """
    This class is used to capture face and store it in a database.

    Args:
        database_name (str): Name of the database. Default is 'db.sqlite3'.
        table_name (str): Name of the table. Default is 'users'.
        save_image (bool): Whether to save image or not. Default is False.
        image_location (str): Location where images will be saved. Default is 'dataset'.
        haarcascade_frontalface_location (str): Location of haarcascade_frontalface_default.xml file. Default is './haarcascade_frontalface_default.xml'.

    Attributes:
        user_database (UserDatabase): Object of UserDatabase class.
        capture_face (CaptureFace): Object of CaptureFace class.
        save_image (bool): Whether to save image or not.

    Methods:
        take_photo(username:str)-> None: Captures photo and stores it in database.
        get_all_users()-> list: Returns all users data from database.
        get_user_with_username(username:str)-> list: Returns user data with given username from database.
        close_all_connections()-> None: Closes all connections with database.
        delete_user_data(username:str)->bool: Deletes user data with given username from database.
        drop_table()->bool: Drops table from database.

    """
    def __init__(self, database_name:str = 'db.sqlite3',
                table_name:str = 'users', save_image: bool= False, image_location:str="dataset",
                haarcascade_frontalface_location : str = './haarcascade_frontalface_default.xml') -> None:
        # Created database
        self.user_database = UserDatabase(database_name=database_name, table_name=table_name)
        self.user_database.create_user_database()
        # Initiating camera
        self.capture_face = CaptureFace(save_image=save_image, image_location=image_location, 
                                        haarcascade_frontalface_location=haarcascade_frontalface_location)
        
        self.save_image = save_image
        
    def take_photo(self, username )-> None:
        """
        Captures photo and stores it in database.
        Args:
            username (str): Name of the user.
        Returns:
            None
        """
        image_bytes = self.capture_face.capture_image(user_name=username)
        self.user_database.insert_user_data_no_image(
            user_name=username, image_bytes=image_bytes
        )

    def get_all_users(self)-> list:
        """
        Returns all users data from database.
        Args:
            None
        Returns:
            list: List of all users data.
        """
        return self.user_database.get_all_user_data()
    
    def get_user_with_username(self, username)-> list:
        """
        Returns user data with given username from database.
        Args:
            username (str): Name of the user.
        Returns:
            list: List of user data with given username.
        """
        return self.user_database.get_user(user_name=username)
    
    def close_all_connections(self)-> None:
        """
        Closes all connections with database.
        Args:
            None
        Returns:
            None
        """
        self.user_database.terminate_database_connection()

    def delete_user_data(self, username)->bool:
        """
        Deletes user data with given username from database.
        Args:
            username (str): Name of the user.
        Returns:
            bool: True if deleted successfully else False.
        """
        return self.user_database.delete_user_data(user_name=username)
    
    def drop_table(self)->bool:
        """
        Drops table from database.
        Args:
            None
        Returns:
            bool: True if dropped successfully else False.
        """
        return self.user_database.drop_table()


