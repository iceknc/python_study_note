from django.contrib import admin
from test_app.models import BookInfo, HeroInfo, ChinaRegion, Picture, GoodsInfo


class BookStackedInline(admin.StackedInline):
    model = HeroInfo
    extra = 2


class BookTabularInline(admin.TabularInline):
    model = HeroInfo
    extra = 2


# Register your models here.
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date', 'bprice', 'bread', 'bcomment']
    # inlines = [BookStackedInline]
    inlines = [BookTabularInline]


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname', 'hgender', 'hcomment', 'hbook']
    fields = ['hname', 'hgender', 'hcomment', 'hbook']


class ChinaRegionAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ['id', 'code', 'name', 'parentCode', 'parentId', 'parentName']
    actions_on_bottom = True
    ordering = ['id', ]
    # list_filter = ['parentCode',]
    search_fields = ['name']
    fields = ['code', 'name', 'parentId']

class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id']

admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
admin.site.register(ChinaRegion, ChinaRegionAdmin)
admin.site.register(Picture)
admin.site.register(GoodsInfo,GoodsInfoAdmin)
