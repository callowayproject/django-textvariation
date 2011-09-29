=============
Template Tags
=============

{% variation_url object variation %}

returns a url of the object with variations applied to it

{% get_text_variations object %}

Using the request, or other method, if possible, set the object's <field>_variation attributes and possibly update the text_variations context variable

Required before using the content object.

{% get_variation object field dimension=val dimension2=val ... %}

Returns the best variation fit for the object's specified field