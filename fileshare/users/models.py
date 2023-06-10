# from django.db import models
# from autoslug import AutoSlugField
# from django.contrib.auth.models import User
# from django.db import models
# # Create your models here.

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(default='default.png', upload_to='profile_pics',blank=True)
#     slug = AutoSlugField(populate_from='user')
#     bio = models.CharField(max_length=255, blank=True)
#     friends = models.ManyToManyField("Profile", blank=True)

#     def __str__(self):
#         return str(self.user.username)

#     def get_absolute_url(self):
#         return "/users/{}".format(self.slug)


