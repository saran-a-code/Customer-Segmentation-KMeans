# ==========================================
# Customer Segmentation using K-Means
# ==========================================

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans

# ------------------------------------------
# Step 1: Load Dataset
# ------------------------------------------

data = pd.read_csv("dataset/Mall_Customers.csv")

print("\nFirst 5 Rows")
print(data.head())

# ------------------------------------------
# Step 2: Dataset Information
# ------------------------------------------

print("\nDataset Information")
print(data.info())

print("\nStatistical Summary")
print(data.describe())

print("\nMissing Values")
print(data.isnull().sum())

# ------------------------------------------
# Step 3: Data Visualization
# ------------------------------------------

# Age Distribution
plt.figure(figsize=(6,4))
sns.histplot(data["Age"], bins=20, color="blue")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# Income Distribution
plt.figure(figsize=(6,4))
sns.histplot(data["Annual Income (k$)"], bins=20, color="green")
plt.title("Annual Income Distribution")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Count")
plt.show()

# Spending Score Distribution
plt.figure(figsize=(6,4))
sns.histplot(data["Spending Score (1-100)"], bins=20, color="orange")
plt.title("Spending Score Distribution")
plt.xlabel("Spending Score")
plt.ylabel("Count")
plt.show()

# Scatter Plot
plt.figure(figsize=(8,6))
sns.scatterplot(
    x="Annual Income (k$)",
    y="Spending Score (1-100)",
    data=data
)
plt.title("Income vs Spending Score")
plt.show()

# ------------------------------------------
# Step 4: Select Features
# ------------------------------------------

# We use only Income and Spending Score
X = data.iloc[:, [3,4]].values

# ------------------------------------------
# Step 5: Find Optimal Clusters
# (Elbow Method)
# ------------------------------------------

wcss = []

for i in range(1,11):

    kmeans = KMeans(
        n_clusters=i,
        init='k-means++',
        random_state=42,
        n_init=10
    )

    kmeans.fit(X)

    wcss.append(kmeans.inertia_)

# Plot Elbow Graph
plt.figure(figsize=(8,5))
plt.plot(range(1,11), wcss, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()

# ------------------------------------------
# Step 6: Train K-Means Model
# ------------------------------------------

kmeans = KMeans(
    n_clusters=5,
    init='k-means++',
    random_state=42,
    n_init=10
)

# Predict cluster labels
y_kmeans = kmeans.fit_predict(X)

print("\nCluster Labels")
print(y_kmeans)

# ------------------------------------------
# Step 7: Visualize Clusters
# ------------------------------------------

plt.figure(figsize=(10,7))

plt.scatter(
    X[y_kmeans==0,0],
    X[y_kmeans==0,1],
    s=100,
    c='red',
    label='Cluster 1'
)

plt.scatter(
    X[y_kmeans==1,0],
    X[y_kmeans==1,1],
    s=100,
    c='blue',
    label='Cluster 2'
)

plt.scatter(
    X[y_kmeans==2,0],
    X[y_kmeans==2,1],
    s=100,
    c='green',
    label='Cluster 3'
)

plt.scatter(
    X[y_kmeans==3,0],
    X[y_kmeans==3,1],
    s=100,
    c='cyan',
    label='Cluster 4'
)

plt.scatter(
    X[y_kmeans==4,0],
    X[y_kmeans==4,1],
    s=100,
    c='magenta',
    label='Cluster 5'
)

# Plot Centroids
plt.scatter(
    kmeans.cluster_centers_[:,0],
    kmeans.cluster_centers_[:,1],
    s=300,
    c='yellow',
    label='Centroids',
    marker='*'
)

plt.title("Customer Segmentation using K-Means")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.legend()
plt.grid(True)

plt.show()

# ------------------------------------------
# Step 8: Add Cluster Column
# ------------------------------------------

data["Cluster"] = y_kmeans

print("\nCustomers with Cluster Labels")
print(data.head())

# ------------------------------------------
# Step 9: Save Output
# ------------------------------------------

data.to_csv("Customer_Segmentation_Output.csv", index=False)

print("\nProject Completed Successfully!")
print("Output saved as Customer_Segmentation_Output.csv")