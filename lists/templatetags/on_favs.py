from django import template
from lists import models as list_models
from django.shortcuts import render, redirect, reverse

register = template.Library()


@register.simple_tag(takes_context=True)
def on_favs(context, room):
    try:
        user = context.request.user
        the_list, _ = list_models.List.objects.get_or_create(
            user=user, name="My Favourite Houses"
        )
        return room in the_list.room.all()
    except Exception as ex:
        return redirect("core:home")
        print(ex)
