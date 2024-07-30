from rest_framework import filters


class OnlyNewPerevalFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        status = request.query_params.get("status", None)
        if status == "new":
            return queryset.filter(status="new")
        return queryset
