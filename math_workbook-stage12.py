# === Stage 12: Постраничный вывод ===
# Project: MathWorkbook
def add_pagination(request, queryset):
    """Add pagination to a queryset with page number and page size."""
    page_number = int(request.GET.get("page", 1))
    page_size = int(request.GET.get("page_size", 10))
    paginator = Paginator(queryset, page_size)
    page_obj = paginator.get_page(page_number)
    request.pagination = page_obj
    return page_obj
