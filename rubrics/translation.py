from modeltranslation.translator import TranslationOptions,register
from .models import Go,Eat,Stay,News,TypesEat,TypesGo,TypesStay,Cities,Akmola,Events,Tours,Tourists,StaticPages,SidebarToStay,NationalFoods

@register(NationalFoods)
class NationalFoodsTranslationOptions(TranslationOptions):
    fields = ('title','content')


@register(SidebarToStay)
class SidebarToStayTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(StaticPages)
class StaticPagesTranslationOptions(TranslationOptions):
    fields = ('title','content')

@register(Tourists)
class ToursTranslationOptions(TranslationOptions):
    fields = ('title','short_description','content')

@register(Tours)
class ToursTranslationOptions(TranslationOptions):
    fields = ('title','short_description','content')

@register(Events)
class EventsTranslationOptions(TranslationOptions):
    fields = ('title','short_description','content','address')

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title','short_description','content')

@register(Akmola)
class AkmolaTranslationOptions(TranslationOptions):
    fields = ('title','short_description','content')

@register(Go)
class GoTranslationOptions(TranslationOptions):
    fields = ('title','short_description','content','address')
@register(Eat)
class EatTranslationOptions(TranslationOptions):
    fields = ('title','short_description','content','address')
@register(Stay)
class StayTranslationOptions(TranslationOptions):
    fields = ('title','short_description','content','address')

@register(TypesStay)
class TypesStayTranslationOptions(TranslationOptions):
    fields = ('name',)
@register(TypesEat)
class TypesEatTranslationOptions(TranslationOptions):
    fields = ('name',)
@register(TypesGo)
class TypesGoTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Cities)
class CitiesTranslationOptions(TranslationOptions):
    fields = ('name',)

