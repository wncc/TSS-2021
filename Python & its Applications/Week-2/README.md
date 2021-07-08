# Welcome to Week 2 of Learner Space's Python and its Applications!

For this week we will look at Applications of Python in Data Analysis fields and will cover various python libraries used for this namely :
* [Numpy](#Numpy)
* [Pandas](#Pandas)
* [Matplotlib](#Matplotlib)
* [Seaborn](#Seaborn)
* [Scikit-learn](#Scikit-learn)
* [Assignment](#Assignment)

Let's get started!

## Numpy
### What is NumPy?
NumPy stands for Numerical Python. One of the most fundamental packages in Python, NumPy is a general-purpose array-processing package.It is a Python library used for working with arrays.It provides high-performance multidimensional array objects and tools to work with the arrays. NumPy is an efficient container of generic multi-dimensional data.
NumPy’s main object is the homogeneous multidimensional array where their dimensions are called axes and the number of axes is called rank. NumPy’s array class is called ndarray aka array.To read more about NumPy head over to this [link](https://numpy.org/doc/stable/user/whatisnumpy.html)

### Installation of Numpy
For installation you can refer [this](https://www.w3schools.com/python/numpy/numpy_getting_started.asp)
Once you are done with the installation part , you can use it by importing it in your applications by adding **import** keyword. 
  
### Getting Started With Numpy

Check this [notebook](https://github.com/wncc/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-2/NumPy.ipynb) to get basic knowledge of Numpy.Relevant links to websites and documentations have been provided in the notebook itself.  




## Pandas
Pandas is an open-source Python package that provides high-performance, easy-to-use data structures and data analysis tools for the labeled data in Python programming language. Pandas stand for **Python Data Analysis Library**.
**When to use?**
Pandas is a perfect tool for data wrangling or munging. It is designed for quick and easy data manipulation, reading, aggregation, and visualization.
Pandas take data in a CSV or TSV file or a SQL database and create a Python object with rows and columns called a data frame. The data frame is very similar to a table in statistical software, say Excel or SPSS.

### What can you do with Pandas?
* Indexing, manipulating, renaming, sorting, merging data frame
* Update, Add, Delete columns from a data frame
* Impute missing files, handle missing data or NANs
* Plot data with histogram or box plot

### Getting Started With Pandas

Check this [notebook](https://github.com/wncc/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-2/Pandas.ipynb) to get basic knowledge of Pandas .Relevant links to websites and documentations have been provided in the notebook itself.  




## Matplotlib
Matplotlib is a data visualization library and 2-D plotting library of Python.It is a close resemblance to MATLAB embedded in Python programming language.
Histogram, bar plots, scatter plots, area plot to pie plot, Matplotlib can depict a wide range of visualizations. With a bit of effort and tint of visualization capabilities, with Matplotlib, you can create just any visualizations.
Matplotlib also facilitates labels, grids, legends, and some more formatting entities with Matplotlib. Basically, everything that can be drawn!

### Installation of Matplotlib
For installation you can refer [this](https://www.w3schools.com/python/matplotlib_getting_started.asp)
Once you are done with the installation part , you can use it by importing it in your applications by adding **import** keyword.

### Getting Started With Matplotlib

Check this [notebook](https://github.com/wncc/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-2/Matplotlib.ipynb) to get basic knowledge of Pandas .Relevant links to websites and documentations have been provided in the notebook itself.  

 
 
 
## Seaborn
Check out [this](https://www.w3schools.com/python/numpy/numpy_random_seaborn.asp) or [this](https://www.datacamp.com/community/tutorials/seaborn-python-tutorial).
You can also look at [Seaborn documenation](http://seaborn.pydata.org/introduction.html) to know more about Seaborn.




## Scikit-learn

Scikit-learn is a free software library for Machine Learning coding primarily in the Python programming language.Scikit-learn is built on top of other Python libraries like NumPy, SciPy,  Matplotlib, Pandas, etc. and so it provides full interoperability with these libraries.You can implement various Supervised and Unsupervised Machine learning models on Scikit-learn like Classification, Regression, Support Vector Machines, Random Forests, Nearest Neighbors, Naive Bayes, Decision Trees, Clustering, etc. with Scikit-learn. 

### Components of scikit-learn
Scikit-learn comes loaded with a lot of features. Here are a few of them to help you understand the spread:
* **Supervised learning algorithms**: Think of any supervised machine learning algorithm you might have heard about and there is a very high chance that it is part of scikit-learn. Starting from Generalized linear models (e.g Linear Regression), Support Vector Machines (SVM), Decision Trees to Bayesian methods – all of them are part of scikit-learn toolbox.
* **Cross-validation**: There are various methods to check the accuracy of supervised models on unseen data using sklearn.
* **Unsupervised learning algorithms**: Again there is a large spread of machine learning algorithms in the offering – starting from clustering, factor analysis, principal    component analysis to unsupervised neural networks.
* **Feature extraction**: Scikit-learn for extracting features from images and text

Check out [this documentation](https://scikit-learn.org/stable/) to get a deeper understanding of deploying it in machine learning, pre-processing, cross-validation and visualization algorithms.

## Applications in Finance!

Now, you can begin looking at some of the applications of Python. Starting with its application in Finance and Specifically in
Automated-Trading in Stock Markets.

If you don't know anything about the Stock Market, you may get a minimal Introduction from [here](https://www.youtube.com/watch?v=bl797s8u0QQ&t=463s).

You just need to know about how prices fluctuate in such Markets and how that can be used to generate profits.

This Process of buying at low prices and selling them at higher ones could be automated to yield astronomical profits!
This is what's known as Algorithmic Trading!
Some people who effiectively automated Cryptocurrency-Trading made upto 3000% Profits, and even though that was partly fueled by the
Cryptocurrency frenzy that took over the world, In general even not-so-complex Stock Market Strategies give upto 10% cumulative Annual Profits in
certain markets.

One of the easiest Strategies in Algorithmic Trading is that of Mean Reversion.

Mean reversion in stock price is the assumption that the price will tend to move back to the average price over time. Mean reversion trading often refers to counter-trend or reversal trading.
Thus, If any stock price is currently below its average, then we should buy it, as there is every chance that it is having some down-time and will rise in coming times.

Similarly if some Stock Price is above its Average, then that indicates, its time to sell.

You may look at a naive implementation of Mean Reversion in [Country Equity Indices](https://en.wikipedia.org/wiki/Stock_market_index) [here](https://www.quantconnect.com/tutorials/strategy-library/mean-reversion-effect-in-country-equity-indexes).

## Assignment

DISCLAIMER: This week's assignments would be a great leap more difficult than last week's. If you aren't able to complete them just as easily as last week's, do not lose hope. You can always ask for help in the Telegram channel. We are making two separate versions of the assignment for that purpose!

The first (**EASY**) version would have a basic coding architecture ready for you, and you'll only have to implement various functions (we'll also tell you what these functions are supposed to do!)

For the second (**HARD**) version, We will just give you the data and control flow of the Program and expect you to do the rest on your own!

Choose according to your comfort level!

If you plan to go for the second version then don't look at the first at all, as that would defeat the purpose of pushing yourself!

If you look at the Compulsory Exercises and find even their **HARD** versions to be fairly easy for you, then you may solve only the Optional Assignments and we'll still be considering you to pass the assignment.

Please, Attempt the first Compulsory Exercise before proce

**1)** There's something which goes by the name of Momentum Anamoly in Trading, which says that what was strongly going up in the near past will probably continue to go up shortly. Stocks which outperform peers on 3-12 month period tend to perform well also in the future.

You may read more about Momentum from [here](https://quantpedia.com/strategies/momentum-factor-effect-in-stocks/).

[EASY](https://github.com/wncc/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-2/Momentum.ipynb)

[HARD](https://github.com/wncc/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-2/MomentumH.ipynb)


**2)** You should get familiar with [Correlation](https://www.investopedia.com/ask/answers/032515/what-does-it-mean-if-correlation-coefficient-positive-negative-or-zero.asp) and its significance in Trading.

Next, Read up about [Paired Switching](https://quantpedia.com/strategies/paired-switching/).

The basic idea behind Paired Switching is to select two stocks which are negatively co-related, so that if one falls then the other should be rising shortly afterwards and vice versa.


[EASY](https://github.com/wncc/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-2/Pairs.ipynb)

[HARD](https://github.com/wncc/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-2/PairsH.ipynb)

**(OPTIONAL)** 

Implementing a Trading Strategy based on Naive Bayes Model!

Get to know about the Naive Bayes' Model from [here](https://towardsdatascience.com/all-about-naive-bayes-8e13cef044cf) and [here](https://en.wikipedia.org/wiki/Naive_Bayes_classifier) (You might want to know about Bernoulli's Naive Bayes Classifier in particular).
Get to know about various indicators used to judge where the market/prices are going. [RSI](https://blog.quantinsti.com/rsi-indicator/)(Relative Strength Index) and [Stoch](https://blog.quantinsti.com/stochastic-oscillator/)(Stochastic Oscillator) are great indicators, you may or may not stop just at them.

Next you can use RSI, Stoch (and other Indicators of your choice) and implement a Bernoulli Naive Bayes Model to predict next day's returns and then use that to trade.

You should also use matplotlib/Seaborn to plot these results as well!

**HINT** : Try to get to know about pre-defined functions which can help you, from sklearn library!
