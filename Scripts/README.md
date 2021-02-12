# This file includs the process for reproducing our analyese.

## Steps
* `Step 1`: We use [Comment Lister](https://github.com/takashi-ishio/CommentLister) tool to Extract comments from Maven reposiyories (DP1).

* `Step 2`: We use identify_SATD_comments.py and keywords_list.txt to identify SABD comments from Maven reporistoryes (DP1).

* `Step 3`: We use parallel_categories_diagram.ipynb to create parallel ctegories diagram for visulization.

* `Step 4`: We use [Ngram classification](https://github.com/rungroj-m/ngram_classification) to build models for automaticly classify SABD comments in aspects of rationals.



