from configparser import ConfigParser

file_path = r"C:\Users\AIB\Desktop\337.all.tsv"


def file_to_stars_list(file_path) -> list:
    stars_list = []
    with open(f"{file_path}", "r") as f:
        for row in f:
            stars_list.append(row.split("\t"))
    return stars_list


def extract_and_filter_stars(stars_list):
    id_ra_dec_mag_list = []
    for item in range(2, len(stars_list[3])):

        id_ra_dec_mag_list = []
    id_ra_dec_mag = "config.ini"
    config = ConfigParser()
    config.read(id_ra_dec_mag)


