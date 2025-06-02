# Introduction

## What does "Supervised" mean ?

In supervised ML, we will have:
- A set of features (input variables) → X
- A target label (the thing we want to predict) → y
We show the model many (X, y) pairs so it can learn a rule to map inputs to the correct outputs.

In contrast, **Unsupervised ML** means the model is given datas without such labels, and needs to try finding hidden patterns.
(Since we don't give any intervention, hence the name "unsupervised".)

---

## What kinds of "Supervised ML" are there ?

**Classification** outputs discrete class label.
Often used models included :
- Logistic regression : Creating a **Sigmoid Function** to the datas, and labeling the outputs based on given threshold.
- Support Vector Machine (SVM) : Creating a **Decision Boundary** with the largeest **margin**, and labeling the ouputs based on where the datas fall relative to the boundary. Note that this algorithm can also be used for **regression** purpose, but I don't know how it works.

**Regression** outputs continuous numeric value. 
Often used models included :
- Linear regression : Creating a linear relationship between inputs and outputs while trying to minimize the SSE.
- (Somehow I only got one, weird.)

There are some algorithms can be used for both purposes :
- K Nearest Neighbors (KNN) : Giving ouput based on its K nearest neighbors. So it can be the average value of or the same category as its neignbors.
- Decision Tree : Basically a series of YES/NO questions.
- Random forests : Basically a bunch of decision trees, and giving ouputs based on the majority of the outputs of the decision trees.

---

## Linear Regression

**Linear regression** is used to predict **numeric values** based on one or multiple input features by fitting a **straight line (or hyperplane)** that best suits the relationship. The model learns by minimizing the Sum of Squared Error (SSE).

We can use MAE, MSE or RMSE. to determine how well the model performs.

**Pros** : Simple, fast, easy to debug, train and interpret, also works well with few features
**Cons** : Assumes linearity, sensitive to outliers and strugles with complex data

---

## Decision Tree

**Decision Tree** is used to predict either **categorical labels** or **numeric values** by learning a sequence of yes/no questions based on feature values. Each internal node represents a decision, and each leaf node holds a final prediction.

**Pros** : Easy to interpret, no need to scaling and can handle both numeric and categorical datasets.
**Cons** : Prone to overfitting, unstable with small data changes

---

## K-Nearest Neighbors

**KNN** is used to predict either **categorical labels** or **numeric values** depending on the task.
- For classification, KNN takes the majority vote of neighbors
- For regression, KNN takes the average of neighbors’ values

If K is too small, the model would tend to overfitting (too sensitive to noise). 
If K is too large, the model will be underfitting (too smooth).
Also, odd numbers are used to avoid tie votes.

**Pros** : Simple and intuitive, no training phase and can adapt to complex patterns
**Cons** : Slow with larger datasets, sensitive to irrelevent features and requires feature scaling
