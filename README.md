## Start Machine Learning project.

### Software and account Requirement.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)


Creating conda environment
```
conda create -p venv python==3.7 -y
```
```
conda activate venv/
```
OR 
```
conda activate venv
```

```
pip install -r requirements.txt
```

To Add files to git
```
git add .
```

OR
```
git add <file_name>
```

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status 
```
git status
```
To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```

To check remote url 
```
git remote -v
```

Update GIT Access token
'''

Create new PAT in Github
git remote set-url origin https://<personal_access_token>@github.com/<your_username>/<repo_name>.git

Your git remote -v should be something like:

origin  https://<your_personal_access_token>@github.com/<username>/<repo_name>.git (fetch)
origin  https://<your_personal_access_token>@github.com/<username>/<repo_name
'''


To setup CI/CD pipeline in heroku we need 3 information
1. HEROKU_EMAIL = manas.uit@gmail.com
2. HEROKU_API_KEY = <Should not put tese info in public domain>
3. HEROKU_APP_NAME = ml-regression-app_mp

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase


To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 7f1e3b48825e
```

To check running container in docker
```
docker ps
```

Tos stop docker conatiner
```
docker stop <container_id>
```

To remove docker file
'''
docker rmi -f $(docker images -aq)
'''


To insatll ipykernel - for jupyternotebook
'''
pip install ipykernel
'''