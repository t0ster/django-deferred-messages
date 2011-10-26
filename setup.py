from setuptools import setup
import os

setup(name='django-deferred-messages',
      author="Roman Dolgiy",
      author_email="roman@bravetstudio.com",
      packages=["deferred_messages"],
      namespace_packages=[],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
