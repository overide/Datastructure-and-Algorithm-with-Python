class Node:

	def __init__(self):
		self.children = dict()
		self.is_leaf = False

class Trie:

	def __init__(self):
		self.root = Node()

	def insert(self,word):
		'''
		Insert a word in the trie
		'''
		current = self.root
		for i, w in enumerate(word,1):
			if current.children.get(w,None) == None:
				n = Node()
				if i == len(word):
					n.is_leaf = True
				current.children[w] = n
			current = current.children[w]

	def search(self, word):
		'''
		Search the word in trie
		'''
		current = self.root
		for i,w in enumerate(word,1):
			if current.children.get(w,None):
				current = current.children[w]
				if i == len(word) and current.is_leaf == True:
					return True

			else:break

		return False

	def have_prefix(self, prefix):
		'''
		Search if given prefix exist in trie 
		'''
		current = self.root
		for i,w in enumerate(prefix,1):
			if current.children.get(w,None):
				current  = current.children[w]
				if i == len(prefix):
					return True
			else:break
		return False

	def _delete(self, word,current=None,depth=0):
		'''
		delete a given word from trie
		'''
		if depth < len(word):
			if current.children.get(word[depth], None):
				child = current.children[word[depth]]
				self._delete(word,child,depth+1)

				if child.children == {}:
					del current.children[word[depth]]

				if (child.is_leaf and (depth+1)) == len(word):
					child.is_leaf = False
				
			else:
				print("Word don't exist!")
				return

	def delete(self,word):
		current = self.root
		self._delete(word,current,0)