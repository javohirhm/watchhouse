from django.db import models

class Watch(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.brand} - {self.name}"
    
    def get_primary_image(self):
        """Get the first image or None"""
        return self.images.first()
    
    def get_all_images(self):
        """Get all images ordered by order field"""
        return self.images.all().order_by('order')
    
    class Meta:
        verbose_name_plural = "Watches"


class WatchImage(models.Model):
    watch = models.ForeignKey(Watch, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='watch_images/')
    order = models.IntegerField(default=0, help_text='Image order (0 is primary)')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Image {self.order + 1} for {self.watch.name}"
    
    class Meta:
        ordering = ['order']
        verbose_name = "Watch Image"
        verbose_name_plural = "Watch Images"


class Order(models.Model):
    watch = models.ForeignKey(Watch, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=20)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')
    
    def __str__(self):
        return f"Order #{self.id} - {self.customer_name} - {self.watch.name}"
    
    class Meta:
        ordering = ['-order_date']
