# Third Layer - *Use Cases (Application Layer)*

This is the heart of the app's behavior.

TODO

## What lives here

| Component   | Purpose                          | What it is in the app           | Tech                |
| ----------- | -------------------------------- | ------------------------------- | ------------------- |

What they do:

* Implement application-specific rules
* Orchestrate entities
* Enforce business workflows

Examples:

* Create card
* Move card
* Archive board
* Reorder columns

Tech:

* Pure Python
* No FastAPI
* No SQLAlchemy
* No Pydantic

```python
class CreateCardUseCase:
    def __init__(self, card_repo: CardRepository):
        self.card_repo = card_repo

    def execute(self, input: CreateCardInput):
        card = Card.create(...)
        self.card_repo.save(card)
        return CreateCardOutput(card)
```

Responsibilities:

* Business rules
* Transaction boundaries
* Calling repositories
* Handling domain errors

⚠️ There should be no :

* HTTP
* DB
* frameworks

## Where they live

TODO

## Dependencies

TODO

## Next

[Fourth Layer - *Entities (Domain Layer)*](./fourth_layer.md)
