from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from appdata.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('DepartmentAdd/', DepartmentAdd),
    path('DepartmentView/', DepartmentView),
    path('DepartmentList/', DepartmentList),
    path('DepartmentDelete/<int:id>', DepartmentDelete),
    path('', Login),
    path('Welcome/', Welcome),
    
    
]
if settings.DEBUG:
        urlpatterns+= static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
