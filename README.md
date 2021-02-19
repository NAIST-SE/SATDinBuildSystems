# Research Artifact: Characterizing and Mitigating Self-Admitted Build Debt

https://github.com/NAIST-SE/SABD

This is a research artifact for the paper: **Characterizing and Mitigating Self-Admitted Build Debt**. This artifact is a repository consisting of our 500 SABD comments dataset and 'ready-to-be-addressed' SABD comments. The purposes of this artifact are to enable researchers to reuse the dataset for further software engineering research.


## Abstract
Technical Debt is a metaphor used to describe the situation in which long-term code quality is traded for short-term goals in software projects.
In recent years, the concept of self-admitted technical debt (SATD) was proposed, which focuses on debt that is intentionally introduced and described by developers.
Although prior work has made important observations about admitted technical debt in source code, little is known about SATD in build systems. 
In this paper, we coin the term Self-Admitted Build Debt (SABD) and 
conduct a qualitative analysis of 500 SABD extracted from the Maven build system of 300 projects.
Our results show that limitations in tools and libraries, and complexities of dependency management are the most frequent causes, accounting for 49% and 23% of the comments.
We also find that developers often document SABD as issues to be fixed later. 
To automate the detection of SATD rationale, we train classifiers to label comments according to the surrounding document content. 
The classifier performance is promising, achieving an F1-score of 0.67--0.75. 
Finally, we were able to identify 43% of the ready-to-be-addressed SABD, with 56% of them being quickly resolved after developers were being made aware.
Our work presents the first step towards understanding technical debt in build systems and opens up avenues for future work such as tool support and awareness for both researchers and build system maintainers.


## Contents
* `Dataset` - a directory of the dataset
	* `500_SABD_Comments.csv` - results of RQ1: open coding and card sorting SABD comments in Maven repositories.
		* `Index` - a numbered list.
		* `Comment Location` - where the SABD comment store at in the repository.
		* `Comment` - the content of the SABD comment.
		* `Keywords` - the set of keywords which are used to extract SABD comment.
		* `Location` - where the SABD comment store at in the build file.
		* `Reason` - why the SABD occure in the build file.
		* `Purpose` - why the developer left the SABD comment in the build file.
	* `ready-to-be-addressed_SABD_Comments.csv` - results of RQ2: identification for 'ready-to-be-addressed' SABD comments in 500 SABD comments.
		* `Index` - a numbered list.
		* `Comment Location` - where the SABD comment store at in the repository.
		* `Comment` - the content of the SABD comment.
		* `Keywords` - the set of keywords which are used to extract SABD comment.
		* `Location` - where the SABD comment store at in the build file.
		* `Reason` - why the SABD occure in the build file.
		* `Purpose` - why the developer left the SABD comment in the build file.
		* `URL1` - the first hyperlink in the SABD comment.
		* `URL2` - the second hyperlink in the SABD comment.
		* `Submitting approach` - the approach to report SABD comment to the developers.
		* `Pull request/Issue link` - the hyperlink where we report SABD comment.
		* `Status` - the current status of the pull request or issue.
	* `keywords_list.txt` - our adopated list of SABD keywords which are merged from [Huang et al.](https://doi.org/10.1007/s10664-017-9522-4) and [Potdar and Shihab](10.1109/ICSME.2014.31).
	* `Revision_list.csv` - the list of HEAD revisions extract from DP1.
* `Scripts` - a directory of Scripts.
	* `README.md` - a readme file for Scripts directory.
	* `parallel_categories_diagram.ipynb` - the parallel categories diagram among location, reason, and purpose.
	* `identify_SABD_comments.py` - the script which is used to detect SABD comments.
* `POM_files_used_in_paper` - a directory of POM files that used in paper. Filename represents the link to orginal POM file shown in the paper.
* `LICENSE` - [CC0 1.0 Universal.](https://creativecommons.org/publicdomain/zero/1.0/)
* `README.md` - this file.
## Authors
- Tao Xiao
- [Dong Wang](https://dong-w.github.io/)
- [Shane McIntosh](http://shanemcintosh.org/)
- [Hideaki Hata](https://hideakihata.github.io/)
- [Raula Gaikovina Kula](https://raux.github.io/)
- [Takashi Ishio](https://takashi-ishio.github.io/)
- [Kenichi Matsumoto](https://matsumotokenichi.github.io/)
