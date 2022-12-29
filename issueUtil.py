import string


def create_issue_content(traffic_data: dict, view_data: dict) -> string:
    # 문자열 그냥 합치면 효율성이 떨이짐.
    github_url = 'https://github.com/'
    issue_list = list()
    issue_cloner_header = '## Unique Cloner <br/> \n'
    issue_viewer_header = '## Unique viewer <br/> \n'
    issue_list.append(issue_cloner_header)



    for unique_cloner in traffic_data:
        repo_name, cloner = unique_cloner
        issue_list.append(f"- [{repo_name}]({github_url}" + repo_name + f") 의 클론 수:{cloner} <br/>\n")

    issue_list.append('<br/>' * 5)
    issue_list.append("\n")

    issue_list.append(issue_viewer_header)

    for unique_view in view_data:
        repo_name, viewer = unique_view
        issue_list.append(f"- [{repo_name}]({github_url}" + repo_name + f") 의 방문자:{viewer} <br/>\n")

    issue_list.append("If you, the creator, also visit or clone the repository daily, the results will be counted and "
                      "accumulated daily. Please be aware of this.<br/>")

    return ''.join(issue_list)

