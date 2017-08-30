from modeltranslation.translator import translator, TranslationOptions
from tks.apps.member.models import member as Member


class MemberTranslationOptions(TranslationOptions):
    fields = ('name', 'company_name', 'biz_type',)

translator.register(Member, MemberTranslationOptions)
