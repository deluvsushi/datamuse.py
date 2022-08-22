from requests import get


class Datamuse:
	def __init__(self):
		self.api = "https://api.datamuse.com"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
		}
	
	def get_words_with_similar_meaning(
			self,
			word: str):
		return get(
			f"{self.api}/words?ml={word}",
			headers=self.headers).json()
	
	def get_words_that_starts_with(
			self,
			word: str,
			starts_with: str,):
		return get(
			f"{self.api}/words?ml={word}&sp={starts_with}*",
			headers=self.headers).json()
	
	def get_words_that_ends_with(
			self,
			word: str,
			ends_with: str,):
		return get(
			f"{self.api}/words?ml={word}&sp=*{starts_with}",
			headers=self.headers).json()
	
	def get_words_that_sounds_like(
			self,
			word: str):
		return get(
			f"{self.api}/words?sl={word}",
			headers=self.headers).json()
	
	def get_words_with_starting_ending(
			self,
			word: str):
		return get(
			f"{self.api}/words?sp={word}",
			headers=self.headers).json()
	
	def get_words_spelled_similarly(
			self,
			word: str):
		return get(
			f"{self.api}/words?sp={word}",
			headers=self.headers).json()
	
	def get_words_that_rhyme_with(
			self,
			word: str):
		return get(
			f"{self.api}/words?rel_rhy={word}",
			headers=self.headers).json()
	
	def get_word_adjectives(self, word: str):
		return get(
			f"{self.api}/words?rel_jjb={word}",
			headers=self.headers).json()
	
	def get_word_nouns(self, word: str):
		return get(
			f"{self.api}/words?rel_jja={word}",
			headers=self.headers).json()
	
	def get_words_triggered_by(self, word: str):
		return get(
			f"{self.api}/words?rel_trg={word}",
			headers=self.headers).json()
	
	def get_word_far_suggestions(self, word: str):
		return get(
			f"{self.api}/sug?s={word}",
			headers=self.headers).json()
