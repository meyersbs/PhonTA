
#!/usr/bin/python

#################################################################################
# @PROJECT: PhonTA - Phonetic Transcription Assistant				#
# @VERSION:									#
# @AUTHOR: Benjamin Meyers							#
# @EMAIL: ben@lionlogic.org							#
# @LICENSE: MIT									#
#################################################################################

##### IMPORTS ###################################################################
import os, subprocess

##### VARIABLES #################################################################
arpa_to_ipa = {	"AA":u'\u0000', "AA0":u'\u0000', "AA1":u'\u0000', "AA2":u'\u0000',
		"AE":u'\u0000', "AE0":u'\u0000', "AE1":u'\u0000', "AE2":u'\u0000',
		"AH":u'\u0000', "AH0":u'\u0000', "AH1":u'\u0000', "AH2":u'\u0000',
		"AO":u'\u0000', "AO0":u'\u0000', "AO1":u'\u0000', "AO2":u'\u0000',
		"AW":u'\u0000', "AW0":u'\u0000', "AW1":u'\u0000', "AW2":u'\u0000',
		"AY":u'\u0000', "AY0":u'\u0000', "AY1":u'\u0000', "AY2":u'\u0000',
		"B":u'\u0000',
		"CH":u'\u0000',
		"D":u'\u0000',  "DH":u'\u0000',
		"EH":u'\u0000', "EH0":u'\u0000', "EH1":u'\u0000', "EH2":u'\u0000',
		"ER":u'\u0000', "ER0":u'\u0000', "ER1":u'\u0000', "ER2":u'\u0000',
		"EY":u'\u0000', "EY0":u'\u0000', "EY1":u'\u0000', "EY2":u'\u0000',
		"F":u'\u0000',
		"H":u'\u0000',  "HH":u'\u0000',
		"IH":u'\u0000', "IH0":u'\u0000', "IH1":u'\u0000', "IH2":u'\u0000',
		"IY":u'\u0000', "IY0":u'\u0000', "IY1":u'\u0000', "IY2":u'\u0000',
		"JH":u'\u0000',
		"K":u'\u0000',
		"L":u'\u0000',
		"M":u'\u0000',
		"N":u'\u0000',  "NG":u'\u0000',
		"OW":u'\u0000', "OW0":u'\u0000', "OW1":u'\u0000', "OW2":u'\u0000',
		"OY":u'\u0000', "OY0":u'\u0000', "OY1":u'\u0000', "OY2":u'\u0000',
		"P":u'\u0000',
		"R":u'\u0000',
		"S":u'\u0000',  "SH":u'\u0000',
		"T":u'\u0000',  "TH":u'\u0000',
		"UH":u'\u0000', "UH0":u'\u0000', "UH1":u'\u0000', "UH2":u'\u0000',
		"UW":u'\u0000', "UW0":u'\u0000', "UW1":u'\u0000', "UW2":u'\u0000',
		"V":u'\u0000',
		"W":u'\u0000',
		"Y":u'\u0000',
		"Z":u'\u0000',  "ZH":u'\u0000'}

def sort_dict(dictionary):
	""" Takes the given dictionary and sorts it alphabetically. """
	if os.path.exists(dictionary):
		subprocess.call(['sort', '-V', dictionary, '-o', dictionary], stdout=None)
		return True
	else:
		return False

def update_dict(dictionary):
	sort_dict(dictionary)
	return False

def translate(text):
	return False
