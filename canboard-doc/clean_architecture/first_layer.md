# First Layer - *Frameworks & Drivers*

This layer is replaceable. Its elements should be independent from each other and only depend on elements from the inner layers. If you change any of FastAPI, React, PostgreSQL, nothing else should break.

It is the "Outside world". Anything that enters (or leaves) the app will come from (or go to) one of the elements of this layer :

* Information needs to be stored -> DB
* DB -> information that is needed
* Information to display to the user -> UI
* UI -> Inputs from the user
* Etc..

## What lives here

| Component   | Purpose                          | What it is in the app           | Tech                |
| ----------- | -------------------------------- | ------------------------------- | ------------------- |
| **Devices**             | TODO | User’s phone / browser          | iOS / Android / Web |
| **Web**                 | TODO | HTTP transport                  | REST                |
| **UI**                  | TODO | CanBoard UI (canboard-frontend) | React             |
| **External Interfaces** | TODO | HTTP, OpenAPI                   | FastAPI             |
| **DB**                  | TODO | Persistent storage              | PostgreSQL          |

## Responsibilities

* Rendering UI
* Sending HTTP requests
* Receiving HTTP responses
* Storing data
* Talking to the outside world

⚠️ There should be no business logic here!

## Concrete examples

### UI (React)

* Kanban board screen
* Drag & drop cards
* Calls generated OpenAPI client

``` dart
api.createCard(boardId, columnId, title);
```

React:

* Does not know what a “valid card” is
* Does not enforce business rules

### Web / External Interfaces (FastAPI)

* HTTP routing
* JSON parsing
* OpenAPI generation

```python
@router.post("/cards")
def create_card(request: CreateCardRequest):
    pass
```

### DB (PostgreSQL + SQLAlchemy)

* Tables
* Foreign keys
* Indexes
* Constraints (non-business)

## Where they live

TODO

## Dependencies

TODO

## Next

[Second Layer - *Interface Adapters*](./second_layer.md)
