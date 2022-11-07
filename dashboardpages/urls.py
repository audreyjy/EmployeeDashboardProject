from django.urls import path
from .views import indexPageView, addPageViewGet, AddPageViewPost, EditPageView, EditPageViewPost, DelPageView


urlpatterns = [
    path("", indexPageView, name="index"), 
    path("add/", addPageViewGet, name="add"),
    path("addrec/", AddPageViewPost, name='addrec'),
    path("edit/<int:j_id>", EditPageView, name='edit'),
    path("editrec/<int:j_id>", EditPageViewPost, name='editrec'),
    path("del/<int:j_id>", DelPageView, name='del')
]
