from django.contrib import admin
from django.urls import path, include
from main.views import HomeView
from tasks.views import TaskListView, TaskUpdateView, TaskDeleteView, TaskCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='main-home'),
    path('', TaskListView.as_view(), name = 'task-list'),
    path('Tasks/<int:pk>/edit/', TaskUpdateView.as_view(), name= 'task-edit'),
    path('Tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name= 'task-delete'),
    path('Tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('account/', include('account.urls'))
]
