# OS Module

List all files and directories in a given path

    $ python3 list.py
    Files and directories for path '\' is: 
    ['srv', 'snap', 'dev', 'lib', 'usr', 'lost+found', 'bin.usr-is-merged', 'sbin', 'run', 'bin', 'root', 'sbin.usr-is-merged', 'devopsworkspace', 'tmp', 'backupScript.sh', 'lib.usr-is-merged', 'sys', 'var', 'swap.img', 'backups', 'mnt', 'cdrom', 'media', 'test', 'etc', 'home', 'opt', 'lib64', 'boot', 'proc']

Delete a file or directory

    $ python3 rm.py
    Successfully removed directory: test

Print all environment variables

    $ python3 environ.py
    The environment variables are:
    environ({'USER': 'tj', 'XDG_MENU_PREFIX': 'gnome-', 'HOME': '/home/tj', 'DBUS_SESSION_BUS_ADDRESS': 'unix:path=/run/user/1000/bus', 'XDG_DATA_DIRS': '/usr/share/ubuntu:/usr/share/gnome:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop', 'XDG_CONFIG_DIRS': '/etc/xdg/xdg-ubuntu:/etc/xdg', 'WINDOWPATH': '2', 'GTK_MODULES': 'gail:atk-bridge', 'XDG_SESSION_DESKTOP': 'ubuntu', 'GSM_SKIP_SSH_AGENT_WORKAROUND': 'true', 'GNOME_DESKTOP_SESSION_ID': 'this-is-deprecated', 'QT_ACCESSIBILITY': '1', 'DEBUGINFOD_URLS': 'https://debuginfod.ubuntu.com ',.......})

Set a custom environment variable, DB_ADMIN as user(Extract user from environment variables)

    $ python3 customEnviron.py
    The DB_ADMIN is:  tj
    
Install curl using os module

    $ python3 curl.py 
    Fetched 8,733 kB in 10s (886 kB/s)        
    Reading package lists... Done
    Building dependency tree... Done
    Reading state information... Done
    41 packages can be upgraded. Run 'apt list --upgradable' to see them.
    Reading package lists... Done
    Building dependency tree... Done
    Reading state information... Done
    curl is already the newest version (8.5.0-2ubuntu10.6).
    0 upgraded, 0 newly installed, 0 to remove and 41 not upgraded.

Create a script that checks disk usage by calling df -h using os module

    $ python3 disk.py      
    Disk usage: 
    Filesystem      Size  Used Avail Use% Mounted on
    tmpfs           1.6G  2.8M  1.6G   1% /run
    /dev/nvme0n1p7  144G   69G   69G  50% /
    tmpfs           7.7G  292M  7.4G   4% /dev/shm
    tmpfs           5.0M   12K  5.0M   1% /run/lock
    efivarfs        256K  165K   87K  66% /sys/firmware/efi/efivars
    /dev/nvme0n1p1  256M  103M  154M  40% /boot/efi
    tmpfs           1.6G  140K  1.6G   1% /run/user/1000
    0
