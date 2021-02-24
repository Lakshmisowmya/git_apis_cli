# git_apis_cli

CLI to make requests to github API. 

https://docs.github.com/en/rest/overview/endpoints-available-for-github-apps

# Supported Endpoints

-  repos 
   - Languages : https://docs.github.com/en/rest/reference/repos#list-repository-languages
   - Contributors : https://docs.github.com/en/rest/reference/repos#list-repository-contributors
-  users
   - userDetails : https://docs.github.com/en/rest/reference/users#get-a-user

# Installation

```
pip3 install git-apis
```

# Usage

```
$ git-apis --help
Usage: git-apis [OPTIONS] COMMAND [ARGS]...

  A CLI wrapper for the GitHub APIs.

Options:
  --help  Show this message and exit.

Commands:
  repos  Get Repo related details - Languages/Contributors for a given repo...
  users  Get User details
```

## **Repos**
```
$ git-apis repos --help
Usage: git-apis repos [OPTIONS] [languages|contributors]

  Get Repo related details - Languages/Contributors for a given repo

  languages        - Lists languages for specified repository.

                     The value shown for each language is the number of
                     bytes of code written in that language.

  contributors     - Lists contributors to the specified repository

                     Sorts them by the number of commits per contributor in
                     descending order

Options:
  -r, --repo TEXT   Return details of this repo  [required]
  -o, --owner TEXT  Return only repos of this owner  [required]
  --help            Show this message and exit.
  
```  
To get the languages used in a public repo like https://github.com/grafana/grafana

```
$ git-apis repos languages --repo grafana --owner grafana
{'TypeScript': 9096427, 'Go': 4246052, 'JavaScript': 706586, 'HTML': 420811, 'Rich Text Format': 352348, 'SCSS': 259056, 'Shell': 138550, 'Dockerfile': 37977, 'Python': 35068, 'Jsonnet': 33059, 'CSS': 19419, 'Makefile': 6720, 'Smarty': 2116, 'PHP': 574}
 ```
 
 ## **Users**
 ```
$ git-apis users --help
Usage: git-apis users [OPTIONS] USERNAME

  Get User details

Options:
  --help  Show this message and exit.
 ```
 To get a user details
 
 ```
$ git-apis users  Lakshmisowmya
{'login': 'Lakshmisowmya', 'id': 20332588, 'node_id': 'MDQ6VXNlcjIwMzMyNTg4', 'avatar_url': 'https://avatars.githubusercontent.com/u/20332588?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/Lakshmisowmya', 'html_url': 'https://github.com/Lakshmisowmya', 'followers_url': 'https://api.github.com/users/Lakshmisowmya/followers', 'following_url': 'https://api.github.com/users/Lakshmisowmya/following{/other_user}', 'gists_url': 'https://api.github.com/users/Lakshmisowmya/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/Lakshmisowmya/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/Lakshmisowmya/subscriptions', 'organizations_url': 'https://api.github.com/users/Lakshmisowmya/orgs', 'repos_url': 'https://api.github.com/users/Lakshmisowmya/repos', 'events_url': 'https://api.github.com/users/Lakshmisowmya/events{/privacy}', 'received_events_url': 'https://api.github.com/users/Lakshmisowmya/received_events', 'type': 'User', 'site_admin': False, 'name': None, 'company': None, 'blog': '', 'location': None, 'email': None, 'hireable': None, 'bio': None, 'twitter_username': None, 'public_repos': 9, 'public_gists': 0, 'followers': 3, 'following': 1, 'created_at': '2016-07-07T05:46:42Z', 'updated_at': '2021-02-23T17:28:00Z'}
