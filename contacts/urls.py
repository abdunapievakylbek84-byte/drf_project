from pathlib import Path

from django.urls import path
from contacts.views import Contact, ContactList, ContactCreate, ContactDetail, ContactDelete, ContactUpdate

urlpatterns = [
    path('contacts/', ContactList.as_view()),
    path('contacts/create/', ContactCreate.as_view()),
    path('contacts/<int:pk>/', ContactDetail.as_view()),
    path('contacts/<int:pk>/delete/', ContactDelete.as_view()),
    path('contacts/<int:pk>/update/', ContactUpdate.as_view()),
]