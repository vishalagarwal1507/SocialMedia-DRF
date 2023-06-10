from rest_framework import serializers
from .models import File,Folder
import shutil

class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = '__all__'

class FileListSerializer(serializers.Serializer):
    files = serializers.ListField(
        child = serializers.FileField(max_length=10000000, allow_empty_file = False, use_url =False)
    )
    folders = serializers.CharField(required=False)


    def zip_files(self,folder):
        print(f'/public/static/zip/{str(folder.uid)}','zip',f'/public/static/{str(folder.uid)}')
        try:
            shutil.make_archive(f'public/static/zip/{str(folder.uid)}','zip',f'public/static/{str(folder.uid)}')
        except Exception as e:
            print(e)

    def create(self,validated_data):
        folder = Folder.objects.create()
        files = validated_data.pop('files')
        files_objs = []
        for file in files:
            print(file)
            files_obj = File.objects.create(folder=folder, files=file)
            files_objs.append(files_obj)

        self.zip_files(folder)

        return {'files': [], 'folder': str(folder.uid), 'file_url':"https:localhost:8000/media/zip/"+str(folder.uid)+".zip"}
    

