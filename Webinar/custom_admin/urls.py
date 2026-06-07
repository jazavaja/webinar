from django.urls import path
from . import views

urlpatterns = [
    path("",views.main_admin,name="admin_main"),
    path("/edt_user/<int:id>/",views.edit_user,name="admin_edit_user"),
    path("/create_user",views.create_user,name="admin_create_user"),
    path("/admin_user",views.user,name="admin_users"),
    path("/admin_webinar",views.webinar,name="admin_webinars"),
    path("/delete_user/<int:id>/",views.delete_user,name="admin_delete_user"),
    path("/activate_webinar/<int:id>/",views.activate_webinar,name="admin_active_webinar"),
    path("/deactivate_webinar/<int:id>/",views.deactivate_webinar,name="admin_deactivate_webinar"),
    # path("/sub/<int:id>/",views.admin_sub,name="admin_sub"),

]