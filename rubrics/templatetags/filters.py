from django import template

register = template.Library()


@register.filter(name='TypeCount')
def TypeCount(value,arg):
    return value[arg]

@register.filter(name='ShortDesc')
def ShortDesc(value,arg):
    if value!=None:
        if len(value)>arg:
            return value[:arg-1]+'...'
        else:
            return value
    else:
        return 'Описания нет'

@register.filter(name='ToStr')
def ToStr(value):
    return str(value)