# -*- coding: utf-8 -*-
import codecs
from itertools import tee, islice, chain, izip
class Linguist:
	vowels = ["A","AA","I","II","U","UU","AE1","AE2","AI","O1","O2","AU"]

	velar_gutteral_c = ["K11","KH1","G11","GH1","NG1"]
	palatal_c = ["C11","C11 CH","J1","JH1","N22 J1","Y1","S22"]
	retroflex_cerebral_c = ["T11","T1H","D1","DDH","N1","Z1","S11","L22"]
	alveolar_c = ["R1","R22","L11"]
	dental_c = ["T22","T2H","D2","D2H","N22","S33"]
	bilabal_c = ["P1","PH1","B1","BH","M1"]
	labiodental_c = ["V1"]
	glottal_c = ["H1"]

# A StackOverflow guide for next and previous item in a list
	def previous_and_next(self,some_iterable):
		prevs, items, nexts = tee(some_iterable, 3)
		prevs = chain([None], prevs)
		nexts = chain(islice(nexts, 1, None), [None])
		return izip(prevs, items, nexts)

	def rule_applier(self, fileName):
		with codecs.open(fileName , "r" , "utf-8") as file:
			for each_line in file:
				transcription = each_line.split(" ",1)[1].encode("ascii").split()
				for previous, item, nxt in self.previous_and_next(transcription):
					print "List : ",transcription,"\nItem is now", item, "next is", nxt, "previous is", previous
					# case ക in between first and last phoneme

					# check preceeding phoneme and succeeding phoneme
						# case: preceeded by nonnasal sonorant, succeeded by any vowels[]

li = Linguist()
li.rule_applier("a.txt")
