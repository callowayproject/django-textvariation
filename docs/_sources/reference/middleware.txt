.. _textvariationmiddleware:

=======================
TextVariationMiddleware
=======================


Needs to be first in the list so it can properly modify the path information.

The middleware modifies the request

* Matches request path against the configured regular expressions

* If it matches, extract the dimensions and set into request.META['TEXT_VARIATIONS']

* Join the unnamed groups in the matching regular expression with "/"

* Set request.path, request.path_info and request.META['PATH_INFO'] to the resulting value
