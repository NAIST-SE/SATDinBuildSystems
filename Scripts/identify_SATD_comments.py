import pandas as pd
from pathlib import Path
import os
import numpy as np
import re

root = os.path.dirname(os.getcwd())
html_url_repo = pd.read_csv(root + '/Dataset/3out.csv', header=None)

# import maven comments which is stored as stdout file
files = Path(root + '/Dataset/').glob('**/stdout')



SATD_comments = pd.DataFrame(columns=['Link Location', 'Comment', 'Keywords'])
Comments_with_no_keywords = pd.DataFrame(columns=['Link Location', 'Comment'])
revision_list = pd.DataFrame(columns=['Repository ID', 'Revison'])
with open(root + '/Dataset/keywords_list.txt', 'r') as file:
    keywords_debt = file.read().split(', ')


maven_comments = 0
maven_repo = 0
pom_file = 0
error = []
for file in files:
    df = pd.read_json(file)
    if not df.empty:
        files_column = df['Files']
        repo_id = df['Repository'][0]
        object_id = df['ObjectId'][0]
        html_url = str(html_url_repo[2][np.where(html_url_repo[0] == repo_id)[0]].values)
        html_url = html_url.replace('\'', '')
        html_url = html_url.replace('[', '')
        html_url = html_url.replace(']', '')
        if 'FileTypes' not in df.columns:
            error.append(file)
        else:
            if 'MAVEN' in df['FileTypes'].keys():
                pom_file += df['FileTypes']['MAVEN']
                maven_repo += 1
                revision_list = revision_list.append(pd.Series([repo_id,html_url + '/commmit/' + object_id], index=revision_list.columns), ignore_index=True)
        
        for index in files_column.index:
            filepath = index
            if isinstance(files_column[index], dict):
                for key in files_column[index].keys():
                    if key.isdigit():
                        if filepath[-7:] == 'pom.xml':
                            maven_comments += 1
                            comment = files_column[index][key]['Text']
                            line = files_column[index][key]['Line']
                            link_url = html_url + '/blob/' + object_id + '/' + filepath + '#L' + str(line)
                            keywords = [keyword for keyword in keywords_debt if re.search(r"\b" + re.escape(keyword.lower()) + r"\b", comment.lower())]
                            if len(keywords)> 0 and link_url not in list(SATD_comments['Link Location']):

                                SATD_comments = SATD_comments.append(
                                            pd.Series(
                                                [link_url, comment, keywords],
                                                index=SATD_comments.columns), ignore_index=True)

                            elif link_url not in list(Comments_with_no_keywords['Link Location']):
                                Comments_with_no_keywords = Comments_with_no_keywords.append(
                                            pd.Series(
                                                [link_url, comment],
                                                index=Comments_with_no_keywords.columns), ignore_index=True)


print(maven_comments)
print(maven_repo)
print(pom_file)
print(error)

SATD_comments_dup = SATD_comments.drop_duplicates(subset=['Link Location', 'Comment'], keep='first', inplace=False)
Comments_with_no_keywords_dup = Comments_with_no_keywords.drop_duplicates(subset=['Link Location', 'Comment'], keep='first', inplace=False)
Comments_with_no_keywords_dup_no_empty = Comments_with_no_keywords_dup[Comments_with_no_keywords_dup.Comment != '']
revision_list.to_csv(root + '/Dataset/revision_list.csv', index=None, header=True)
SATD_comments_dup.to_csv(root + '/Dataset/SATD_comments.csv', index=None, header=True)
Comments_with_no_keywords_dup_no_empty.to_csv(root + '/Dataset/comments_with_no_keywords.csv', index=None, header=True)
Comments_sample = Comments_with_no_keywords_dup_no_empty.sample(384)
Comments_sample.to_csv(root + '/Dataset/384_samples_comments_with_no_keywords', index=None, header=True)