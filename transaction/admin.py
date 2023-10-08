from django.contrib import admin
from .models import *


admin.site.register(ExpenditureTransaction)

admin.site.register(ProfitableTransaction)

admin.site.register(IncomeType)

admin.site.register(Category)

admin.site.register(Meter)
