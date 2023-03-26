from face_transcript import UserDatabase, CaptureFace

class CaptureFaceInDataBase:
    def __init__(self, database_name:str = 'db.sqlite3',
                table_name:str = 'users', save_image: bool= False, image_location:str="dataset",
                haarcascade_frontalface_location : str = './haarcascade_frontalface_default.xml') -> None:
        # Created database
        self.user_database = UserDatabase(database_name=database_name, table_name=table_name)
        self.user_database.create_user_database()
        # Initiating camera
        self.capture_face = CaptureFace(save_image=save_image, image_location=image_location, 
                                        haarcascade_frontalface_location=haarcascade_frontalface_location)
        
    def take_photo(self, username, databasename ):
        pass
