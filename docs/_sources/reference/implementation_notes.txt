====================
Implementation Notes
====================

#. There could be potentially a large number of variations for an individual field.

#. We want to keep the number of database calls/accesses and data storage to a minimum.

#. We must track some metadata about the variations, such as: variations used, invalidated variations.

Methods
*******

#. Related table(s)
	There are several variations: 
	
	* One table for each model with variations (using a Foreign Key)
	
	* One table for all models with variations (using a Generic Foreign Key)
	
	* Use a JSON field for all text variations of an object
	
	* A separate row for each text variation

#. Additional field(s) in the model
	There are two variations:
	
	* Use a JSON field for all text variations of an object
	
	* A separate field for each potential text variation

Implementation
**************

A combination of both methods will be used in a non-normalized way to provide flexibility and performance. A variation table for each model with variations will store each variation for each field. A JSON/serialized field on the model will store a cached version of the same information.

The fields in the variation table are:

==========  ==================================================================
field       Description
==========  ==================================================================
<model>_id  Foreign key to the row in the master table
fieldname   Name of the field in which this variation applies
<name>_dim  A field for each defined dimension to contain the dimension variant
is_invalid  A boolean flag to indicate the variation is currently invalid, as the default variation has changed. Declaring variations invalid instead of deleting them should be an option as to allow the site to continue to display the content.
value       The value of this variation for this field
==========  ==================================================================

The cache field contains a structure based on the current :ref:`settings-dimension_priority` settings. 

.. warning::
   If this setting changes the cache field for each item in every table will need to be recalculated. There is a management command to do this.

The cache is a hierarchical dictionary with each field at the top level and then each dimension hierarchically contained in order of priority.

.. code-block:: python

	{
	    'field': {
	        'dim1-variant1': {
	            'dim2-variant1': 'variation value',
	            'dim2-variant2': 'variation value',
	        }
	    }
	}


Example Walkthrough
*******************

Assuming that we have three dimensions: audience, text difficulty, and language; a table called article with three variable fields: headline, subhead, and content; the table and metadata table might look like:

.. note::
   See :ref:`settings-example` for the configuration.

.. image:: /images/variations-schema-example.png

If you added a row into article, you might have

==  =============  =========  ========  ===========  =========================
Id  Headline       Subhead    Byline    Content      Text Variations
==  =============  =========  ========  ===========  =========================
1   First article             Carmen    Lots of ...  ``{'headline':{'en':{'ad'...``
==  =============  =========  ========  ===========  =========================

The Text Variations field would contain a serialized dictionary:

.. code-block:: python

	{
	    'headline': {
	        'en': { 'ad': { 's': 'First Article',},},},
	    'subhead': {
	        'en': { 'ad': { 's': '',},},},
	    'content': {
	        'en': { 'ad': { 's': 'Lots of ...',},},},
	}

And the Audience Variation table contains

===  ==========  =========  ============  ============  ===================  ==========  ===================
Id   Article Id  Fieldname  Audience Dim  Language Dim  Text Difficulty Dim  Is Invalid  Value
===  ==========  =========  ============  ============  ===================  ==========  ===================
1    1           headline   ad            en            s                    False       First Article
2    1           subhead    ad            en            s                    False       
3    1           content    ad            en            s                    False       Lots of ...
===  ==========  =========  ============  ============  ===================  ==========  ===================

If you add a spanish variation to the headline and content fields, the Text Variations field would contain:

.. code-block:: python

	{
	    'headline': {
	        'en': { 'ad': { 's': 'First Article',},},
	        'es': { 'ad': { 's': u'Artículo Primero',},},},
	    'subhead': {
	        'en': { 'ad': { 's': '',},},},
	    'content': {
	        'en': { 'ad': { 's': 'Lots of ...',},},
	        'es': { 'ad': { 's': 'Mucho ...',},},},
	}

And the Audience Variation table contains

===  ==========  =========  ============  ============  ===================  ==========  ===================
Id   Article Id  Fieldname  Audience Dim  Language Dim  Text Difficulty Dim  Is Invalid  Value
===  ==========  =========  ============  ============  ===================  ==========  ===================
1    1           headline   ad            en            s                    False       First Article
2    1           subhead    ad            en            s                    False       
3    1           content    ad            en            s                    False       Lots of ...
4    1           headline   ad            es            s                    False       Artículo Primero
5    1           content    ad            es            s                    False       Mucho ...
===  ==========  =========  ============  ============  ===================  ==========  ===================



Schema Migrations
*****************

Adding/removing the JSON field

Adding/removing a metadata dimension field
