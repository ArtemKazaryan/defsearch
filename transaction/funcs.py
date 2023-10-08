from django.shortcuts import render
from .models import ProfitableTransaction, ExpenditureTransaction
from django.db.models import Sum, F


def func2(request, maxdeltadays, sumpro, sumexp, multidash):
    queryset = ExpenditureTransaction.objects.values('name').annotate(totalexp=Sum(F('quantity') * F('price')),
                                                                      averpr=Sum(F('quantity') * F('price')) / Sum('quantity'),
                                                                      totalquant=Sum('quantity'), meter=F('meter__name'),
                                                                      categories=F('category__name')
                                                                       ).order_by()
    for item in queryset:
        item['consumptionrate'] = item['totalquant'] / maxdeltadays
        item['speedexp'] = item['totalexp'] / maxdeltadays

    context = {'queryset': queryset, 'multidash': multidash}
    return render(request, 'transaction/specialcalculation2.html', context)


def func3(request, maxdeltadays, sumpro, sumexp, multidash):
    queryset = ExpenditureTransaction.objects.values('category').annotate(totalexp=Sum(F('quantity') * F('price')),
                                                                          categories=F('category__name')).order_by()
    for item in queryset:
        item['speedexp'] = item['totalexp'] / maxdeltadays
        item['percentexp'] = round(100 * item['totalexp'] / sumexp, 0)
    context = {'queryset': queryset, 'multidash': multidash}
    return render(request, 'transaction/specialcalculation3.html', context)


def func4(request, maxdeltadays, sumpro, sumexp, multidash):
    queryset = ProfitableTransaction.objects.values('incometype').annotate(totalpro=Sum(F('amount')),
                                                                           incometypes=F('incometype__name')).order_by()
    for item in queryset:
        item['speedpro'] = item['totalpro'] / maxdeltadays
        item['percentpro'] = round(100 * item['totalpro'] / sumpro, 0)
    context = {'queryset': queryset, 'multidash': multidash}
    return render(request, 'transaction/specialcalculation4.html', context)


def func5(request, maxdeltadays, sumpro, sumexp, multidash):
    queryset = ProfitableTransaction.objects.values('name').annotate(totalpro=Sum(F('amount')),
                                                                     incometypes=F('incometype__name')).order_by()
    for item in queryset:
        item['speedpro'] = item['totalpro'] / maxdeltadays
        item['percentpro'] = round(100 * item['totalpro'] / sumpro, 0)
    context = {'queryset': queryset, 'multidash': multidash}
    return render(request, 'transaction/specialcalculation5.html', context)



