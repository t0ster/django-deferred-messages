from django.contrib import messages


class DeferredMessageMiddleware(object):
    def process_response(self, request, response):
        # Making sure messages middleware is loaded
        if hasattr(request, '_messages') and "deferred_messages" in request.session:
            for message in request.session["deferred_messages"]:
                messages.add_message(request, message.level, message.message, message.extra_tags)
            del request.session["deferred_messages"]
        return response
