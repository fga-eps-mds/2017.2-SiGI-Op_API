import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'sigi_op.settings'
import django
django.setup()

from django.contrib.auth.management.commands.createsuperuser import get_user_model
if get_user_model().objects.filter(username='admin'): 
    print("Super user already created")
else:
    get_user_model()._default_manager.db_manager('default').create_superuser(username='admin', email='admin@admin.com', password='admin123456')
    print("Super user created")
