from django.contrib import admin
from .models import Watch, WatchImage, Order

class WatchImageInline(admin.TabularInline):
    model = WatchImage
    extra = 1
    max_num = 5
    fields = ['image', 'order']
    
@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'price', 'stock', 'image_count', 'created_at']
    list_filter = ['brand', 'created_at']
    search_fields = ['name', 'brand', 'description']
    ordering = ['-created_at']
    inlines = [WatchImageInline]
    
    def image_count(self, obj):
        return obj.images.count()
    image_count.short_description = 'Images'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'watch', 'customer_name', 'customer_phone', 'order_date', 'status']
    list_filter = ['status', 'order_date']
    search_fields = ['customer_name', 'customer_phone', 'watch__name']
    ordering = ['-order_date']
    readonly_fields = ['order_date']
