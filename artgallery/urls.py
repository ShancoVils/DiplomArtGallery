from . import views
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import LoginUser
from .views import RegisterUser
from django.conf.urls.static import static
from django.conf import settings
from .views import WorkCreate, Contacts, Workpage, Autorpage, LoginUserChange, LikeView, Popular, ProfileLike, Work_category

# from .views import SignUpView
 
urlpatterns = [
    path('', views.main, name='main'),
    

    #Категории переделать
    path('categories/CategoryIllustrator.html', views.CategoryIllustrator, name='Illustrator'),
    path('categories/CategoryLanding.html', views.CategoryLanding, name='Landing'),
    path('categories/CategoryPhoto.html', views.CategoryPhoto, name='Photo'),
    path('categories/CategoryPhotoshop.html', views.CategoryPhotoshop, name='Photoshop'),
    path('categories/CategoryProduct.html', views.CategoryProduct, name='ProductDisign'),
    path('categories/CategoryUI.html', views.CategoryUI, name='UICategory'),
    #Категории переделать

    #Страница авторов
    path('autors/autors.html', views.AutorsPage, name='autors'),

    #Добавить работу
    path('profiles/index/addwork/addwork/', WorkCreate.as_view(), name='testingcrud'),

    #Регистрация/авторизация
    path('registration/login/', views.login_or_reg, name='login'),

    #Регистрация/авторизация
    path('logout/', views.logout_user, name='logout'),

    #Профиль
    path('profiles/index/', views.Profile, name='profile'),
    
    #ПрофильЛайк
    path('profiles/index/', ProfileLike, name='profilelike'),

    #Контакты
    path('contacts/index.html', Contacts.as_view(), name='contacts' ),

    #Популярное
    path('popular_works/index/', Popular, name='popular'),

    #Работы
    path('work_category/index/', Work_category, name='work_category'),


    #Страница работы
    path('workpage/<int:works_id>/', Workpage, name='workpage'),

    #Страница авторов
    path('autor/<int:customuser_id>/', Autorpage, name='anotherautorpage'),


    #Настройки профиля
    path('profile_option/<int:pk>/', LoginUserChange.as_view(), name='profile_option'),
    
    #Лайк
    path('like/<int:pk>/', LikeView, name='like_work'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
