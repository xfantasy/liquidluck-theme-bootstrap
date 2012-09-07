# Bootstrap Theme for Felix Felicis

This theme is designed for documentation site.


## Installation

Install this theme with liquidluck:

```
$ liquidluck install bootstrap
```

Install this theme with Git:

```
$ git submodule add git://github.com/lepture/liquidluck-theme-bootstrap.git _themes/bootstrap
```

## Setup

Edit your settings file, change the theme to ``bootstrap``.

```py
theme = 'bootstrap'
use_relative_url = True
```

Disable some writers:

```py
writers = {
    'archive_feed': None,
    'category_feed': None,
    'year': None,
    'tag': None,
}
```


## Advanced

Category support:

```py
theme_variables = {
    'categories': {
        'work': u'工作',
        'life': u'生活',
    },
}
```

Navigation support:

```py
theme_variables = {
    'navigation': [
        (u'博客', 'http://lepture.com'),
        ('Theme', 'http://github.com/lepture/liquidluck-theme-bootstrap'),
    ],
}
```
