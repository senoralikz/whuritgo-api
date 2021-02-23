from django.urls import path
from .views.mango_views import Mangos, MangoDetail
from .views.expense_views import Expenses, ExpenseDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing
    path('mangos/', Mangos.as_view(), name='mangos'),
    path('mangos/<int:pk>/', MangoDetail.as_view(), name='mango_detail'),
    path('expenses/', Expenses.as_view(), name='expenses'),
    path('expenses/<int:pk>/', ExpenseDetail.as_view(), name='expense_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-password/', ChangePassword.as_view(), name='change-password')
]
