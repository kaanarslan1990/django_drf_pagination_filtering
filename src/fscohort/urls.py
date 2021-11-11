from django.urls import path
from fscohort.views import home_page, student_list, student_add, student_detail, student_delete, student_update, manuel_api, student_list_api, student_list_api_2, student_add_api
from .api.views import student_list_crate_api, student_get_update_delete, course_list_create_api, StudentListCreateAPIView, StudentDetailAPIView, CourseListCreateAPIView

urlpatterns = [
    
    #*----------------------------------class based views
    path("list_api/", StudentListCreateAPIView.as_view(), name="list"),
    path("list_api/<int:id>", StudentDetailAPIView.as_view(), name="detail"),
    path("course_api/", CourseListCreateAPIView.as_view(), name="courses"),

    #*----------------------------------function based views
    # path("list_api/", student_list_crate_api, name="list"),
    # path("course_api/", course_list_create_api, name="courses"),
    # path("list_api/<int:id>", student_get_update_delete, name="detail"),
    # path('api_add/', student_add_api),
    # path('api_list2/', student_list_api_2, name='list-api-2'),
    # path('api_list/', student_list_api, name='list-api'),
    # path('api/', manuel_api, name='api'),
    
    #*-----------------------------------teplate
    # path('home/', home_page, name='home'),
    # path('list/',student_list , name='list'),
    # path('add/',student_add , name='add'),
    # path('<int:id>',student_detail , name='detail'),
    # path('<int:id>/delete',student_delete , name='delete'),
    # path('<int:id>/update',student_update , name='update'),
]


    
    