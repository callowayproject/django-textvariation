========================
Goals of Text Variations
========================

Django Text Variations grew out of a need for certain types of content to have multiple versions of text based on specified variation types. 

In short, text variations needs to accomplish:

#. There can be multiple types of variations (e.g. language, audience, text difficulty)

#. There could be multiple fields on a model which require text variations.

#. There could be a maximum number of variations of content equal to the multiplication of the number of each variation type. (e.g. text difficulty levels x audiences x languages)

#. Variation types are configurable on a per-project (site) implementation.

#. Any of the variation types, or the variations within that type, could be added to or removed from at any time. (e.g. deciding on going from one language to multiple languages, or going from two language variations to three)

#. There should be a way to handle addressing the variation in a url.

#. Not all the variations will be used for each item.

#. There should be a default variation. If an addressed variation does not exist, it should use the default variation, or a variation algorithmically specified using available variations (graceful fallback).

#. Invalidation of variations should happen when the default content is changed.
