from .models import Category, Tag

def generate_cat_count_list(cat_cnts):
    result = ""
    for cat_cnt in cat_cnts:
        result += f"<li>{cat_cnt['cat_id__cat']}: {cat_cnt['cnt']}</li>"
    return result

def generate_category_iterable():
    category_list = Category.objects.all()
    category_iterable = [(str(index + 1), category.cat) for index, category in enumerate(category_list)]
    return category_iterable

def generate_tag_iterable():
    tag_list = Tag.objects.all()
    tag_iterable = [(str(index +1), tag.name) for index, tag in enumerate(tag_list)]
    return tag_iterable