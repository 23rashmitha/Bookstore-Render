from django.contrib import admin
from .models import TeluguBook, HindiBook, EnglishBook, FrenchBook, KannadaBook

# Register your models here.
admin.site.register(TeluguBook)
admin.site.register(HindiBook)
admin.site.register(EnglishBook)
admin.site.register(FrenchBook)
admin.site.register(KannadaBook)

