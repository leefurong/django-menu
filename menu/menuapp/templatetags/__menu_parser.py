from menuapp.models import MenuItem


INDENT = {
            'indent': True,
            'dedent': False,
        }
DEDENT={
            'indent': False,
            'dedent': True,
        }


class StructuredMenu():
    def __init__(self, menu_name):
        menu_items = MenuItem.objects.filter(menu_name=menu_name)

        # make a dict, so that it will be faster to query children
        item_dict = {}
        for item in menu_items:
            key = item.parent and item.parent.pk
            item_dict.setdefault(key, []).append(item)
        
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
                result.extend(self._get_normalized(child.pk))
            result.append(DEDENT)
        return result

