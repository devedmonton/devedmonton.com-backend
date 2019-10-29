from django.db import models

from grapple.models import (
    GraphQLString,
    GraphQLStreamfield,
)
from wagtail.core.models import Page


class HomePage(Page):
    pass

    graphql_fields = [
        GraphQLString("title"),
    ]
