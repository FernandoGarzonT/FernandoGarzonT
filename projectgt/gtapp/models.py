from django.db import models
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password
from email_validator import validate_email, EmailNotValidError
from django.utils import timezone



class Imagen(models.Model):
    """Create Model Image"""

    name_imagen = models.CharField(max_length=50, help_text='Name description')
    image_location = models.ImageField(upload_to='', blank=True, null=True)
    text_imagen = models.TextField(max_length=10000)
    date_create_imagen = models.DateTimeField('Date Create Imagen')

    def __str__(self):
        return self.name_imagen

class Person(models.Model):
    """Create Model Person for profile"""

    first_name = models.CharField(max_length=50, help_text='Example Carlo Mario')
    last_name = models.CharField(max_length=50, help_text='Example Benedetti Postiga')
    nickname = models.CharField(unique=True, max_length=20, validators=[UnicodeUsernameValidator])
    cell_phone = models.IntegerField(help_text='3001112233')
    email_person = models.EmailField(unique=True) 
    date_create_user = models.DateTimeField(default=timezone.now)
    password_user = models.CharField(max_length=32, validators=[validate_password], 
                                    help_text='minimun eigth characters')

    REQUIRED_FIELDS = ["email_person"]       

    def email_validator(self):
        """Validate Email, with format correct """
        while True:
            try:
                self.email_person = validate_email(self.email_person).email_person
            except EmailNotValidError as e:
                print(str(e) + "Your Email should be in this format example@example.com")
    
    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name
    
    def __str__(self):
        return self.email_person

""" class Minigame(models.Model):
    r"Variables for Minigames"

    num = models.CharField(max_length=12)
    palabra = models.CharField(max_length=10)

    def __str__(self):
        return self.num, self.palabra """
