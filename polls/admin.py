from django.contrib import admin
from django.db.models import Count, Sum, Min, Max

from django.db.models.functions import Trunc
from django.db.models import DateTimeField

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Product, Customer, Order


from django.contrib import admin
from .models import SaleSummary


def get_next_in_date_hierarchy(request, date_hierarchy):
    if date_hierarchy + '__day' in request.GET:
        return 'hour'
    if date_hierarchy + '__month' in request.GET:
        return 'day'
    if date_hierarchy + '__year' in request.GET:
        return 'week'
    return 'month'


@admin.register(SaleSummary)
class SaleSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/sale_summary_change_list.html'
    date_hierarchy = 'orderDate'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {
            'total': Sum('amount'),
            'total_sales': Sum('articleOrdered__price') * Sum('amount'),
        }

        response.context_data['summary'] = list(
            qs
            .values('articleOrdered__product')
            .annotate(**metrics)
            .order_by('-total_sales')
        )

        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics)
        )

        period = get_next_in_date_hierarchy(request, self.date_hierarchy)
        response.context_data['period'] = period

        summary_over_time = qs.annotate(
            period=Trunc(
                'orderDate',
                period,
                output_field=DateTimeField(),
            ),
        ).values('period').annotate(total=(Sum('articleOrdered__price')) * Sum('amount')).order_by('period')

        summary_range = summary_over_time.aggregate(
            low=Min('total'),
            high=Max('total'),
        )
        high = summary_range.get('high', 0)
        low = summary_range.get('low', 0)

        response.context_data['summary_over_time'] = [{
            'period': x['period'],
            'total': x['total'] or 0,
            'pct':
            ((x['total'] or 0) - low) / (high - low) * 100
            if high > low else 0,
        } for x in summary_over_time]

        return response

    list_filter = (
        'articleOrdered__product',
    )


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product


class CustomerResource(resources.ModelResource):
    class Meta:
        model = Customer


class OrderResource(resources.ModelResource):
    class Meta:
        model = Order


class ProductAdmin(ImportExportModelAdmin):
    resource_classes = [ProductResource]


class CustomerAdmin(ImportExportModelAdmin):
    resource_classes = [CustomerResource]


class OrderAdmin(ImportExportModelAdmin):
    resource_classes = [OrderResource]


admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
