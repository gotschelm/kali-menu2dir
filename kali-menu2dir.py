#!/usr/bin/env python
#
# Copyright 2014 Cornelis Gotschelm <gotschelm gmail com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.#!/usr/bin/env python

from xdg.Menu import parse, Menu, MenuEntry
from xdg.DesktopEntry import DesktopEntry
import os, stat, errno, sys

#execs = []

def create_dir_menu(menu, dest_dir):
    for submenu in menu.Entries:
        if isinstance(submenu, Menu):
            create_dir_menu(submenu, dest_dir)
        elif isinstance(submenu, MenuEntry):
            for parent in submenu.Parents:
                pdir = parent.getPath()
                filename =  os.path.join(dest_dir, pdir,
                                         submenu.DesktopEntry.getName() )
                create_script(filename, submenu.DesktopEntry.getExec())
#               execs.append(submenu.DesktopEntry.getExec())

def create_script(filename, content):
    try:
        os.makedirs(os.path.dirname(filename))
    except OSError as e:
        if e.errno is not errno.EEXIST:
            raise

    content = content.replace('${SHELL:-bash}', '')

    with open(filename, 'w') as f:
        f.write(content)

    st = os.stat(filename)
    os.chmod(filename, st.st_mode | stat.S_IEXEC)

# Main

if not len(sys.argv) > 1:
    print """ Usage:
                kalimenu2dir <path>
          """
    sys.exit()

menu = parse('/etc/xdg/menus/gnome-applications.menu')
kindex = [str(x) for x in menu.getEntries()].index("Kali") + 1
kalimenu = menu.Entries[kindex]
dest_dir = os.path.abspath(sys.argv[1])

create_dir_menu(kalimenu, dest_dir)
