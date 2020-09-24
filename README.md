# Search App Backend

This searchapp project is powered by:
- Python 3.6
- Django
- PostgreSql  
- Elasticsearch
- Docker


# How to setup 

1. install docker follow the instruction here https://docs.docker.com/get-docker/
2. install python virtual environment choose one of below option:
    - pyenv: https://github.com/pyenv/pyenv-virtualenv
    - virtualenvwrapper: https://virtualenvwrapper.readthedocs.io/en/latest/install.html
    - virtulenv: https://pypi.org/project/virtualenv/
 3. create virtualenv using python 3.6
 4. activate virtualenv.
 5. clone searchapp-backend source code here:
 6. to run the app run `docker compose up` this will take several minutes until it's up.

## API
### Search autocomplete api
|                |             |
|----------------|----------------------------------------
|**Url**			 |`/api/search-autocomplete/`                       
|**Method**          |`GET`           
|**Params**          |```{ search: string }```
|**Response**		 |status 200 OK

```
[
	{
		score: float,
		text1: string,
		text2: string
	},
]
```
