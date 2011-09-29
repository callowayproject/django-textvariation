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
        'text_difficulty': {
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

def get_fallback_path(val, dim_dict):
    tmp_list = [val]
    if dim_dict[val].get('fallback', None) is None:
        return tmp_list
    elif isinstance(dim_dict[val]['fallback'], (list, tuple)):
        # assume the fallback has already been expanded
        return dim_dict[val]['fallback']
    elif isinstance(dim_dict[val]['fallback'], basestring):
        tmp_list.extend(get_fallback(dim_dict[val]['fallback'], dim_dict))
        return tmp_list

for key in TEXT_VARIATIONS['DIMENSIONS'].keys():
    for variant in TEXT_VARIATIONS['DIMENSIONS'][key].keys():
        TEXT_VARIATIONS['DIMENSIONS'][key][variant]['fallback'] = get_fallback(variant, TEXT_VARIATIONS['DIMENSIONS'][key])

variations = {
    'headline': {
        'en': {
            'ad': {
                's': 'en-ad-s',
                'l': 'en-ad-l'
            },
        },
        'es': {
            'ad': {
                's': 'es-ad-s'
            }
        },
    }
}

# get Spanish, Child, Low
lookup = {
    'audience': TEXT_VARIATIONS['DIMENSIONS']['audience']['cd']['fallback'],
    'language': TEXT_VARIATIONS['DIMENSIONS']['language']['es-mx']['fallback'],
    'text_difficulty': TEXT_VARIATIONS['DIMENSIONS']['text_difficulty']['l']['fallback'],
}

cur_dict = variations['headline']
for dim in TEXT_VARIATIONS['DIMENSION_PRIORITY']:
    for key in lookup[dim]:
        if key in cur_dict:
            cur_dict = cur_dict[key]
            break

print cur_dict

