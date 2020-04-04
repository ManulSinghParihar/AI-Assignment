from random import randint

maxsize = 1000000

class Node(object):
	def __init__(self,depth,playNum,sticksRem,val=0):
		self.depth=depth
		self.playNum=playNum
		self.sticksRem=sticksRem
		self.val=val
		self.children=[]
		self.makeChildren()


	def makeChildren(self):
		if self.depth>=0:
			for i in range(1,3):
				v=self.sticksRem-i
				self.children.append(Node(self.depth-1,-self.playNum,v,self.realValue(v)))

	def realValue(self,value):
		if(value==0):
			return maxsize*-self.playNum #return maxsize*self.playNum
		elif(value<0): 
			return maxsize*-self.playNum
		return 0

def MinMax(node,depth,playNum):
	if(depth==0) or (abs(node.val)==maxsize):
		return node.val

		bestVal=maxsize*-playNum

	for i in range(len(node.children)):
		child=node.children[i]
		newVal=MinMax(child,depth-1,-playNum)
		if(abs(maxsize*playNum-newVal)<abs(maxsize*playNum-bestVal)):
			bestVal=newVal
	return bestVal

def AlphaBeta(node, depth, alpha, beta, playNum):
	if(depth==0) or (abs(node.val)==maxsize):
		return node.val

	bestVal=maxsize*-playNum
	if (playNum == 1):
		for i in range(len(node.children)):
			child=node.children[i]
			alpha = max(alpha, AlphaBeta(child, depth - 1, alpha, beta, 1))
			if beta <= alpha:
				break
		return alpha
		
	else:
		for i in range(len(node.children)):
			child=node.children[i]
			beta = min(beta, AlphaBeta(child, depth - 1, alpha, beta, -1))
			if beta <= alpha:
				break
		return beta
		
def Decis(sticks,playNum,isHumanPlaying=True):
	if isHumanPlaying:
		if sticks <= 0:
			print("*"*33)
			if playNum > 0:
				if sticks == 0:
					print("\tBot Won")
				else:
					print("\tHuman Won!!!")
			else:
				if sticks == 0:
					print("\tHuman Won!!!")
				else:
					print("\tBot Won!!!")
			print("*"*33)
			return 0
		return 1
	else:
		if sticks <= 0:
			print("*"*33)
			if playNum > 0:
				if sticks == 0:
					print("\tBot1 Won!!!")
				else:
					print("\tBot2 Won!!!")
			else:
				if sticks == 0:
					print("\tBot2 Won!!!")
				else:
					print("\tBot1 Won!!!")
			print("*"*33)
			return 0
		return 1

if __name__ == '__main__':
	sticksTotal = int(input("\nPick no. of sticks : "))
	depth = 4
	currPlay = 0

	game_choice = input('Enter your choice :\n\'a\' for Bot1 v/s Bot2\n\'b\' Bot v/s Human :\t')

	if game_choice == 'a':
		AI_num = int(input("Which bot do you want to play first ? (1 or 2) : "))
		currPlay = 1 if AI_num == 1 else -1
		Player_AI, Opp_AI = randint(1,3), 0
		print('AI-{}\'s choice : {}'.format(AI_num, Player_AI))
		node2 = Node(depth,currPlay,sticksTotal)
		sticksTotal -= Player_AI

		while sticksTotal > 0:
			currPlay = 1

			if Decis(sticksTotal, currPlay, False):
				currPlay = -1
				node = Node(depth,currPlay,sticksTotal)
				bestChoice = -100
				bestVal = -currPlay*maxsize
				for i in range(len(node.children)):
					nChild = node.children[i]
					newVal = AlphaBeta(nChild, depth, maxsize, -maxsize, currPlay)
					if abs(currPlay*maxsize-newVal) <= abs(currPlay*maxsize-bestVal):
						bestVal = newVal
						bestChoice = i
				bestChoice += 1
				if bestChoice > sticksTotal:
					bestChoice = sticksTotal
				print("AI-{}\'s choice : {}".format(4-AI_num, bestChoice))
				sticksTotal -= bestChoice
				Decis(sticksTotal, currPlay, False)
			currPlay *= -1
			AI_num = 4 - AI_num


	elif game_choice == 'b':
		while currPlay != 1 and currPlay != -1:
			currPlay = input("Want to play first ? (y or n) : ")
			currPlay = 1 if currPlay == 'y' else -1
			node2 = Node(depth,currPlay,sticksTotal)

			if currPlay == 1:
				print("Pick either 1, 2 or 3 sticks")

			while sticksTotal > 0:
				if currPlay == 1:
					print("{} sticks remain. Pick number\n".format(sticksTotal))
					choice = int(input("Human's choice : "))
					while choice > 3 or choice > sticksTotal:
						print("{} sticks remain. Pick correctly!!!\n".format(sticksTotal))
						choice = int(input("Human's choice : "))
					sticksTotal -= int(float(choice))

				else:
					currPlay = 1

				if Decis(sticksTotal, currPlay):
					currPlay *= -1
					node = Node(depth,currPlay,sticksTotal)
					bestChoice = -100
					bestVal = -currPlay*maxsize
					for i in range(len(node.children)):
						nChild = node.children[i]
						newVal = AlphaBeta(nChild, depth, maxsize, -maxsize, currPlay)
						if abs(currPlay*maxsize-newVal) <= abs(currPlay*maxsize-bestVal):
							bestVal = newVal
							bestChoice = i
					bestChoice += 1
					if bestChoice>sticksTotal:
						bestChoice = sticksTotal
					print("AI's choice : {}\n".format(bestChoice))
					sticksTotal -= bestChoice
					Decis(sticksTotal, currPlay)
				currPlay *= -1