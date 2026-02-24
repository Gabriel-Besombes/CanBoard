# Fourth Layer - *Entities (Domain Layer)*

This is the core business model.

TODO

## What lives here

| Component   | Purpose                          | What it is in the app           | Tech                |
| ----------- | -------------------------------- | ------------------------------- | ------------------- |

What they are:

* Business objects
* Invariants
* Rules that are always true

Examples:

* Board
* Column
* Card
* User

Tech:

* Plain Python
* Dataclasses or rich objects
* Zero dependencies

```python
class Card:
    def __init__(self, title: CardTitle, position: Position):
        if position < 0:
            raise InvalidPosition()
```

Responsibilities

* Enforce invariants
* Contain business logic
* Express ubiquitous language

## Where they live

TODO

## Dependencies

TODO

## Next

TODO
