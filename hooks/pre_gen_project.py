# import sys
# import json

## Was an attempt to use pre/post gen hooks to update the cookiecutter.json ##
## Pre gen hooks did not see cookiecutter.json as exisiting file ##
## Post gen triggers after cookiecutter.json has run and failed cause connection_cls and adapter_cls didn't exist ##


# if '{{cookiecutter.adapter_src}}' == 'sql':
#     entry = '{"adapter_cls":"SQLAdapter","connection_cls": "SQLConnectionManager"}'
# elif '{{cookiecutter.adapter_src}}' == 'base':
#     entry = '{"adapter_cls":"BaseAdapter","connection_cls":"BaseConnectionManager"}'    
# else:
#     entry = '{"adapter_cls":"TODO","connection_cls":"TODO"}'

# with open("cookiecutter.json", "r+") as file:
#     data = json.load(file)
#     data.append(entry)
#     file.seek(0)
#     json.dump(data, file)

# sys.exit(1)

#  Variables from json
#  "adapter_cls":["SQLAdapter","BaseAdapter"],
#  "connection_cls":["SQLConnectionManager","BaseConnectionManager"],

{% if cookiecutter.adapter_src == "sql" %}
{{ cookiecutter.update({ "adapter_cls":"SQLAdapter","connection_cls": "SQLConnectionManager"}) }}
{% else %}
{{ cookiecutter.update({"adapter_cls":"BaseAdapter","connection_cls":"BaseConnectionManager"}) }}
{% endif %}
