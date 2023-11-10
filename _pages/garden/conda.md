---
title: "conda" 
date: 2023-03-23
---


```bash
conda create --name NAME python==3.8 -y
conda activate NAME
pip install poetry
poetry config virtualenvs.create false
poetry init
poetry install --no-root
```

to auto-find conda environments in jupyter notebooks...

```
conda install nb_conda
```


* nb_conda_kernels in the environment with Jupyter
* ipykernel and ipywidgets in the Python environment you want to access (note that ipywidgets is to enable some Juptyer functionality, not environment visibility, see related docs).
