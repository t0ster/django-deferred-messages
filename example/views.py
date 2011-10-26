from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages

from deferred_messages import add_deferred_message


def one(request, **kwargs):
    template_name = kwargs.pop('template_name', 'base.html')

    add_deferred_message(request, messages.INFO, 'Hello world from messages!')

    return render_to_response(template_name, RequestContext(request))


def two(request, **kwargs):
    template_name = kwargs.pop('template_name', 'base.html')

    return render_to_response(template_name, RequestContext(request))
