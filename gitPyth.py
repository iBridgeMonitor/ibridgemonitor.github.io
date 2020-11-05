import base64
from github import Github
from github import InputGitTreeElement

user="iBridgeMonitor"
print(user)
print("HELLO")
g=Github(user,password)
repo=g.get_user().get_repo('git-test')


file_list=["Y:\McGunnigle\myWork\Web\Resources\wwx3\bMonitor\myUploadTest.txt"]
file_names=["myUploadTest.txt"]

commit_message="gmg Try this..."

master_ref = repo.get_git_ref('heads/master')
master_sha = master_ref.object.sha
base_tree = repo.get_git_tree(master_sha)
element_list = list()
for i, entry in enumerate(file_list):
    print(i)
    with open(entry) as input_file:
        data = input_file.read()
    if entry.endswith('.png'):
        data = base64.b64encode(data)
    element = InputGitTreeElement(file_names[i], '100644', 'blob', data)
    element_list.append(element)
tree = repo.create_git_tree(element_list, base_tree)
parent = repo.get_git_commit(master_sha)
commit = repo.create_git_commit(commit_message, tree, [parent])
master_ref.edit(commit.sha)