
from django.contrib import admin
from django.urls import path, include
from wordcount import views
from jobs import views as jobs_views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', jobs_views.home,name='home_page'),
    #path('word_setup/', views.setup,name='wordsetup'),
    #path('wordsetup/',views.count, name='count'),
    path('word_setup/',include('wordcount.urls')),
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
