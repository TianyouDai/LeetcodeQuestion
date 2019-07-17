class Solution:
	def isAlienSorted(self, words: List[str], order: str) -> bool:
		words_values = [[order.index(char) for char in list(word)] for word in words]       

		while len(words_values) > 1:
			for i in range(len(words_values[0])):
				if words_values[0][i] > words_values[1][i]:
					return False
				elif words_values[0][i] < words_values[1][i]:
					words_values = words_values[1:]
					break

				if i == len(words_values[0]) - 1:
					words_values = words_values[1:]
				elif i == len(words_values[1]) - 1:
					return False

		return True
