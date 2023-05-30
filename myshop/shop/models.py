from django.db import models
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields

class Category(TranslatableModel):
    translations = TranslatedFields(
    name = models.CharField(max_length=200,db_index=True),
    slug = models.SlugField(max_length=200,db_index=True),
    )
    
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

    class Meta:
        # ordering = ('name' ,)
        verbose_name = 'category'
        verbose_name_plural = "categories"


    def __str__(self):
        return self.name
    

class Product(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=200,db_index=True),
        slug = models.SlugField(max_length=200,db_index=True),
        description = models.TextField(blank=True),
        price = models.PositiveIntegerField(),
    )

    category = models.ForeignKey(Category, related_name="product", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    available = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id,self.slug])

    # class Meta:
    #     ordering = ('name',)
    #     index_together = (('id','slug'),)

    def __str__(self):
        return self.name
    

    def getsnippet(self):
        return self.description[0:30] + '...'
    