# 🛍️ Customer Segmentation using K-Means Clustering

## 📌 Project Overview

Customer Segmentation is an **Unsupervised Machine Learning** technique used to group customers based on similar characteristics. In this project, the **K-Means Clustering** algorithm is applied to the Mall Customers dataset to identify different customer groups based on **Annual Income** and **Spending Score**.

This segmentation helps businesses understand customer behavior and create personalized marketing strategies, improving customer satisfaction and increasing sales.

---

## 🎯 Objectives

* Understand the concept of Unsupervised Learning.
* Perform Exploratory Data Analysis (EDA).
* Apply the K-Means Clustering algorithm.
* Determine the optimal number of clusters using the Elbow Method.
* Visualize customer segments.
* Analyze customer groups for business decision-making.

---

## 📂 Dataset

**Dataset:** Mall Customers Dataset

### Features

| Column                 | Description                               |
| ---------------------- | ----------------------------------------- |
| CustomerID             | Unique ID of each customer                |
| Gender                 | Male/Female                               |
| Age                    | Customer's age                            |
| Annual Income (k$)     | Annual income in thousand dollars         |
| Spending Score (1-100) | Score assigned based on spending behavior |

For clustering, only the following features were used:

* Annual Income (k$)
* Spending Score (1-100)

---

## 🛠️ Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* K-Means Clustering

---

## 📊 Exploratory Data Analysis (EDA)

The following visualizations were created:

* Age Distribution
* Annual Income Distribution
* Spending Score Distribution
* Annual Income vs Spending Score Scatter Plot

These visualizations help in understanding customer demographics and spending behavior.

---

## 🤖 Machine Learning Algorithm

### K-Means Clustering

K-Means is an Unsupervised Learning algorithm that groups similar data points into clusters.

Steps followed:

1. Load the dataset.
2. Explore and visualize the data.
3. Select Annual Income and Spending Score as features.
4. Apply the Elbow Method to determine the optimal number of clusters.
5. Train the K-Means model.
6. Predict customer clusters.
7. Visualize the clustered customers and centroids.

---

## 📈 Elbow Method

The Elbow Method was used to determine the optimal number of clusters by calculating the **Within Cluster Sum of Squares (WCSS)** for different values of K.

The elbow point indicated that **5 clusters** provide a good balance between model simplicity and clustering performance.

---

## 📸 Output

The project generates:

* Customer Distribution Graphs
* Elbow Method Graph
* Cluster Visualization
* Cluster Centroids
* Customer_Segmentation_Output.csv

---

## 📁 Project Structure

```text
Customer-Segmentation-KMeans/
│
├── dataset/
│   └── Mall_Customers.csv
│
├── images/
│
├── customer_segmentation.py
├── Customer_Segmentation_Output.csv
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/your-username/customer-segmentation-kmeans.git
```

2. Navigate to the project folder

```bash
cd customer-segmentation-kmeans
```

3. Install the required libraries

```bash
pip install -r requirements.txt
```

4. Run the project

```bash
python customer_segmentation.py
```

---

## 📌 Results

* Successfully grouped customers into **5 distinct clusters** using the K-Means algorithm.
* Visualized customer segments based on annual income and spending score.
* Identified different customer categories that can help businesses improve targeted marketing and customer engagement.

---

## 🚀 Future Improvements

* Add Feature Scaling using StandardScaler.
* Calculate Silhouette Score for cluster evaluation.
* Build an interactive Streamlit web application.
* Deploy the application online.
* Experiment with other clustering algorithms such as DBSCAN and Hierarchical Clustering.

---

## 📚 Skills Demonstrated

* Python Programming
* Data Preprocessing
* Exploratory Data Analysis (EDA)
* Data Visualization
* Unsupervised Machine Learning
* K-Means Clustering
* Elbow Method
* Customer Segmentation
* Model Evaluation
* Git & GitHub

---

## 👨‍💻 Author

**Saran A**

* LinkedIn: https://linkedin.com/in/saranaa
* GitHub: https://github.com/saran-a-code

---

## ⭐ If you found this project useful, consider giving it a star on GitHub!
