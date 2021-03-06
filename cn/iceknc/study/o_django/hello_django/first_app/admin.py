from django.contrib import admin

from first_app.models import BookInfo, HeroInfo


# Register your models here.
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'bpub_date']


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname', 'hgender', 'hcomment', 'hbook']


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
