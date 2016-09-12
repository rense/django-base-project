from mptt.managers import TreeManager


class MenuItemManager(TreeManager):

    def get_main_menu(self):
        return self.model.published.all().filter(parent__isnull=True)
