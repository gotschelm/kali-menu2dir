kali-menu2dir
=============

Create a directory structure in a given path based on the Kali aplications
menu in Kali Linux. This is useful when you want to browse the kali menu
inside a terminal or when you use a WM that is not fully XDG compatible.

For better window manager integration, check out xdg-menu[1] 

[1]: https://wiki.archlinux.org/index.php/XdgMenu


##Usage##

    ./kali-menu2dir.py <path>


##Example##

    root@kali:~# ./kali-menu2dir.py .
    root@kali:~# ls -1 "Kali Linux/Top 10 Security Tools/"
    aircrack-ng
    burpsuite
    hydra
    john
    (...)
