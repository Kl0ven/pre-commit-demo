# pre-commit-demo
A pre-commit Demo


[pre-commit Website](https://pre-commit.com/)
[pre-commit Github](https://github.com/pre-commit/pre-commit)



## installation
```bash
poetry install  # with poetry

pip install -r requirements.txt  # with pip
```

Then run to setup the pre-commit
```bash
poetry run pre-commit install

ou

pre-commit install
```

## Run
pre-commit will be launch on every commit. You can launch them manually with the following command:
```bash
pre-commit run  # only on staged file

pre-commit run  --all-file # on all file
```
