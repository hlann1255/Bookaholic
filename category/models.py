
from django.db import models
from django.urls import reverse
# Create your models here.
#null and blank are used to allow the database to store null values
#https://translate.google.com.vn/?sl=en&tl=vi&text=If%20True%2C%20Django%20will%20store%20empty%20values%20as%20NULL%20in%20the%20database.%20Default%20is%20False.%0A%0ANote%20that%20empty%20string%20values%20will%20always%20get%20stored%20as%20empty%20strings%2C%20not%20as%20NULL.%20Only%20use%20null%3DTrue%20for%20non-string%20fields%20such%20as%20integers%2C%20booleans%20and%20dates.%20For%20both%20types%20of%20fields%2C%20you%20will%20also%20need%20to%20set%20blank%3DTrue%20if%20you%20wish%20to%20permit%20empty%20values%20in%20forms%2C%20as%20the%20null%20parameter%20only%20affects%20database%20storage%20(see%20blank).%0A%0AAvoid%20using%20null%20on%20string-based%20fields%20such%20as%20CharField%20and%20TextField%20unless%20you%20have%20an%20excellent%20reason.%20If%20a%20string-based%20field%20has%20null%3DTrue%2C%20that%20means%20it%20has%20two%20possible%20values%20for%20%E2%80%9Cno%20data%E2%80%9D%3A%20NULL%2C%20and%20the%20empty%20string.%20In%20most%20cases%2C%20it%E2%80%99s%20redundant%20to%20have%20two%20possible%20values%20for%20%E2%80%9Cno%20data%3B%E2%80%9D%20Django%20convention%20is%20to%20use%20the%20empty%20string%2C%20not%20NULL.%0A%0AField.blank%0A%0AIf%20True%2C%20the%20field%20is%20allowed%20to%20be%20blank.%20Default%20is%20False.%0A%0ANote%20that%20this%20is%20different%20than%20null.%20null%20is%20purely%20database-related%2C%20whereas%20blank%20is%20validation-related.%20If%20a%20field%20has%20blank%3DTrue%2C%20validation%20on%20Django%E2%80%99s%20admin%20site%20will%20allow%20entry%20of%20an%20empty%20value.%20If%20a%20field%20has%20blank%3DFalse%2C%20the%20field%20will%20be%20required.%0A%0AField.default%0A%0AThe%20default%20value%20for%20the%20field.%20This%20can%20be%20a%20value%20or%20a%20callable%20object.%20If%20callable%20it%20will%20be%20called%20every%20time%20a%20new%20object%20is%20created.&op=translate
class Category(models.Model):
    category_name = models.CharField(max_length=50,unique=True ) 
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255,blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)
    
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])
    def __str__(self):
        return self.category_name