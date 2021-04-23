class Person:
	def __init__(self, ID, Age, Hobby, Genre, Sport): 
		self.id = int(ID)
		self.age = int(Age)
		self.hobby = Hobby
		self.genre = Genre
		self.sport = Sport
		self.numericals = [self.age]

	def __str__(self): 
		return f"{self.id}: Person(age: {self.age}, hobby: {self.hobby}, genre: {self.genre}, sport: {self.sport})"

	def __repr__(self): return f"Person #{self.id}"
	
	def get_categoricals(self): return [self.hobby, self.genre, self.sport]
	def get_data(self): return self.categoricals + self.numericals
