from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    minimum_age_appropriate = models.IntegerField(default=0, blank=False)
    maximum_age_appropriate = models.IntegerField(default=-1, blank=False)
                                                  
    def random_image(self): 
      randimage=self.productimage_set.order_by('?')
      if randimage.exists():
        return randimage [0]
  
    def __str__(self):
        return f"Product {self.name}, price {self.price:.02f}"

    def age_range(self):
        if self.maximum_age_appropriate == -1:
            return f"Ages {self.minimum_age_appropriate} and up"
        elif self.maximum_age_appropriate == self.minimum_age_appropriate:
            return f"Age {self.minimum_age_appropriate}"
        else:
            return f"Ages {self.minimum_age_appropriate} to {self.maximum_age_appropriate}"

class ProductImage(models.Model):
  image = models.ImageField (blank=False, null=False, upload_to="images")
  caption= models.CharField(max_length=150,blank=True)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)

  def __str__(self):
    if self.caption==None:
      return f"{self.product.name}"
    else:
	    return f"{self.product.name}: {self.caption}"

class ProductImage(models.Model):
  image = models.ImageField(upload_to='product_images/')
  caption = models.CharField(max_length=30)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)