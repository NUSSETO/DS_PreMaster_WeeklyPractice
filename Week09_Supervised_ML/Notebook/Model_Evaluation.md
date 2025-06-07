## Core Metrics

- Accuracy : TP + TN / All datas
  - It's used to measure **the total correct predictions**
  - If the counts difference between positive and negative is large, this could be misleading.
- Precision : TP / All predicted positives (TP + FP)
  - It's used to measure how well the model performs with predicting positive cases.
- Recall : TP / All actual positives (TP + FN)
  - It's used to measure how well the model performs with not missing positive cases.
- F1 - Score : 2 * (Precision * Recall) / (Precision + Recall)
  - It's used to balance both concerns : being accurate and not missing. 
  - It's quite handy when you need 1 score to consider both FP and FN.
