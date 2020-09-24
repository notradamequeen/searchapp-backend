
# Search App Backend

This searchapp project is powered by:
- Python 3.6
- Django
- PostgreSql
- Elasticsearch
- Docker

# How to setup

1. install docker follow the instruction here https://docs.docker.com/get-docker/
2. install docker-compose follow the instruction here https://docs.docker.com/compose/install/
3. install python virtual environment choose one of below option:
    - pyenv: https://github.com/pyenv/pyenv-virtualenv
    - virtualenvwrapper: https://virtualenvwrapper.readthedocs.io/en/latest/install.html
    - virtulenv: https://pypi.org/project/virtualenv/
4. create virtualenv using python 3.6
5. activate virtualenv.
6. clone searchapp-backend source code
```git clone https://github.com/notradamequeen/searchapp-backend.git```
7. to run the app run `docker-compose up` this will take several minutes until it's up.
8. to shut down the app run `docker-compose down`

  

## API
### Search autocomplete api
|  			     |   |
|----------------|----------------------------------------
|**Url**         |`/api/search-autocomplete/`
|**Method**      |`GET`
|**Params** |```{ search: string }```
|**Response** |status 200 OK

```
[
	{
		text1: string,
		text2: string
	},
]
```
