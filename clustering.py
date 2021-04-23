from csv import DictReader
from sklearn.preprocessing import OneHotEncoder
from sklearn.cluster import KMeans

from person import Person

NUM_CLUSTERS = 40

def get_data(): 
	filename = "data.csv"
	with open(filename) as file: 
		reader = DictReader(file)
		return [Person(**row) for row in reader]

def transform(people): 
	encoder = OneHotEncoder()
	categoricals = [person.get_categoricals() for person in people]
	encoder.fit(categoricals)
	transform = encoder.transform(categoricals).toarray()
	for transformed, person in zip(transform, people):
		person.categoricals = transformed

def get_labels(people):
	model = KMeans(n_clusters = NUM_CLUSTERS)
	means = model.fit([person.get_data() for person in people])
	return means.labels_

def get_clusters(people, labels): 
	result = [[] for _ in range(NUM_CLUSTERS)]
	for person, label in zip(people, labels):
		result [label].append(person)
	return result

people = get_data()
transform(people)
labels = get_labels(people)
clusters = get_clusters(people, labels)
for person in clusters [0]:
	print(person)
