import main_functions as mf


def main():
    file_path = input("Please indicate a database file path: ")
    input_ra = float(input("Right Ascension: "))
    input_dec = float(input("Declination: "))
    fov_v = float(input("Field of view - vertical: "))
    fov_h = float(input("Field of view - horizontal: "))
    n = int(input("Number of stars to see in the output file: "))
    id_ra_dec_mag_list = mf.stars_id_ra_dec_mag_list(file_path)
    filtered_sorted_stars = mf.filtered_sorted_final_stars(id_ra_dec_mag_list, fov_h, fov_v, input_ra, input_dec)
    mf.final_n_stars_output(filtered_sorted_stars, n)


if __name__ == "__main__":
    main()
