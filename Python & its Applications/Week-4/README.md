# Welcome to Week 4 of Learner Space's Python and its Applications!

For this week we will be seeing how to build basic(and slightly advanced!) Search engines in Python :

We will start by learning more about Web Scraping, as building Search Engines involves extensive use of these tools.












Now, we could begin looking into building Search Engines. We will start by looking into a basic search engine built in Python :

## Term Frequency - Inverse Document Frequency based Search

**Term Frequency (TF)** is a frequency of term (t) on document (d). The formula looks like this :

![images/0.png](https://github.com/thevaliantthird/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-4/images/0.png)

Beside of that, we can use a log with bases of 10 to calculate the TF, so the number becomes smaller, and the computation process becomes faster. Also, make sure to add one on it because we don’t want log 0 exist.

![images/1.png](https://github.com/thevaliantthird/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-4/images/1.png)


Then, there is the **Inverse Document Frequency (IDF)**. This formula will be used for calculating the rarity of the word in all documents. It will be used as weights for the TF. If a word is frequent, then the IDF will be smaller. In opposite, if the word is less frequent, then the IDF will be larger. The formula looks like this :

![images/2.png](https://github.com/thevaliantthird/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-4/images/2.png)

Recall the TF-IDF, we can see how does it affect the value on each cell. It will remove all the words that are frequently shown in documents but at the same time not important, such as and, or, even, actually, etc. Based on that, we use this as the value on each cell on our matrix.

You can head to [this](https://github.com/wncc/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-4/FirstEngine.ipynb) notebook and explore what is TF-IDF and how its used for building a basic search engine. Over-the-hood, we are simply getting statistical measures of matchings of words, getting these results as vectors and then considering the cosine-similarity between them as a measure of optimality in searching.

## Towards greater Sophistication : BM25

Many firms like Uber, Udemy, Slack, Shopify along with other organisations used TF-IDF until as recently as 2016. After that they shifted to a slightly more sophisticated way : **BM25**, which is still used today.

So what is BM25? It stands for ‘Best match 25’ (the other 24 attempts were clearly not very successful). It was released in 1994 at the third Text Retrieval Conference, yes there really was a conference dedicated to text retrieval…

It is probably best thought of as tf-idf ‘on steroids’, implementing two key refinements:

**Term frequency saturation**. BM25 provides diminishing returns for the number of terms matched against documents. This is fairly intuitive, if you looking to search for a specific term which is very common in documents then there should become a point where the number of occurrences of this term become less useful to the search.

**Document length**. BM25 considers document length in the matching process. Again, this is intuitive; if a shorter article contains the same number of terms that match as a longer article, then the shorter article is likely to be more relevant.

These refinements also introduce two hyper-parameters to adjust the impact of these items on the ranking function. ‘k’ to tune the impact of term saturation and ‘b’ to tune document length.

Bringing this all together, BM25 is calculated as:

![images/3.png](https://github.com/thevaliantthird/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-4/images/3.png)

#Assignment

For this Week's Assignment, you shall build test Google's own Search Algorithm : **PageRank** (The 'Page' doesn't stand for webpages, but rather for its author and Google's co-founder, Larry Page!)

When search engines like Google display search results, they do so by placing more “important” and higher-quality pages higher in the search results than less important pages. But how does the search engine know which pages are more important than other pages?

One heuristic might be that an “important” page is one that many other pages link to, since it’s reasonable to imagine that more sites will link to a higher-quality webpage than a lower-quality webpage. We could therefore imagine a system where each page is given a rank according to the number of incoming links it has from other pages, and higher ranks would signal higher importance.

But this definition isn’t perfect: if someone wants to make their page seem more important, then under this system, they could simply create many other pages that link to their desired page to artificially inflate its rank.

For that reason, In PageRank’s algorithm, a website is more important if it is linked to by other important websites, and links from less important websites have their links weighted less. This definition seems a bit circular, but it turns out that there are multiple strategies for calculating these rankings.

## Random Surfer Model

One way to think about PageRank is with the random surfer model, which considers the behavior of a hypothetical surfer on the internet who clicks on links at random. Consider the corpus of web pages below, where an arrow between two pages indicates a link from one page to another.
