# Hypothesis Testing

We can either **Reject hypothesis** or **fail to reject hypothesis**.
(Since we cannot easily say the hypothesis is correct, the best we can do is **fail to** reject the hypothesis.)

The **primary hypothesis** is usaully the **null hypothesis**.

**Null Hypothesis (H₀)** is the hypothesis that there is no difference between groups.
(Since it will be easier to see if there is any difference than how much difference.)

**Alternative Hypothesis (H₁)** is usaully the **opposite** of null hypothesis.
(But it's just any hypothesis that contradicts null hypothesis.)

**p-values**  is the probability of observed results happen assuming **null hypothesis** holds.
(That is, when p-values is small, we are more likely to reject the null hypothesis, normally it's set to 0.05.)
(Since if the null hypothesis is **True**, p-values shouldn't be small, but the results say otherwise, which means the null hypothesis is **False**)

We can only reject or fail to reject the **null hypothesis**.
(Again, we don't know if our alternative hypothesis is correct or not, there could be many alternative hypotheses)

P-values only tell if there is any differnece, not how much.

---

Getting a small P-values (suggesting we should reject null hypothesis) when null hypothesis is true is called **False Positive** or **Type I error**.

Getting a huge P-values (suggesting we fail to reject null hypothesis) when null hypothesis is false is called **False Negative** ot **Type II error**.

---

# T-Test : Setosa vs Versicolor Petal Length

### T Test:
Assuming X and Y are independent and normally distributed with a common variance, t-test helps us to determine whether X and Y have the same means.

### Hypotheses:
- **Null Hypothesis (H₀):** There is no difference in petal length between Setosa and Versicolor.
- **Alternative Hypothesis (H₁):** There is a difference in petal length between Setosa and Versicolor.

### Test Results:
- **T-statistic:** -39.493
- **P-value:** < 0.001

### Interpretation:
The p-value is extremely small (effectively 0), 
which means the observed difference in petal length is **very unlikely** under the assumption of the null hypothesis.  
Therefore, we **reject H₀** and conclude that **Setosa and Versicolor have different petal lengths**.

The large value of the t-statistic also indicates that the difference between the group means is much larger than expected.
