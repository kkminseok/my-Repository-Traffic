
def create_issue_content(traffic_data):
    # 문자열 그냥 합치면 효율성이 떨이짐.
    github_url = 'https://github.com/'
    issue_list = list()
    #issue_header = '## Unique Cloner <br/>\n'
    #issue_cloner_detail = '<details> <br/> '
    #issue_summary = '<summary> Cloner </summary> <br/>'
    #issue_cloner_detail_close = '</details> <br/>'
    #issue_list.append(issue_header)
    #issue_list.append(issue_cloner_detail)
    #issue_list.append(issue_summary)

    for data in traffic_data:
        repo_name, cloner = data
        issue_list.append(f"- [{repo_name}]({github_url}" + repo_name + f") 의 Unique Cloner:{cloner} <br>\n")

    #issue_list.append(issue_cloner_detail_close)
    return ''.join(issue_list)

