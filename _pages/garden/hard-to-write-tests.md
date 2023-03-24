---
title: "hard to write tests" 
date: 2023-03-23
---

sometimes it is hard to write tests

then you end up not writing any tests because it is hard

this makes it harder to write tests

and you end up in this vicious negative feedback loop that is hard to get out of

it is hard to write tests *exactly because* it is hard to write tests

try to write code that is *designed* to be tested

we want to depend on abstractions and not on implementations

good

```python
df = pd.read_csv(path)
result = foo(df)
```

better

```python
import pandas as pd
from abstractmethod import ABC

class DataLoaderInterface(ABC):
    def load_data() -> pd.DataFrame: 
        raise NotImplementedError

class PandasDataLoader(DataLoaderInterface):
    def load_data(path):
        df = pd.read_csv(path)
        return df

df = Dataloader().load_data(path)
result = foo(df)
``` 

it really looks like we added a lot of boilerplate

which is true

but the bottom version is much more easily extendible because we are not coupled to the *implementation* of the pandas library

if we want to read in a dict or from another parquet file we can just write another data loader that implements the interface
