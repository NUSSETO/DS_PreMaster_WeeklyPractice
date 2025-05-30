# Data Cleaning Review
I use the **Data Cleaning** course on Kaggle to review.

---

# Missing Values

There are two main reasons why datas were missing :
- They didn't exist in the first place
- They weren't recorded

Better figure it out before handling the missing values, 
because it makes no sense to add values if there shouldn't be.

To handle missing values, you can either :
- Drop it (I don't want to deal with it)
- Fill it (and try to make sense out of it)

Use '.dropna()' to drop any **rows(axis = 0, default)**/**cols(axis = 1)** that contain any missing value.

Use '.fillna()' to fill in values. Here are some command that might come it handy :
- **method = 'bfill'** : backward fill, use the value that comes after the missing value to fill in
- **method = 'ffill'** : forward fill, use the value that comes before the missing value to fill in
- Or just any thing else you want to fill in

---

# Transforming datas

**Scaling** means you transform your data to fit in a specific range.

**Normalization** means you normalize your data. Simple as that. But you can have various ways to normalize.

---

# Extra Stuff

fig, ax = plt.subplots(1, 2, figsize = (15, 3)) means you have a plot that contains 1 row and 2 cols.
'ax' is to tell where to put your plot. In this situation, you can use :
sns.any_plot_funtion(your_data_here, ax = ax[0]) to specify put your plot on the left.
And of course, if you have 2 rows, use ax = ax[1, 1] or somthing like that.

**Box-cox** (a way to normalize) only takes positive values.
