import main_functions as mf


def main():
    file_path = input("Please indicate a database file path: ")
    ra = input("Right Ascension: ")
    dec = input("Declination: ")
    fov_v = input("Field of View - vertical: ")
    fov_h = input("Field of View - horizontal: ")
    n = input("Number of stars to see in the output file: ")
