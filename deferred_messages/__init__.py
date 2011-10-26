def add_deferred_message(request, level, message, extra_tags=None):
    from django.contrib.messages.storage.base import Message
    if not "deferred_messages" in request.session:
        request.session["deferred_messages"] = []
    request.session["deferred_messages"].append(Message(level, message, extra_tags))
