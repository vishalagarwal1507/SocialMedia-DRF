from django.db import models
import uuid
import os

# Create your models here.
class Folder(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

def get_upload_path(instance, filename):
    return os.path.join(str(instance.folder.uid),filename)
    
class File(models.Model):
    folder = models.ForeignKey(Folder, on_delete= models.CASCADE) 
    files = models.FileField(upload_to=get_upload_path)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.folder.uid)
    
    def get_absolute_url(self):
        return "/files/{}".format(self.folder.uid)