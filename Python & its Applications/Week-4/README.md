# Welcome to Week 4 of Learner Space's Python and its Applications!

For this week we will be seeing how to build basic(and slightly advanced!) Search engines in Python :

We will start by learning more about Web Scraping, as building Search Engines involves extensive use of these tools.

We will be covering BeautifulSoup in considerable depth (a bit beyond what's required to build Search Engines), as why to stop oneself from learning, when you have found some motivation to do so!

## BeautifulSoup

Beautiful Soup is a Python package for parsing HTML and XML documents (including having malformed markup, i.e. non-closed tags, so named after tag soup). It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for [web scraping](https://en.wikipedia.org/wiki/Web_scraping).
All one needs to know to use this really cool library are the bare basics of python (or any programming language for that matter) and the ability to recognize patterns in an HMTL code. Proficiency in CSS, HTML and web development is not a must.

### Installation

To install Beautifulsoup on Windows, Linux, or any operating system, one would need **pip** package.Refer [this](https://www.geeksforgeeks.org/beautifulsoup-installation-python/) article for installation.

### How to Use Beautifulsoup?

The best way to understand the use of this library would be to follow an example .Head over to this [website](https://www.geeksforgeeks.org/how-to-scrape-websites-with-beautifulsoup-and-python/) which demonstrates how to use it.

#### Other useful Resources 

Here are the links of some other useful resources on Beautifulsoup:

* [This](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) is the official documentation for the library and contains all information on all the member functions and how to use them best.

* [This](https://automatetheboringstuff.com/chapter11/) is another useful resource and can be easily followed even by someone with no previous knowledge about parsing. 


Now, we could begin looking into building Search Engines. We will start by looking into a basic search engine built in Python :

## Term Frequency - Inverse Document Frequency based Search

You can head to [this](https://github.com/wncc/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-4/FirstEngine.ipynb) notebook and explore what is TF-IDF and how its used for building a basic search engine. Over-the-hood, we are simply getting statistical measures of matchings of words, getting these results as vectors and then considering the cosine-similarity between them as a measure of optimality in searching.

## Towards greater Sophistication : BM25

TF-IDF used to be the most used Search Algorithm by a lot of big firms like Udemy, Slack etc. as recently as 2016, but after that BM25 took over. Head to [this notebook](https://github.com/wncc/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-4/BM25.ipynb) and explore the algorithm in action for yourself! You will need a certain file containing the Data which shall be parsed, you may find it [here](https://drive.google.com/file/d/1pJFPa5772JiXWxZ9pGpwNbO6D0BBCEXZ/view?usp=sharing). Make sure you download it and upload it to your kernel while playing around with the notebook.

# Assignment

For this Week's Assignment, you shall build test Google's own Algorithm : **PageRank** (The 'Page' doesn't stand for webpages, but rather for its author and Google's co-founder, Larry Page!)

When search engines like Google display search results, they do so by placing more “important” and higher-quality pages higher in the search results than less important pages. But how does the search engine know which pages are more important than other pages?

One heuristic might be that an “important” page is one that many other pages link to, since it’s reasonable to imagine that more sites will link to a higher-quality webpage than a lower-quality webpage. We could therefore imagine a system where each page is given a rank according to the number of incoming links it has from other pages, and higher ranks would signal higher importance.

But this definition isn’t perfect: if someone wants to make their page seem more important, then under this system, they could simply create many other pages that link to their desired page to artificially inflate its rank.

For that reason, In PageRank’s algorithm, a website is more important if it is linked to by other important websites, and links from less important websites have their links weighted less. This definition seems a bit circular, but it turns out that there are multiple strategies for calculating these rankings.

## Random Surfer Model

One way to think about PageRank is with the random surfer model, which considers the behavior of a hypothetical surfer on the internet who clicks on links at random. Consider the corpus of web pages below, where an arrow between two pages indicates a link from one page to another.

![Corpus](https://github.com/thevaliantthird/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-4/images/1.png)

The random surfer model imagines a surfer who starts with a web page at random, and then randomly chooses links to follow. If the surfer is on Page 2, for example, they would randomly choose between Page 1 and Page 3 to visit next (duplicate links on the same page are treated as a single link, and links from a page to itself are ignored as well). If they chose Page 3, the surfer would then randomly choose between Page 2 and Page 4 to visit next.

A page’s PageRank, then, can be described as the probability that a random surfer is on that page at any given time. After all, if there are more links to a particular page, then it’s more likely that a random surfer will end up on that page. Moreover, a link from a more important site is more likely to be clicked on than a link from a less important site that fewer pages link to, so this model handles weighting links by their importance as well.

One way to interpret this model is as a [Markov Chain](https://setosa.io/ev/markov-chains/), where each page represents a state, and each page has a transition model that chooses among its links at random. At each time step, the state switches to one of the pages linked to by the current state.

By sampling states randomly from the Markov Chain, we can get an estimate for each page’s PageRank. We can start by choosing a page at random, then keep following links at random, keeping track of how many times we’ve visited each page. After we’ve gathered all of our samples (based on a number we choose in advance), the proportion of the time we were on each page might be an estimate for that page’s rank.

However, this definition of PageRank proves slightly problematic, if we consider a network of pages like the one below.

![Disconnected Network](https://github.com/thevaliantthird/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-4/images/2.png)

Imagine we randomly started by sampling Page 5. We’d then have no choice but to go to Page 6, and then no choice but to go to Page 5 after that, and then Page 6 again, and so forth. We’d end up with an estimate of 0.5 for the PageRank for Pages 5 and 6, and an estimate of 0 for the PageRank of all the remaining pages, since we spent all our time on Pages 5 and 6 and never visited any of the other pages.

To ensure we can always get to somewhere else in the corpus of web pages, we’ll introduce to our model a damping factor `d`. With probability `d` (where `d` is usually set around `0.85`), the random surfer will choose from one of the links on the current page at random. But otherwise (with probability `1 - d`), the random surfer chooses one out of all of the pages in the corpus at random (including the one they are currently on).

Our random surfer now starts by choosing a page at random, and then, for each additional sample we’d like to generate, chooses a link from the current page at random with probability `d`, and chooses any page at random with probability `1 - d`. If we keep track of how many times each page has shown up as a sample, we can treat the proportion of states that were on a given page as its PageRank.

## Iterative Algorithm

We can also define a page’s PageRank using a recursive mathematical expression. Let `PR(p)` be the PageRank of a given page p: the probability that a random surfer ends up on that page. How do we define `PR(p)`? Well, we know there are two ways that a random surfer could end up on the page:

1. With probability `1 - d`, the surfer chose a page at random and ended up on page `p`.
2. With probability `d`, the surfer followed a link from a page `i` to page `p`.

The first condition is fairly straightforward to express mathematically: it’s `1 - d` divided by `N`, where `N` is the total number of pages across the entire corpus. This is because the `1 - d` probability of choosing a page at random is split evenly among all `N` possible pages.

For the second condition, we need to consider each possible page `i` that links to page `p`. For each of those incoming pages, let `NumLinks(i)` be the number of links on page `i`. Each page `i` that links to p has its own PageRank, `PR(i)`, representing the probability that we are on page `i` at any given time. And since from page `i` we travel to any of that page’s links with equal probability, we divide `PR(i)` by the number of links `NumLinks(i)` to get the probability that we were on page `i` and chose the link to page `p`.

This gives us the following definition for the PageRank for a page `p`.

![Formula](https://github.com/thevaliantthird/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-4/images/3.png)

In this formula, `d` is the damping factor, `N` is the total number of pages in the corpus, `i` ranges over all pages that link to page `p`, and `NumLinks(i)` is the number of links present on page `i`.

How would we go about calculating PageRank values for each page, then? We can do so via iteration: start by assuming the PageRank of every page is `1 / N`(i.e., equally likely to be on any page). Then, use the above formula to calculate new PageRank values for each page, based on the previous PageRank values. If we keep repeating this process, calculating a new set of PageRank values for each page based on the previous set of PageRank values, eventually the PageRank values will converge (i.e., not change by more than a small threshold with each iteration).

Phewwww....That was a lot!

Now you can head over to [this notebook](https://github.com/wncc/TSS-2021/blob/main/Python%20%26%20its%20Applications/Week-4/PageRank.ipynb) . You will need to download the three folders named `corpus0`, `corpus1` & `corpus2`, and store them in the same directory from where you run this notebook(/upload them to the kernel where you're running it!), in order to see your code in action.

### Optional Assignment

Try to integrate PageRank and either of BM25/TF-IDF to construct a fully functional Search Engine, which works by making use of Web Scraping and not already collected Data. 
