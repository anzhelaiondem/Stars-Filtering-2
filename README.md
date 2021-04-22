# Stars-Filtering-2
## Summary
This program is designed to search in the given .tsv data file and create a .csv file that will contain the N brightest stars that are within the defined frames of equatorial coordinates. The frame is based on the provided horizontal and vertical field of view (fov_h, fov_v), right ascension (ra), and declination (dec). The output file also contains stars' id, equatorial coordinates (ra, dec), brightness (magnitude) and the distance from the given ra dec point. The final data is sorted in ascending order based on distance.

### Input
1 The absolute path of the file/data (the file should be in .tsv format).\
2 Right ascension.\
3 Declination.\
4 Field of view: vertical\
5 Field of view: horizontal\
6 The number of stars to see in the output file.

### Output
CSV file with the name of current date and time.\
The location of the output file is the same folder where the program files are.\
The file contains five attributes of the N files: id of a star (source_id), right ascension (ra_ep2000), declination (dec_ep2000), mean magnitude (phot_g_mean_mag), and distance (distance).

## Description of the program structure
The program consists of four modules: "main.py", "main_functions.py", "support_functions.py" and "global_vars.py".
The main running method is located in the "main.py" module that needs to be run.
After running it, the input function asks you to enter the above-mentioned parameters. After providing correct information, the program creates the output file with the current date and time (.csv) in the same directorey.

#### Limitations of the program
1. Provided link:\
	- The data file should be in .tsv format.\
	- The file should have exact form regarding the attributes/columns and their index:\
    . right ascension index: 0\
	. declination index: 1\
	. id index: 7\
	. mean magnitude index: 22\
	These are set in the "global_vars.py" module and can be adjusted according to the provided data file.

2. Inputted data:\
	- Inputted right ascension should be in degrees.\
	- All inputs (except the file path) should be numbers.

3. N number of start (N>0).\
	- If N is greater than the available number of stars, the output file will contain the available amount of stars.\
	- If there are no stars available, the program gives a warning message and does not create an output file.
