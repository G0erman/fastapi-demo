# Requirements

* pyenv
* python 3.11
* Poetry works well with pyenv. `pyenv exec poetry add fastapi`

# Useful commands

* `pyenv exec poetry show --latest`
* `pyenv exec poetry add pytest --group dev`

# Installation

```sh
pyenv exec python -m venv venv
source venv/bin/activate
pyenv exec poetry install --with dev
``` 

# Local development

`make pre-commit`
`make run`

