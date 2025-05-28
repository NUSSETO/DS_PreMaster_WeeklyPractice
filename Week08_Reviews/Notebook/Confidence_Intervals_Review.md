# Confidence Interval

**Population data** represents **all** the data in the datasets, the **mean**, **SD**, etc. of it would be called **population parameters** (depending on what distribution it follows).

But we don't usually have the population data, so instead we **estimate** the population parameters by **sampling** from the datasets.
And with **confidence interval** (and p-value of course), we can know how confident we should be about our **estimate**.

**Confidence Interval** means how likely the **population parameters** (90%, 95%, 99%, etc.) is within the interval, based on our sample.
In other words, the probability of **population parameters** that falls outside of the interval would be very low, which implies **low p-values**.

---

# Somthing I learnt while coding

np.random.normal(loc = 170, scale = 10, size = 10000) means randomly generate normal distribution with 10000 datas using mean = 170, SD = 10.
Yes, loc = location = mean, scale = SD, it's math.

plt.hist(population, bins = 30, edgecolor = 'black', alpha = 0.7), where **bins** = 30 means the graph has 30 bars. **alpha** stands for transparency of the bars.

**for _ in range(1000):** means repeat the command for 10000 times and I don't care about the variables.

np.random.choice(population, size = 100, **replace = True**), note that replace is set to True by default.

**axvline** stands for AXis Vertical LINE.
