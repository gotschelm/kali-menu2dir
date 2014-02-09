#!/usr/bin/env python

from xdg.Menu import parse, Menu, MenuEntry
from xdg.DesktopEntry import DesktopEntry
import os, stat, errno, sys

#execs = []

def create_dir_menu(menu, dest_dir):
    for submenu in menu.Entries:
        if isinstance(submenu, Menu):
            #print ("\t" * tab) + unicode(submenu)
            create_dir_menu(submenu, dest_dir)
        elif isinstance(submenu, MenuEntry):
            #print ("\t" * tab) + unicode(submenu.DesktopEntry)
            for parent in submenu.Parents:
                pdir = parent.getPath()
                filename =  os.path.join(dest_dir, pdir,
                                         submenu.DesktopEntry.getName() )
                create_script(filename, submenu.DesktopEntry.getExec())
#                execs.append(submenu.DesktopEntry.getExec())

def create_script(filename, content):
    try:
        os.makedirs(os.path.dirname(filename))
    except OSError as e:
        if e.errno is not errno.EEXIST:
            raise

    with open(filename, 'w') as f:
        f.write(content)

    st = os.stat(filename)
    os.chmod(filename, st.st_mode | stat.S_IEXEC)




if not sys.argv[1]:
    print """ Usage:
                kalimenu2dir <path>
          """
    sys.exit()

menu = parse('/etc/xdg/menus/gnome-applications.menu')
kindex = [str(x) for x in menu.getEntries()].index("Kali") + 1
kalimenu = menu.Entries[kindex]
dest_dir = os.path.abspath(sys.argv[1])
create_dir_menu(kalimenu, dest_dir)

