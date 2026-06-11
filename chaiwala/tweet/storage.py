from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible
from django.core.files.base import ContentFile
import mimetypes

@deconstructible
class DatabaseStorage(Storage):
    def _open(self, name, mode='rb'):
        from .models import DatabaseFile
        name = name.replace('\\', '/')
        try:
            db_file = DatabaseFile.objects.get(name=name)
            return ContentFile(db_file.content, name=name)
        except DatabaseFile.DoesNotExist:
            raise FileNotFoundError(f"File not found: {name}")

    def _save(self, name, content):
        from .models import DatabaseFile
        name = name.replace('\\', '/')
        
        # Read content bytes
        content_bytes = content.read()
        
        mime_type, _ = mimetypes.guess_type(name)
        if not mime_type:
            mime_type = 'application/octet-stream'
        
        # Save to DB
        DatabaseFile.objects.update_or_create(
            name=name,
            defaults={
                'content': content_bytes,
                'mime_type': mime_type,
                'size': len(content_bytes)
            }
        )
        return name

    def delete(self, name):
        from .models import DatabaseFile
        name = name.replace('\\', '/')
        DatabaseFile.objects.filter(name=name).delete()

    def exists(self, name):
        from .models import DatabaseFile
        name = name.replace('\\', '/')
        return DatabaseFile.objects.filter(name=name).exists()

    def url(self, name):
        from django.urls import reverse
        name = name.replace('\\', '/')
        return reverse('serve_db_file', kwargs={'path': name})

    def size(self, name):
        from .models import DatabaseFile
        name = name.replace('\\', '/')
        try:
            return DatabaseFile.objects.get(name=name).size
        except DatabaseFile.DoesNotExist:
            return 0
