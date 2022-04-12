import strawberry
from strawberry.django import auto
from typing import List
from strawberry_app import models


@strawberry.django.type(models.Fruit)
class Fruit:
    id: auto
    name: auto
    color: 'Color'


@strawberry.django.type(models.Color)
class Color:
    id: auto
    name: auto
    fruits: List[Fruit]
