
import os


class Config:
    BASE_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
    SRC_DIR_PATH = os.path.join(BASE_DIR_PATH, "Plate_Licenses")
    SRC_FILE_PATH = os.path.join(SRC_DIR_PATH, "plate_license_J.jpg")

    def __init__(self):
        self.SRC_ABSOLUTE_PATH_LIST = list()

        for file_item in os.listdir(self.SRC_DIR_PATH):
            file_item_abs_path = os.path.join(self.SRC_DIR_PATH, file_item)
            self.SRC_ABSOLUTE_PATH_LIST.append(file_item_abs_path)
