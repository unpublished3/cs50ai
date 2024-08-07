import os
import random
import re
import copy
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(link for link in pages[filename] if link in pages)

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    distribution = {}
    for page_ in corpus:
        if len(corpus[page]) == 0:
            distribution[page_] = 1 / len(corpus)
        else:
            distribution[page_] = (1 - damping_factor) / len(corpus)

        if page_ in corpus[page]:
            distribution[page_] += damping_factor / len(corpus[page])

    return distribution


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    page_ranks = {}
    page = random.choice(list(corpus.keys()))
    for _ in range(n):
        if page not in page_ranks:
            page_ranks[page] = 0

        page_ranks[page] += 1 / n

        model = transition_model(corpus, page, damping_factor)
        pages = list(model.keys())
        probabilites = list(model.values())

        page = random.choices(pages, weights=probabilites, k=1)[0]

    return page_ranks


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    old_ranks = {}
    page_ranks = {}
    c = (1 - damping_factor) / len(corpus)

    for page in corpus:
        old_ranks[page] = 1 / len(corpus)
        page_ranks[page] = 1 / len(corpus)

        if not len(corpus[page]):
            for page_ in corpus:
                corpus[page].add(page_)

    back_links = {}
    for page in corpus:
        back_links[page] = set()
        for page2 in corpus:
            if page in corpus[page2]:
                back_links[page].add(page2)

    while True:
        for page in corpus:
            rank = 0

            for page2 in back_links[page]:
                rank += old_ranks[page2] / len(corpus[page2])
            page_ranks[page] = round(damping_factor * rank + c, 5)

        if not converged(old_ranks, page_ranks):
            old_ranks = copy.deepcopy(page_ranks)
        else:
            break

    return page_ranks


def converged(old_ranks, new_ranks):
    for page in old_ranks.keys():
        if abs(old_ranks[page] - new_ranks[page]) >= 0.001:
            return False

    return True


if __name__ == "__main__":
    main()
