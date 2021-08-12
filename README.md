# Research Artifact: Characterizing and Mitigating Self-Admitted Technical Debt in Build Systems

https://github.com/NAIST-SE/SATDinBuildSystems

This is a research artifact for the paper: **Characterizing and Mitigating Self-Admitted Technical Debt in Build Systems**. This artifact is a repository consisting of raw data, our 500 SATD comments dataset, and 'ready-to-be-addressed' SATD comments, and scripts. The purposes of this artifact are to enable researchers to reuse the dataset for further software engineering research.


## Abstract
Technical Debt is a metaphor used to describe the situation in which long-term software artifact quality is traded for short-term goals in software projects. In recent years, the concept of self-admitted technical debt (SATD) was proposed, which focuses on debt that is intentionally introduced and described by developers. Although prior work has made important observations about admitted technical debt in source code, little is known about SATD in build systems. In this paper, we set out to better understand the characteristics of SATD in build systems. To do so, through a qualitative analysis of 500 SATD comments in the Maven build system of 291 projects, we characterize SATD by location and rationale (reason and purpose). Our results show that limitations in tools and libraries, and complexities of dependency management are the most frequent causes, accounting for 50% and 24% of the comments. We also find that developers of ten document SATD as issues to be fixed later. As a first step towards the automatic detection of SATD rationale, we train classifiers to detect the two most frequently occurring reasons and the four most frequently occurring purposes of SATD in the content of comments in Maven build systems. The classifier performance is promising, achieving an F1-score of 0.71–0.79. Finally, within 16 identified ‘ready-to-be-addressed’ SATD instances, the three SATD submitted by pull requests and the five SATD submitted by issue reports were resolved after developers were made aware. Our work presents the first step towards understanding technical debt in build systems and opens up avenues for future work, such as tool support to track and manage SATD backlogs.

## Contents
* `Dataset` - a directory of the dataset
	* `500_SATD_Comments.csv` - results of RQ1: open coding and card sorting SATD comments in Maven repositories.
		* `Comment Location` - where the SATD comment store at in the repository.
		* `Comment` - the content of the SATD comment.
		* `Keywords` - the set of keywords which are used to extract SATD comment.
		* `Location` - where the SATD comment store at in the build file.
		* `Reason` - why the SATD occure in the build file.
		* `Purpose` - why the developer left the SATD comment in the build file.
	* `ready-to-be-addressed_SATD_Comments.csv` - results of RQ2: identification for 'ready-to-be-addressed' SATD comments in 500 SATD comments.
		* `Index` - a numbered list.
		* `Comment Location` - where the SATD comment store at in the repository.
		* `Comment` - the content of the SATD comment.
		* `Keywords` - the set of keywords which are used to extract SATD comment.
		* `Location` - where the SATD comment store at in the build file.
		* `Reason` - why the SATD occure in the build file.
		* `Purpose` - why the developer left the SATD comment in the build file.
		* `URL1` - the first hyperlink in the SATD comment.
		* `URL2` - the second hyperlink in the SATD comment.
		* `Submitting approach` - the approach to report SATD comment to the developers.
		* `Pull request/Issue link` - the hyperlink where we report SATD comment.
		* `Status` - the current status of the pull request or issue.
	* `keywords_list.txt` - our adopated list of SATD keywords which are merged from [Huang et al.](https://doi.org/10.1007/s10664-017-9522-4) and [Potdar and Shihab](10.1109/ICSME.2014.31).
	* `revision_list.csv` - the list of HEAD revisions extract from DP1.
	* `3out.csv` - the list of repositores ID and name from [Hata et al.](10.1109/ICSE.2019.00123).
	* `result-buildfiles-extended` - dataset shared by [Hata et al.](10.1109/ICSE.2019.00123).
	* `comments_with_no_keywords.csv` - list of Maven comments that are not identified as SATD by the keyword-basedapproach.
	* `384_samples_comments_with_no_keywords.csv` - list of sample Maven comments that are not identified as SATD by the keyword-basedapproach.
* `Scripts` - a directory of Scripts.
	* `README.md` - a readme file for Scripts directory.
	* `parallel_categories_diagram.ipynb` - the parallel categories diagram among location, reason, and purpose.
	* `identify_SATD_comments.py` - the script which is used to detect SATD comments.
* `POM_files_used_in_paper` - a directory of POM files that used in paper. Filename represents the link to orginal POM file shown in the paper.
* `LICENSE` - [CC0 1.0 Universal.](https://creativecommons.org/publicdomain/zero/1.0/)
* `survey.pdf` - survey material for section 6 DEVELOPER FEEDBACK.
* `README.md` - this file.
## Authors
- Tao Xiao
- [Dong Wang](https://dong-w.github.io/)
- [Shane McIntosh](http://shanemcintosh.org/)
- [Hideaki Hata](https://hideakihata.github.io/)
- [Raula Gaikovina Kula](https://raux.github.io/)
- [Takashi Ishio](https://takashi-ishio.github.io/)
- [Kenichi Matsumoto](https://matsumotokenichi.github.io/)
