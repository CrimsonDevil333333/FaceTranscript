import PIL.Image
import io
import numpy as np

from facetranscript import CaptureFaceInDataBase

def load_image_from_bytes(file_data, mode='RGB'):
    im = PIL.Image.open(io.BytesIO(file_data))
    if mode:
        im = im.convert(mode)
    return np.array(im)

class FaceTrainer:
    def __init__(self, face_data:CaptureFaceInDataBase) -> None:
        self.face_data_instance = face_data
        self.transformed_list = []
        self.known_face_encodings = []
        self.known_face_names = []
        self.face_locations = []
        self.face_encodings = []
        self.face_names = []
        self.process_this_frame = True
    
    def refresh_transformed_list(self)-> None:
        self.transformed_list = []
        self.known_face_encodings = []
        self.known_face_names = []
        self.face_locations = []
        self.face_encodings = []
        self.face_names = []
    
    def print_all_lists(self)-> None:
        print(self.known_face_names)
        print(self.known_face_encodings)
    
    def transform_all_faces(self)->None:
        user_list =self.face_data_instance.get_all_users()
        self.refresh_transformed_list()
        if len(user_list) == 0:
            return None
        for user in user_list:
            user_name, user_image = user
            user_image = load_image_from_bytes(user_image)
            self.known_face_encodings.append(user_image)
            self.known_face_names.append(user_name)