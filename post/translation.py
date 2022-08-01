from modeltranslation.translator import translator, TranslationOptions
from .models import Post,Category,Link

class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)
translator.register(Post, PostTranslationOptions)

    
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)
translator.register(Category, CategoryTranslationOptions)


class LinkTranslationOptions(TranslationOptions):
    fields = ('title',)
translator.register(Link, LinkTranslationOptions)


# class CommentTranslationOptions(TranslationOptions):
#     fields = ('content',)
# translator.register(Comment, CommentTranslationOptions)