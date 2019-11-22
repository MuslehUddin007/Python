from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default='Edit category')
    subcategory = models.CharField(max_length=50 ,default='Edit subcategory')
    price = models.FloatField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default='No Image')

    def __str__(self):
        return self.product_name