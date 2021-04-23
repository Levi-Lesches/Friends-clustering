from csv import DictReader
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt
from pathlib import Path

from person import Person

MIN_CLUSTER_SIZE = 4
MAX_CLUSTER_SIZE = 10
MIN_CLUSTERS = None
MAX_CLUSTERS = None


def get_data(): 
	filename = r"data\people.csv"
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

def get_metrics(people): 
	"""
	A list of datapoints representing which k works best for k-means
	"""
	global MIN_CLUSTERS
	MIN_CLUSTERS = len(people) // MAX_CLUSTER_SIZE
	MAX_CLUSTERS = len(people) // MIN_CLUSTER_SIZE
	filename = Path(r"data\metrics.csv")
	if filename.exists(): 
		print("Reading metrics")
		contents = filename.read_text()
		metrics = [float(num) for num in contents.split(",")]
	else: 
		print("Generating metrics")
		metrics = []
		data = [person.get_data() for person in people]
		k_range = range(MIN_CLUSTERS, MAX_CLUSTERS + 1)
		for k in k_range:
			model = KMeans(n_clusters = k).fit(data [:100])
			labels = model.labels_
			metrics.append(silhouette_score(data [:100], labels, metric = 'euclidean'))
		with open(filename, "w") as file: 
			file.write(",".join(map(str, metrics)))
		plt.plot(list(k_range), metrics)
		plt.show()
	return metrics

def determine_k(metrics): 
	"""
	Uses data from get_metrics to determine what the best k-value is
	"""
	max_metric = max(metrics)
	max_k = metrics.index(max_metric) + MIN_CLUSTERS
	return max_k

def get_labels(people, num_clusters):
	model = KMeans(n_clusters = num_clusters)
	means = model.fit([person.get_data() for person in people])
	return means.labels_

def get_clusters(num_clusters, people, labels): 
	result = [[] for _ in range(num_clusters)]
	for person, label in zip(people, labels):
		result [label].append(person)
	return result

people = get_data()
transform(people)
metrics = get_metrics(people)
num_clusters = determine_k(metrics)
labels = get_labels(people, num_clusters)
clusters = get_clusters(num_clusters, people, labels)

for person in clusters [0]:
	print(person)