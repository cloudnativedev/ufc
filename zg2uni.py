# -*- coding: utf-8 -*-
import re

def replace(input):
	""" Replace each zawgyi code point with equivlant code point in Unicode.
	Conversions will be one on one. """
	output = output.replace(u'\u106A', u'\1009')

def decompose(input):
	""" Decompose combined characters to sequence of characters. """

def visual2logical(input):
	""" Reorder the sequence of characters from visual order to logical order. """

def normalize(input)
	""" 
	:param input: zawgyi encoded string
	:return: unicode string
	"""
def convert(input):
	tallAA = u'\u102B'
	AA = u'\u102C'
	vi = u'\u102D'
	# lone gyi tin
	ii = u'\u102E'
	u = u'\u102F'
	uu = u'\u1030'a q
	ve = u'\u1031'
	ai = u'\u1032'
	ans = u'\u1036'
	db = u'\u1037'
	visarga = u'\u1038'

	asat = u'\u103A'

	ya = u'\u103B'
	ra = u'\u103C'
	wa = u'\u103D'
	ha = u'\u103E'
	zero = u'\u1040'

	output = input

	output = output.replace(u'\u106A', u'\1009')

	output = re.sub(u'[\u103B\u107E\u107F\u1080\u1081\u1082\u1083\u1084]', u'\u103C', output)
	output = re.sub(u'(\u103A)(\u1037)', u"\\2\\1", output);

	# Reorder Yayit to CMV Format
	output = re.sub(u'(\u103C)([\u1000-\u1021])', u'\\2\\1', output)

	# Reorder ThaWayHtoe
	output = re.sub(u'\u1031([\u1000-\u1021])', u'\\1\u1031', output)
	output = re.sub(u'\u1031([\u103B-\u103E\+])', u'\\1\u1031', output)

	output = output.replace(u'\u103A\u1037', u'\u1037\u103A')
	output = output.replace(u'\u1075', u'\u1039\u1012')


	return output
