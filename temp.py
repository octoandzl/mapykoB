import numpy as np
import random as rm

state_space = ["rook","bishop","knight"]
#transitonNames = [["rr","rb","rk"],["br","bb","bk"],["kr","kb","kk"]]
#transitionMatrix = [[0.2,0.6,0.2],[0.1,0.6,0.3],[0.2,0.7,0.1]]

transitions = {"rr":0.2,"rb":0.6,"rk":0.2,"br":0.1,"bb":0.6,"bk":0.3
               "kr":0.2,"kb":0.7,"kk":0.1}

#This function checks if tansition matrix is properly built
def is_valid_transition_matrix(transitions):
	tot = 0
	for _ in transitions:
		tot += _
		if tot != 3:
			print("Transition matrix is not well built, check it.")
		else:
			print("Transition matrix is well built.")

def compute_probabilities(state_space, transitions):
	pass
