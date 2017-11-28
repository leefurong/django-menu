from menuapp.models import MenuItem


INDENT = {
            'indent': True,
            'dedent': False,
        }
DEDENT={
            'indent': False,
            'dedent': True,
        }

def get_path(url):
    from urlparse import urlparse
    return urlparse(url).path

class StructuredMenu():
    def __init__(self, menu_name, selected_path):
        menu_items = MenuItem.objects.filter(menu_name=menu_name)

        # make a dict, so that it will be faster to query children
        item_dict = {}
        selected_item = None
        for item in menu_items:
            key = item.parent and item.parent.pk
            item_dict.setdefault(key, []).append(item)
            if (get_path(item.link) == selected_path):
                selected_item = item

        # expand
        expanded_items = set([selected_item])
        parent = selected_item and selected_item.parent
        while parent:
            expanded_items.add(parent)
            parent = parent.parent
        for item in menu_items:
            item.expand = item in expanded_items

        
        # sort menu items by order_weight
        for v in item_dict.values():
            v.sort(lambda a,b: cmp(a.order_weight, b.order_weight))
        
        self.item_dict = item_dict

    
    def get_children(self, parent_pk=None):
        return self.item_dict.get(parent_pk,[])


    def get_normalized(self):
        return self._get_normalized(None)


    def _get_normalized(self, parent_pk):
        result = []
        children = self.get_children(parent_pk)
        if children:
            result.append(INDENT)
            for child in children:
                result.append({
                    'title': child.title,
                    'link': child.link,
                    'indent': False,
                    'dedent': False,
                })
                if child.expand:
                    result.extend(self._get_normalized(child.pk))
            result.append(DEDENT)
        return result

