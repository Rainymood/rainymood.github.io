---
title: "services and handlers" 
date: 2023-03-22
---

the way we write code at Snappet is with services and handlers

we create these kind of services that just do one thing

and then we have a handler that just orchestrates that thing

```python
    query_service = QueryService()
    load_data_service = LoadDataService()
    load_model_service = LoadModelService()
    save_state_service = SaveStateService()

    calculation_service = CalculationService(
        load_model_service=load_model_service,
    )

    handler = CalculationServiceHandler(
        calculation_service=calculation_service,
        load_data_service=load_data_service,
        query_service=query_service,
    )

    handler.run(
        ...
    )
```

this is a form of **dependency injection**

this allows us to write some loosely coupled but highly cohesive code

in essence we just wrap things in services and then compose them together

what is cool is that you should be able to pass a `NoSaveStateService()` now easily and things should work

it took me a while to understand why this code works

in the beginning i just copied it

then i got sceptical

then i got enlightened