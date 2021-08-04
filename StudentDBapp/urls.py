from django.contrib import admin
from django.urls import re_path, path
from .views import (
	home,
	add,
	search,
	display,
	)

urlpatterns = [
	re_path(r'^$', home, name = 'home'),
	re_path(r'^add-student$', add, name = 'add'),
	re_path(r'^search-student$', search, name = 'search'),
	re_path(r'^display-student$', display, name = 'display'),
]