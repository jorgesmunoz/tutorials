import strawberry
from typing import List
from strawberry_app import Fruit


@strawberry.type
class Query:
    fruits: List[Fruit] = strawberry.django.field()


schems = strawberry.Schema(query=Query)
