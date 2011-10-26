Installation
============

settings.py::

  MIDDLEWARE_CLASSES = (
      'django.middleware.common.CommonMiddleware',
      'django.contrib.sessions.middleware.SessionMiddleware',
      'django.middleware.csrf.CsrfViewMiddleware',
      'django.contrib.auth.middleware.AuthenticationMiddleware',
      'django.contrib.messages.middleware.MessageMiddleware',
      'deferred_messages.middleware.DeferredMessageMiddleware',
  )


views.py::

  from deferred_messages import add_deferred_message

  def one(request, **kwargs):
      ...
      add_deferred_message(request, messages.INFO, 'Hello world from messages!')
      ...



``deferred_messages.middleware.DeferredMessageMiddleware`` should come
after ``django.contrib.messages.middleware.MessageMiddleware``.
