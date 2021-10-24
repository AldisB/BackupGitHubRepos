# https://www.thepythoncode.com/article/using-github-api-in-python
# https://github.com/libgit2/pygit2/issues/554

# pip3 install PyGithub requests pygit2

from github import Github
import pygit2

# using an access token
g = Github('TOKEN')
org = g.get_organization('ORGNAME')

callbacks = pygit2.RemoteCallbacks(pygit2.UserPass('TOKEN', 'x-oauth-basic'))
# Clone repo
for repo in org.get_repos():
    # print(repo.clone_url)
    pygit2.clone_repository(
        url=repo.clone_url,
        path=f'/home/<username>/PycharmProjects/Backup/{repo.name}',
        callbacks=callbacks)


