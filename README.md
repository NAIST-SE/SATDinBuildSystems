# Research Artifact: Characterizing and Mitigating Self-Admitted Technical Debt in Build System

https://github.com/NAIST-SE/SATDinBuildSytem

This is a research artifact for the paper: **Characterizing and Mitigating Self-Admitted Technical Debt in Build System**. This artifact is a repository consisting of our
500 SATD comments dataset and 'ready-to-be-addressed' SATD comments. The purposes of this artifact are to enable researchers to reuse the dataset for further software engineering research.

## Contents
* `Dataset` - a directory of the dataset
	* `500_SATD_Comments.csv` - results of RQ1: open coding and card sorting SATD comments in Maven repositories.
		* `Index` - a numbered list.
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
	* `Revision_list.csv` - the list of HEAD revisions extract from DP1.
* `Scripts` - a directory of Scripts.
	* `README.md` - a readme file for Scripts directory.
	* `parallel_categories_diagram.ipynb` - the parallel categories diagram among location, reason, and purpose.
	* `identify_SATD_comments.py` - the script which is used to detect SATD comments.
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