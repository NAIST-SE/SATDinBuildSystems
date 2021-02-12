import pandas as pd
from pathlib import Path

root = os.path.dirname(os.getcwd())
html_url_repo = pd.read_csv(root + '/Dataset/3out.csv', header=None)

# import maven comments which is stored as stdout file
files = Path(root + '/Dataset/').glob('**/stdout')



SATD_comments = pd.DataFrame(columns=['Link Location', 'Comment', 'Keywords'])
with open(root + 'Dataset/keywords_list.txt', 'r') as file:
    keywords_debt = file.read().split(', ')


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

        for index in files_column.index:
            filepath = index
            if isinstance(files_column[index], dict):
                for key in files_column[index].keys():
                    if key.isdigit():

                        if filepath[-7:] == 'pom.xml':
                            maven += 1
                            comment = files_column[index][key]['Text']
                            for keyword in keywords_debt:
                                if re.search(r"\b" + re.escape(keyword.lower()) + r"\b", comment.lower()):
                                    keywords = [key for key in keywords_debt if key.lower() in comment.lower()]
                                    line = files_column[index][key]['Line']
                                    SATD_comments = SATD_comments.append(
                                            pd.Series(
                                                [html_url + '/blob/' + object_id + '/' + filepath +
                                                 '#L' + str(line), comment, keywords],
                                                index=SATD_comments.columns), ignore_index=True)

                                    break

SATD_comments.to_excel(root + '/Results/SABD_comments.xlsx', index=None, header=True)
