
#!/usr/bin/python

#################################################################################
# @PROJECT: PhonTA - Phonetic Transcription Assistant				#
# @VERSION:									#
# @AUTHOR: Benjamin Meyers							#
# @EMAIL: ben@lionlogic.org							#
# @LICENSE: MIT									#
#################################################################################

##### IMPORTS ###################################################################
import os, subprocess, re

##### VARIABLES #################################################################
arpa_to_ipa = {	"AA":u'\u0251', "AA0":u'\u0251', "AA1":u'\u0251', "AA2":u'\u0251',
		"AE":u'\u00E6', "AE0":u'\u00E6', "AE1":u'\u00E6', "AE2":u'\u00E6',
		"AH":u'\u028C', "AH0":u'\u028C', "AH1":u'\u028C', "AH2":u'\u028C',
		"AO":u'\u0254', "AO0":u'\u0254', "AO1":u'\u0254', "AO2":u'\u0254',
		"AW":u'\u0061\u028A', "AW0":u'\u0061\u028A', "AW1":u'\u0061\u028A', "AW2":u'\u0061\u028A',
		"AY":u'\u0061\u026A', "AY0":u'\u0061\u026A', "AY1":u'\u0061\u026A', "AY2":u'\u0061\u026A',
		"B":u'\u0062',
		"CH":u'\u0074\u0283',
		"D":u'\u0064',  "DH":u'\u00F0',
		"EH":u'\u025B', "EH0":u'\u025B', "EH1":u'\u025B', "EH2":u'\u025B',
		"ER":u'\u0279', "ER0":u'\u0279', "ER1":u'\u0279', "ER2":u'\u0279',
		"EY":u'\u0065\u026A', "EY0":u'\u0065\u026A', "EY1":u'\u0065\u026A', "EY2":u'\u0065\u026A',
		"F":u'\u0066',
		"G":u'\u0067',
		"HH":u'\u0068',
		"IH":u'\u026A', "IH0":u'\u026A', "IH1":u'\u026A', "IH2":u'\u026A',
		"IY":u'\u0069', "IY0":u'\u0069', "IY1":u'\u0069', "IY2":u'\u0069',
		"JH":u'\u0064\u0292',
		"K":u'\u006B',
		"L":u'\u006C',
		"M":u'\u006D',
		"N":u'\u006E',  "NG":u'\u014B',
		"OW":u'\u006F\u028A', "OW0":u'\u006F\u028A', "OW1":u'\u006F\u028A', "OW2":u'\u006F\u028A',
		"OY":u'\u0254\u026A', "OY0":u'\u0254\u026A', "OY1":u'\u0254\u026A', "OY2":u'\u0254\u026A',
		"P":u'\u0070',
		"R":u'\u0072',
		"S":u'\u0073',  "SH":u'\u0283',
		"T":u'\u0074',  "TH":u'\u03B8',
		"UH":u'\u028A', "UH0":u'\u028A', "UH1":u'\u028A', "UH2":u'\u028A',
		"UW":u'\u0075', "UW0":u'\u0075', "UW1":u'\u0075', "UW2":u'\u0075',
		"V":u'\u0076',
		"W":u'\u0077',
		"Y":u'\u0079',
		"Z":u'\u007A',  "ZH":u'\u0292'}

def format_cmudict(dictionary):
	""" Takes the given cmudict file and reformats it to CSV. """
	new_dict = open("dictionary.psv", "a")
	print("Formatting cmudict...")
	if os.path.exists(dictionary):
		with open(dictionary, "r") as f:
			for line in f:
				if ";;;" not in line:
					temp_line = re.split(r'\s\s', line)
					new_dict.write(temp_line[0] + "|" + temp_line[1].strip("\n") + "\n")
		new_dict.close()
		subprocess.call(['cp', "dictionary.psv", dictionary], stdout=None)
		subprocess.call(['rm', "dictionary.psv"], stdout=None)
		return True
	return False

def sort_cmudict(dictionary):
	""" Takes the given dictionary and sorts it alphabetically. """
	print("Sorting cmudict...")
	if os.path.exists(dictionary):
		subprocess.call(['sort', '-V', dictionary, '-o', dictionary], stdout=None)
		return True
	else:
		return False

def update_cmudict(dictionary):
	""" Converts the ARPABET given in the cmudict into IPA. """
	print("Updating cmudict...")
	format_cmudict(dictionary)
	sort_cmudict(dictionary)
	new_dict = open("dictionary.psv", "wb")
	if os.path.exists(dictionary):
		with open(dictionary, "r") as f:
			for line in f:
				elems = line.split("|")
				temp_line = ""
				for item in elems[1].split():
					if item not in arpa_to_ipa:
						print("UNKNOWN: " + item)
						pass
					else:
						temp_line += arpa_to_ipa[item] + " "
				new_dict.write(line.strip("\n") + "|" + temp_line.encode('utf8').rstrip() + "\n")
		new_dict.close()
                subprocess.call(['cp', "dictionary.psv", dictionary], stdout=None)
                subprocess.call(['rm', "dictionary.psv"], stdout=None)
		return True
	return False

def translate(text):
	return False
