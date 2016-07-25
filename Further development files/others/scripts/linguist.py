# -*- coding: utf-8 -*-
import codecs
class Linguist:
	vowels = ["A","AA","I","II","U","UU","AE1","AE2","AI","O1","O2","AU"]
	consonants = [	
		"K11","KH1","G11","GH1","NG1",
		"C11","C11 CH","J1","JH1","N22 J1",
		"T11","T1H","D1","DDH","N1",
		"T22","T2H","D2","D2H","N22",
		"P1","PH1","B1","BH","M1"
		"Y1","R22","L11","V1","S11","S22","S33","H1","L22","Z1","R1"
	]

	def rule_applier(self, fileName):
		with codecs.open(fileName , "r" , "utf-8") as file:
			for each_line in file:
				transcription = each_line.split(" ",1)[1].rstrip().split()
				for phoneme_index in range(len(transcription)):
					# case ക in between first and last phoneme
					if transcription[phoneme_index] == 'K11' and phoneme_index > 0 and phoneme_index < len(transcription) :
						# check preceeding phoneme and succeeding phoneme
						# case: preceeded by nonnasal sonorant, succeeded by any vowels[]

li = Linguist()
li.rule_applier("a.txt")
