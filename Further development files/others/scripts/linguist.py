# -*- coding: utf-8 -*-

'''
This Python script is intented for use where there is a need to check validity of the Phoenetic Transcription.
However, this code could be reused to make a proper Intelligent Phoeneme Transcriber in the future if you wish to (ehm.. 'if').

'''

import codecs
from itertools import tee, islice, chain, izip
class Linguist:
	vowels = set(["A","AA","I","II","U","UU","AE1","AE2","AI","O1","O2","AU"])

	velar_gutteral_c = set(["K11","KH1","G11","GH1","NG1"]) #ക vargam
	palatal_c = set(["C11","C11 CH","J1","JH1","N22 J1","Y1","S22"]) #ച vargam
	retroflex_cerebral_c = set(["T11","T1H","D1","DDH","N1","Z1","S11","L22"]) # vargam
	alveolar_c = set(["R1","R22","L11"])
	dental_c = set(["T22","T2H","D2","D2H","N22","S33"]) #ത vargam
	bilabal_c = set(["P1","PH1","B1","BH","M1"]) #പ vargam
	labiodental_c = set(["V1"])
	glottal_c = set(["H1"])
	nasal_sonorant = set(["NG1","N22 J1","N1","N22","M1"])

	consonants = velar_gutteral_c.union(palatal_c,retroflex_cerebral_c,alveolar_c,dental_c,bilabal_c,labiodental_c,glottal_c)

# A StackOverflow guide for next and previous item in a list
	def previous_and_next(self, some_iterable):
		preceeding_, current_, succeeding_ = tee(some_iterable, 3)
		preceeding_ = chain([None], preceeding_)
		succeeding_ = chain(islice(succeeding_, 1, None), [None])
		return izip(preceeding_, current_, succeeding_)

	def rule_voicing_of_stops(self, transcription_, preceeding_, current_, succeeding_, replace_):
		if preceeding_ in self.nasal_sonorant:
			if succeeding_ not in self.consonants and preceeding_ not in self.consonants:
				current_index = transcription_.index(current_)
				transcription_[current_index] = replace_
		elif succeeding_ in self.vowels:
			if succeeding_ not in self.consonants and preceeding_ not in self.consonants:
				current_index = transcription_.index(current_)
				transcription_[current_index] = replace_
		return transcription_

	def rule_t22_special(self, transcription_, preceeding_, current_, succeeding_):
		if current_ == 'T22':
			if preceeding_ != current_:
				if succeeding_ in self.consonants.difference(['M1','R1','Y1']) and succeeding_ != current_:
					current_index = transcription_.index(current_)
					transcription_[current_index] = "L1"
			if preceeding_ != current_:
				if succeeding_ == 'M1':
					current_index = transcription_.index(current_)
					transcription_[current_index] = "L1 M1"
		return transcription_

	def rule_applier(self, fileName):
		with codecs.open(fileName , "r" , "utf-8") as file: # Open file
			for each_line in file: # Read the line
				transcription = each_line.split(" ",1)[1].encode("ascii").split() # Split by first whitespace, take second part, refer: Dictionary fle
				for preceeding, current, succeeding in self.previous_and_next(transcription): # Get current phone and its predecessor and successor
					# Voicing of stops
					# case ക in between first and last phoneme
					if current == 'K11':
						transcription = self.rule_voicing_of_stops(transcription, preceeding, current, succeeding, 'G11')
					# case ച in between first and last phoneme
					elif current == 'C11':
						transcription = self.rule_voicing_of_stops(transcription, preceeding, current, succeeding, 'J1')
					# case ട in between first and last phoneme
					elif current == 'T11':
						transcription = self.rule_voicing_of_stops(transcription, preceeding, current, succeeding, 'D1')
					# case ത in between first and last phoneme
					elif current == 'T22':
						transcription = self.rule_voicing_of_stops(transcription, preceeding, current, succeeding, 'D2')
					# case പ in between first and last phoneme
					elif current == 'P1':
						transcription = self.rule_voicing_of_stops(transcription, preceeding, current, succeeding, 'B1')
					
					# case ത followed by മ eg. ആത്മാവ് and other half /t22/ cases
					transcription = self.rule_t22_special(transcription, preceeding, current, succeeding)
				print(transcription)

li = Linguist()
li.rule_applier("a.txt") # Too lazy here!
