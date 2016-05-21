
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
