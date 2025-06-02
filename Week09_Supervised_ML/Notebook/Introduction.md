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
- Decision Tree : Basically a series of YES/NO questions.
- Random forests : Basically a bunch of decision trees, and giving ouputs based on the majority of the outputs of the decision trees.

**Regression** outputs continuous numeric value. 
Often used models included :
- Linear regression : Creating a linear relationship between inputs and outputs while trying to minimize the SSE.
- (Somehow I only got one, weird.)

There are some algorithms can be used for both purposes :
- K Nearest Neighbors (KNN) : Giving ouput based on its K nearest neighbors. So it can be the average value of or the same category as its neignbors.

---

## Linear Regression

Linear regression is used to predict numeric value based on one or multiple inputs by fitting a **straight line (or hyperplane)** that best suits the relationship.

### One feature
y = \beta_0 + \beta_1 x + \varepsilon
