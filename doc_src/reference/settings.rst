.. _settings:

========
Settings
========

All configuration for Django Text Variations occurs within the ``TEXT_VARIATIONS`` setting variable. ``TEXT_VARIATIONS`` is a dictionary with the following keys:

* :ref:`settings-dimensions`

* :ref:`settings-dimension_priority`

* :ref:`settings-models`

* :ref:`settings-default_url_regex`

* :ref:`settings-url_regex_map`

* :ref:`settings-example`


.. _settings-dimensions:

DIMENSIONS
==========


.. _settings-dimension_priority:

DIMENSION_PRIORITY
==================


.. _settings-models:

MODELS
======


.. _settings-default_url_regex:

DEFAULT_URL_REGEX
=================


.. _settings-url_regex_map:

URL_REGEX_MAP
=============

.. _settings-example:

Example Settings
================

.. code-block:: python

	TEXT_VARIATIONS = {
	    'DIMENSIONS': {
	        'audience': {
	            'ad': {
	                'name': u'Adult',
	                'fallback': None,
	            },
	            'tn': {
	                'name': u'Teen',
	                'fallback': 'ad',
	            },
	            'cd': {
	                'name': u'Child',
	                'fallback': 'tn',
	            }
	        },
	        'text_dificulty': {
	            'l': {
	                'name': u'Low',
	                'fallback': 's',
	            },
	            's': {
	                'name': u'Standard',
	                'fallback': None,
	            },
	            'a': {
	                'name': u'Advanced',
	                'fallback': 's',
	            }
	        },
	        'language': {
	            'en': {
	                'name': u'English',
	                'fallback': None,
	            },
	            'es': {
	                'name': u'Español',
	                'fallback': 'en',
	                'domain': 'es.example.com',
	            },
	            'es-mx': {
	                'name': u'Español mexicano',
	                'fallback': 'es',
	                'domain': 'es-mx.example.com',
	            },
	            'fr': {
	                'name': u'Français',
	                'fallback': 'en',
	                'domain': 'fr.example.com',
	            }
	        },
	    },
	    'DIMENSION_PRIORITY': ['language', 'audience', 'text_difficulty'],
	    'MODELS': {
	        'app.model': ['field1', 'field2'],
	        'app2.model': ['field1', ]
	    },
	    'DEFAULT_URL_REGEX': '{language}/{path};{audience},{text_difficulty}',
	    'URL_REGEX_MAP': {
	        'app.model': '{path};{language},{audience},{text_difficulty}',
	    }
	}
