import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
# Import the necessary libraries

# Load the data from the CSV file
data = pd.read_csv('your_data.csv')

# Execute the K-Means algorithm
# Define the number of clusters you want
num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(data)
# Display the cluster centers
print("Cluster Centers:")
print(kmeans.cluster_centers_)
# Display the clustering of the data
print("Cluster Labels:")
print(kmeans.labels_)

# Visualize the results
plt.scatter(data['BMI'], data['MentHlth'], c=kmeans.labels_, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 3], kmeans.cluster_centers_[:, 4], s=300, c='red', marker='x')
plt.xlabel('BMI')
plt.ylabel('MentHlth')
plt.title('K-Means Clustering')
plt.show()


