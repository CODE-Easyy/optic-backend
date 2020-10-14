from django.db import models


from .validators import min_0

CATEGORIES = (
    ('glasses', 'glasses'),
    ('frames', 'frames'),
    ('outlet', 'outlet'),
)


class SubCategory(models.Model):
    value = models.CharField(max_length=20)
    cat = models.CharField(max_length=20, choices=CATEGORIES)

    def __str__(self):
        return self.value

class Brand(models.Model):
    value = models.CharField(max_length=100)
    def __str__(self):
        return self.value

    class Meta:
        ordering = ('value',)

class Material(models.Model):
    value = models.CharField(max_length=100)
    def __str__(self):
        return self.value
    class Meta:
        ordering = ('value',)

class Radius(models.Model):
    value = models.CharField(max_length=100)
    def __str__(self):
        return self.value
    class Meta:
        ordering = ('value',)

class OpticalPower(models.Model):
    value = models.CharField(max_length=100)
    def __str__(self):
        return self.value
    class Meta:
        ordering = ('value',)

class Volume(models.Model):
    value = models.CharField(max_length=100)
    def __str__(self):
        return self.value
    class Meta:
        ordering = ('value',)

class Product(models.Model):
    ''' Products model '''

    SEXES = (
        ('man', 'man'),
        ('woman', 'woman'),
        ('unisex', 'unisex'),
        ('child', 'child'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(default=0)

    img_1 = models.ImageField(upload_to='products_images', null=True, blank=True)
    img_2 = models.ImageField(upload_to='products_images', null=True, blank=True)
    img_3 = models.ImageField(upload_to='products_images', null=True, blank=True)

    cat = models.CharField(max_length=10, choices=CATEGORIES)
    subcat = models.ForeignKey(SubCategory, blank=True, null=True, on_delete=models.SET_NULL)

    is_new = models.BooleanField(default=True)
    is_leader = models.BooleanField(default=False)
    is_discount = models.BooleanField(default=False)
    discount = models.IntegerField(validators=[min_0], null=True, default=0)


    # GLASSES
    brand = models.ForeignKey(Brand, blank=True, null=True, on_delete=models.SET_NULL)
    material = models.ForeignKey(Material, blank=True, null=True, on_delete=models.SET_NULL)
    sex = models.CharField(max_length=20, choices=SEXES, null=True, blank=True)

    #FRAMES
    radius = models.ForeignKey(Radius, blank=True, null=True, on_delete=models.SET_NULL)
    opt_power = models.ForeignKey(OpticalPower, blank=True, null=True, on_delete=models.SET_NULL)


    #KAPLI
    volume = models.ForeignKey(Volume, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ('title', 'price',)

    def __str__(self):
        return "Product({}, {}, {})".format(self.title, self.cat, self.price)

    def get_max_price(self):
        return max([i.price for i in self.objects.all()])

    def get_min_price(self):
        return min([i.price for i in self.objects.all()])


