from django.contrib import admin
from .models import GoodsCategory, GoodsCategoryBrand, Goods, IndexAd, GoodsImage, Banner, HotSearchWords
# Register your models here.


class GoodsCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category_type', 'parent_category', 'add_time']

class GoodsCategoryBrandAdmn(admin.ModelAdmin):
    list_display = ['category', 'name', 'desc', 'image']

class GoodsAdmin(admin.ModelAdmin):
    list_display = ["name", "click_num", "sold_num", "fav_num", "goods_num", "market_price",
                    "shop_price", "goods_brief", "goods_desc", "is_new", "is_hot", "add_time"]

class IndexAdAdmin(admin.ModelAdmin):
    list_display = ["category", "goods"]


class BannerAdmin(admin.ModelAdmin):
    list_display = ["goods", "image", "index"]

class HotSearchWordsAdmin(admin.ModelAdmin):
    list_display = ["keywords", "index", "add_time"]

admin.site.register(GoodsCategory, GoodsCategoryAdmin)
admin.site.register(GoodsCategoryBrand, GoodsCategoryBrandAdmn)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(IndexAd, IndexAdAdmin)
admin.site.register(GoodsImage)
admin.site.register(Banner, BannerAdmin)
admin.site.register(HotSearchWords, HotSearchWordsAdmin)
