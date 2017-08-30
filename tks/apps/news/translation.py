from modeltranslation.translator import translator, TranslationOptions
from tks.apps.news.models import news


class Translatednews(TranslationOptions):
    fields = ('title', 'descript', )


translator.register(news, Translatednews)
