from xdg.Menu import parse, Menu, MenuEntry

def print_menu(menu, tab=0):
	for submenu in menu.Entries:
	if isinstance(submenu, Menu):
		print ("\t" * tab) + unicode(submenu)
		print_menu(submenu, tab+1)
	elif isinstance(submenu, MenuEntry):
		print ("\t" * tab) + unicode(submenu.DesktopEntry)


a = xdg.Menu.parse('/etc/xdg/menus/gnome-applications.menu')


