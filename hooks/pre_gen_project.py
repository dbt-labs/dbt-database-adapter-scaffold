{% if cookiecutter.adapter_src == "sql" %}
{{ cookiecutter.update({ "adapter_cls":"SQLAdapter","connection_cls": "SQLConnectionManager"}) }}
{% else %}
{{ cookiecutter.update({"adapter_cls":"BaseAdapter","connection_cls":"BaseConnectionManager"}) }}
{% endif %}
