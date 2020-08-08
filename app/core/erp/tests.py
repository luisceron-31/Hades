
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_wsgi_application()


from core.erp.models import Type

# Listar
# select * from Tabla

query = Type.objects.all()
print(query)