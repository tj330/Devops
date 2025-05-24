# Volume Management & Disk Usage

Create a directory /mnt/devops_data.

    $ sudo mkdir /mnt/devops_data 
    
Mount a new volume (or loop device for local practice).

    $ sudo mount /dev/sda1 /mnt/devops_data
    
Verify using df -h and mount | grep devops_data.

    $ df -h
    Filesystem      Size  Used Avail Use% Mounted on
    /dev/sda1        30G  6.0G   24G  21% /mnt/devops_data

    $ mount | grep devops_data
    /dev/sda1 on /mnt/devops_data type vfat (rw,relatime,uid=1000,gid=1000,fmask=0022,dmask=0022,
    codepage=437,iocharset=iso8859-1,shortname=mixed,showexec,utf8,flush,errors=remount-ro)

Unmount the volume

    $ sudo umount /mnt/devops_data
