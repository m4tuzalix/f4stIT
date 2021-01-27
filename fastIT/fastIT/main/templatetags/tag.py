from django import template
register = template.Library()

@register.filter
def verify_length(value):
    if len(value) == 0:
        return ""
    return f"&city={value}"