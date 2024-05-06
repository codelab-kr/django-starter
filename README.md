# 0. Prerequisites
```shell
# Install pipenv
brew install pipenv
# .zshrc 에 가상환경 환경변수 설정
export PIPENV_IGNORE_VIRTUALENVS=1
export PIPENV_VERBOSITY=-1
```

# 1. Set up the project
```shell
git clone https://github.com/codelab-kr/django_starter.git
cd django_starter
pipenv install
pipenv shell
```

### ( Optinal ) If the database is not created
```shell
# create database
python3 manage.py migrate
# create superuser
python3 manage.py createsuperuser
```

# 2. Run server
```shell
python3 manage.py runserver
```


# 3. Access to browser and check
- Server http://localhost:8000
- admin page http://localhost:8000/admin
