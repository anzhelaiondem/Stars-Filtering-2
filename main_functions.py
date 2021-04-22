import support_functions as sf
import global_vars as gv


# Extracts from the given file needed columns (id, ra, dec, mag).
def stars_id_ra_dec_mag_list(file_path) -> list:
    id_ra_dec_mag_list = []
    with open(f"{file_path}", "r") as f:
        for row in f:
            item = row.split("\t")
            if len(item) > 4:
                try:
                    id_ra_dec_mag_list.append([int(item[gv.FILE_ID_IND]),
                                               float(item[gv.FILE_RA_IND]),
                                               float(item[gv.FILE_DEC_IND]),
                                               float(item[gv.FILE_MAG_IND])])
                except ValueError:
                    pass
    return id_ra_dec_mag_list


# Filters the given file based on the inputted parameters(ra, dec, fov_h and fov_v) and sorts with brightness.
def filtered_sorted_final_stars(id_ra_dec_mag_list, fov_h, fov_v, input_ra, input_dec) -> list:
    filtered_sorted_list = []
    for item in id_ra_dec_mag_list:
        if sf.check_ra_dec(item, fov_h, fov_v, input_ra, input_dec):
            dist = ((input_ra - item[gv.OUTPUT_RA_IND]) ** 2 + (input_dec - item[gv.OUTPUT_DEC_IND]) ** 2) ** 0.5
            item.append(dist)
            filtered_sorted_list.append(item)
    sf.sort_descending(filtered_sorted_list, gv.OUTPUT_MAG_IND)
    return filtered_sorted_list


# Checks and provides the output file based on the given N.
def final_n_stars_output(filtered_sorted_list, n):
    if len(filtered_sorted_list) == 0 or n <= 0:
        print("There are no stars with the mentioned parameters.")
    if len(filtered_sorted_list) > n > 0:
        final_list = filtered_sorted_list[:n]
        sf.output(sf.sort_descending(final_list, gv.OUTPUT_DIST_IND))
    if len(filtered_sorted_list) < n:
        sf.output(sf.sort_descending(filtered_sorted_list, gv.OUTPUT_DIST_IND))
