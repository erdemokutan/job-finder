from django_filters import rest_framework as filters
from .models import Job


class JobsFilter(filters.FilterSet):

    min_salary=filters.NumberFilter(field_name='salary' or 0,lookup_expr='gte')#gte= greater than equal
    max_salary=filters.NumberFilter(field_name='salary' or 9999999999,lookup_expr='lte')#lte= less than equal
    
    


    class Meta:
        model=Job
        fields=('education','jobType','experience','min_salary','max_salary',)