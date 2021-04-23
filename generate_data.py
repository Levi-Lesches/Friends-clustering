from csv import DictWriter
import random
from pathlib import Path
from person import Person

NUM_PEOPLE = 370

data_file = (r"data\people.csv")
metrics_file = Path(r"data\metrics.csv")

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
	metrics_file.unlink(missing_ok = True)
	with open(data_file, "w", newline = "") as file: 
		writer = DictWriter(file, ["ID"] + list(choices.keys()))
		writer.writeheader()
		for index, row in enumerate(data, start = 1): 
			row ["ID"] = index
			writer.writerow(row)

people = generate_people()
save(people)
