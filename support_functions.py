import global_vars as gv
import time


def check_ra_dec(star, fov_h, fov_v, input_ra, input_dec) -> bool:
    """Checks if the RA and declination of a star is within the given FOV frame."""
    if (input_ra - fov_h / 2 < star[gv.OUTPUT_RA_IND] < input_ra + fov_h / 2
            and input_dec - fov_v / 2 < star[gv.OUTPUT_DEC_IND] < input_dec + fov_v / 2):
        return True
    else:
        return False


def sort_descending(f_list, index) -> list:
    for i in range(0, len(f_list)):
        for j in range(0, len(f_list) - 1):
            if f_list[j][index] > f_list[j + 1][index]:
                f_list[j], f_list[j + 1] = f_list[j + 1], f_list[j]
    return f_list


def output(n_stars_list):
    """Creates csv file and puts the given list into it."""
    ct = time.strftime('%Y-%m-%d %H.%M.%S')
    with open(f"{ct}.csv", "w") as f:
        f.write("star_id, ra, dec, mag, dist \n")
        for row in n_stars_list:
            f.write(f"{row[gv.OUTPUT_ID_IND]}, "
                    f"{row[gv.OUTPUT_RA_IND]}, "
                    f"{row[gv.OUTPUT_DEC_IND]}, "
                    f"{row[gv.OUTPUT_MAG_IND]}, "
                    f"{(row[gv.OUTPUT_DIST_IND])} \n")
