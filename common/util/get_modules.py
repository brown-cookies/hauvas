def get_modules(modules_list):
    modules = []

    for module_list in modules_list:
        module = {"title": module_list.title, "id": module_list.id}
        items = []

        for module_item in module_list.items.all():
            item = {
                "id": module_item.id,
                "title": module_item.title,
                "description": module_item.description,
                "content_url": module_item.content_url,
                "is_published": module_item.is_published,
            }

            items.append(item)

        module["items"] = items
        modules.append(module)

    return modules
