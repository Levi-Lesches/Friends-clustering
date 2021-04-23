from csv import DictWriter
import random

from person import Person

NUM_PEOPLE = 200
filename = "data.csv"

choices = {
	"Age": range(14, 19),
	"Hobby": ["Coding", "Art", "Studying", "Sports"],
	"Genre": ["Horror", "Comedy", "Action", "Drama", "Romance", "Sci-fi"],
	"Sport": ["Baseball", "Basketball", "Hockey", "Football", "Tennis", "Soccer", "Volleyball"]
}

def generate_people(): return [
	{topic: random.choice(choices [topic]) for topic in choices} 
	for _ in range(NUM_PEOPLE)
]

def save(data): 
	with open(filename, "w", newline = "") as file: 
		writer = DictWriter(file, ["ID"] + list(choices.keys()))
		writer.writeheader()
		for index, row in enumerate(data, start = 1): 
			row ["ID"] = index
			writer.writerow(row)

people = generate_people()
save(people)