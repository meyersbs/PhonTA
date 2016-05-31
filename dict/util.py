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
curr_dir = os.path.dirname(__file__)
default_dictionary = curr_dir + "/english"
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

def download_cmudict():
	print("Downloading cmudict...")
	subprocess.call(['wget', 'http://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/cmudict-0.7b', '-P', curr_dir], stdout=None)
	temp_dict = curr_dir + '/cmudict-0.7b'
	subprocess.call(['cp', temp_dict, default_dictionary], stdout=None)
	subprocess.call(['rm', temp_dict], stdout=None)

def format_cmudict():
	""" Takes the given cmudict file and reformats it to CSV. """
	new_dict = open("dictionary.psv", "a")
	print("Formatting cmudict...")
	if os.path.exists(default_dictionary):
		with open(default_dictionary, "r") as f:
			for line in f:
				if ";;;" not in line and re.match(r'[A-Za-z\']', line[0]):
					temp_line = re.split(r'\s\s', line)
					new_dict.write(temp_line[0] + "|" + temp_line[1].strip("\n") + "\n")

		# Add missing terms.
		new_dict.write("&|AE2 N D\n")
		new_dict.write("@|AE2 T\n")
		# Close the file and cleanup the directory.
		new_dict.close()
		subprocess.call(['cp', "dictionary.psv", default_dictionary], stdout=None)
		subprocess.call(['rm', "dictionary.psv"], stdout=None)
		return True
	return False

def sort_cmudict():
	""" Takes the given dictionary and sorts it alphabetically. """
	print("Sorting cmudict...")
	if os.path.exists(default_dictionary):
		subprocess.call(['sort', '-V', default_dictionary, '-o', default_dictionary], stdout=None)
		return True
	else:
		return False

def update_cmudict():
	""" Converts the ARPABET given in the cmudict into IPA. """
	print("Updating cmudict...")
	new_dict = open("dictionary.psv", "wb")
	if os.path.exists(default_dictionary):
		with open(default_dictionary, "r") as f:
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
                subprocess.call(['cp', "dictionary.psv", default_dictionary], stdout=None)
                subprocess.call(['rm', "dictionary.psv"], stdout=None)
		return True
	return False

def upgrade_cmudict():
	download_cmudict()
	format_cmudict()
	sort_cmudict()
	update_cmudict()
	return "Successfully upgraded to the newest cmudict!"

def search_cmudict(term, encoding="IPA"):
        with open(default_dictionary, "r") as f:
                for line in f:
                        temp_line = line.split("|")
                        if temp_line[0] == term.upper().strip(".").strip("!").strip("?"):
                                if encoding == "IPA":
                                        return temp_line[2].rstrip().strip("\n")
                                else:
                                        return temp_line[1].rstrip().strip("\n")
        return "ERROR"

def add_to_cmudict(term, arpabet, ipa="NONE"):
	if search_cmudict(term) != "ERROR":
		return "Already in cmudict."
	else:
		if ipa == "NONE":
			ipa = search_cmudict(term, "IPA")
		else:
			pass
		
		with open(default_dictionary, "ab") as f:
			f.write(term + "|" + arpabet + "|" + ipa + "\n")

		sort_cmudict()
	return "Successfully added '" + term + "' to the cmudict."		

def translate(text):
	arpa = ""
	ipa = ""
	for term in text.split():
		arpa += search_cmudict(term, "ARPABET") + "   "
		ipa += search_cmudict(term, "IPA") + "   "
	print("ARPABET:\t" + arpa)
	print("IPA:\t\t" + ipa)
	return ""

