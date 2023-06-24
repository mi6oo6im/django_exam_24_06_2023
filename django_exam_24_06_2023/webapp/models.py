from django.core.validators import MinLengthValidator
from django.db import models
from django_exam_24_06_2023.webapp.validators import validate_first_char_is_letter, validate_letters_only

# Create your models here.

"""
•	Profile Model
o	First Name - DONE
	  
o	Last Name - DONE

o	Email - DONE

o	Password - DONE

o	Image URL
	    URL field, optional.
o	Age
	    Integer field, optional.
	    The age default value should be 18.

"""


class UserProfile(models.Model):
    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=25,
        validators=(
            MinLengthValidator(2),
            validate_first_char_is_letter,
        ),
        verbose_name="First Name"
    )
    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=35,
        validators=(
            MinLengthValidator(1),
            validate_first_char_is_letter,
        ),
        verbose_name="Last Name"
    )
    email = models.EmailField(
        null=False,
        blank=False,
        max_length=40,
        verbose_name="Email"
    )
    password = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=(MinLengthValidator(8),),
        verbose_name="Password"
    )
    image_url = models.URLField(
        null=True,
        blank=True,
        verbose_name="Image URL"
    )
    age = models.IntegerField(
        null=True,
        blank=True,
        default=18,
        verbose_name="Age",
    )

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    @property
    def posts(self):
        fruit_count = Fruit.objects.all().count()
        return fruit_count


class Fruit(models.Model):
    name = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        validators=(
            MinLengthValidator(2),
            validate_letters_only,
        ),
        verbose_name="Name"
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name="Image URL"
    )
    description = models.TextField(
        null=False,
        blank=False,
        verbose_name="Description"
    )
    nutrition = models.TextField(
        null=True,
        blank=True,
        verbose_name="Nutrition"
    )
