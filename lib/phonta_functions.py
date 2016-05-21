
#!/usr/bin/python

#################################################################################
# @PROJECT: PhonTA - Phonetic Transcription Assistant				#
# @VERSION:									#
# @AUTHOR: Benjamin Meyers							#
# @EMAIL: ben@lionlogic.org							#
# @LICENSE: MIT									#
#################################################################################

import os, subprocess
from shutil import copyfile

def sort_dict(dictionary):
	""" Takes the given dictionary and sorts it alphabetically. """
	if os.path.exists(dictionary):
		subprocess.call(['sort', '-V', dictionary, '-o', dictionary], stdout=None)
		return True
	else:
		return False

