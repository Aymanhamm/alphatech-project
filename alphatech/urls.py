from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from employees.views import login_view, logout_view, home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('employees/', include('employees.urls')),
    path('tasks/', include('tasks.urls')),
    path('leaves/', include('leaves.urls')),
    path('payroll/', include('payroll.urls')),
    path('performance/', include('performance.urls')),
    path('reports/', include('reports.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)