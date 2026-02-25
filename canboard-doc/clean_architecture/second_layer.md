# Second Layer - *Interface Adapters*

This is the translation layer. It adapts the outside world to the business logic of the app.

Anything that comes from (or goes to) the outside will go through this layer. It translates informtion both ways between the frist and third layer.

TODO

## What lives here

| Component   | Purpose                          | What it is in the app           | Tech                |
| ----------- | -------------------------------- | ------------------------------- | ------------------- |
| **Controllers** | HTTP → Use Case                  | TODO | FastAPI, Pydantic |
| **Presenters**  | Use Case → HTTP response         | TODO | Pydantic, HTTP |
| **Gateways**    | Use Case → DB / external systems | TODO | SQLAlchemy, Alembic |

### Controllers

What they do:

* Receive raw input (HTTP, JSON)
* Validate shape, not business rules
* Call the appropriate use case

Tech:

* FastAPI routers
* Dependency injection
* Pydantic request models

```python
@router.post("/cards")
def create_card(
    request: CreateCardRequest,
    use_case: CreateCardUseCase = Depends()
):
    return use_case.execute(request)
```

⚠️ Controllers must not:

* Access SQLAlchemy
* Contain business logic

### Presenters

What they do:

* Convert use case output into:
  * HTTP response
  * DTO
  * Error format

Tech:

* Pydantic response models
* HTTP status codes

```python
class CardPresenter:
    def present(self, output: CreateCardOutput) -> CardResponse:
        return CardResponse(...)
```

This is where:

* Domain errors → HTTP 400 / 409
* Entities → JSON DTOs

### Gateways

What they do:

* Implement repository interfaces
* Talk to databases or external services

Tech:

* SQLAlchemy
* PostgreSQL
* Alembic

```python
class SqlAlchemyCardRepository(CardRepository):
    def save(self, card: Card):
        pass
```

Key idea:

* Implements an interface defined inside
* Knows SQLAlchemy
* Domain does not know SQLAlchemy exists

## Where they live

TODO

## Dependencies

TODO

## Next

[Third Layer - *Use Cases (Application Layer)*](./third_layer.md)
