Print current CPU usage percentage.

    $ python3 cpu.py 
    CPU usage percentage for the last 1 second is: 19.6%

List all running processes.

    $ python procs.py
    Name: systemd, PID: 1
    Name: kthreadd, PID: 2
    Name: pool_workqueue_release, PID: 3
    Name: kworker/R-rcu_gp, PID: 4
    Name: kworker/R-sync_wq, PID: 5
    Name: kworker/R-slub_flushwq, PID: 6
    Name: kworker/R-netns, PID: 7
    Name: kworker/0:0H-events_highpri, PID: 9
    Name: kworker/R-mm_percpu_wq, PID: 12
    Name: rcu_tasks_kthread, PID: 13
    Name: rcu_tasks_rude_kthread, PID: 14
    Name: rcu_tasks_trace_kthread, PID: 15
    Name: ksoftirqd/0, PID: 16
    Name: rcu_preempt, PID: 17
    Name: rcu_exp_par_gp_kthread_worker/0, PID: 18
    Name: rcu_exp_gp_kthread_worker, PID: 19
    Name: migration/0, PID: 20
    Name: idle_inject/0, PID: 21
    Name: cpuhp/0, PID: 22
    Name: cpuhp/2, PID: 23
    Name: idle_inject/2, PID: 24
    Name: migration/2, PID: 25
    Name: ksoftirqd/2, PID: 26
    Name: kworker/2:0-events, PID: 27
    Name: kworker/2:0H-events_highpri, PID: 28
    Name: cpuhp/4, PID: 29
    Name: idle_inject/4, PID: 30
    Name: migration/4, PID: 31
    Name: ksoftirqd/4, PID: 32
    Name: kworker/4:0H-events_highpri, PID: 34
    Name: cpuhp/6, PID: 35
    Name: idle_inject/6, PID: 36
    Name: migration/6, PID: 37
    Name: ksoftirqd/6, PID: 38
    Name: kworker/6:0H-events_highpri, PID: 40
    Name: cpuhp/8, PID: 41
    Name: idle_inject/8, PID: 42
    Name: migration/8, PID: 43
    Name: ksoftirqd/8, PID: 44
    Name: kworker/8:0H-events_highpri, PID: 46
    Name: cpuhp/9, PID: 47
    Name: idle_inject/9, PID: 48
    Name: migration/9, PID: 49
    Name: ksoftirqd/9, PID: 50
    Name: kworker/9:0H-events_highpri, PID: 52
    Name: cpuhp/10, PID: 53
    Name: idle_inject/10, PID: 54
    Name: migration/10, PID: 55
    Name: ksoftirqd/10, PID: 56
    Name: kworker/10:0H-events_highpri, PID: 58
    Name: cpuhp/11, PID: 59
    Name: idle_inject/11, PID: 60
    Name: migration/11, PID: 61
    Name: ksoftirqd/11, PID: 62
    Name: kworker/11:0H-events_highpri, PID: 64
    Name: cpuhp/1, PID: 65
    Name: idle_inject/1, PID: 66
    Name: migration/1, PID: 67
    Name: ksoftirqd/1, PID: 68
    Name: kworker/1:0H-events_highpri, PID: 70
    Name: cpuhp/3, PID: 71
    Name: idle_inject/3, PID: 72
    Name: migration/3, PID: 73
    Name: ksoftirqd/3, PID: 74
    Name: kworker/3:0H-events_highpri, PID: 76
    Name: cpuhp/5, PID: 77
    Name: idle_inject/5, PID: 78
    Name: migration/5, PID: 79
    Name: ksoftirqd/5, PID: 80
    Name: kworker/5:0H-events_highpri, PID: 82
    Name: cpuhp/7, PID: 83
    Name: idle_inject/7, PID: 84
    Name: migration/7, PID: 85
    Name: ksoftirqd/7, PID: 86
    Name: kworker/7:0H-events_highpri, PID: 88
    Name: kdevtmpfs, PID: 89
    Name: kworker/R-inet_frag_wq, PID: 90
    Name: kauditd, PID: 92
    Name: khungtaskd, PID: 93
    Name: oom_reaper, PID: 94
    Name: kworker/R-writeback, PID: 96
    Name: kcompactd0, PID: 97
    Name: ksmd, PID: 98
    Name: khugepaged, PID: 99
    Name: kworker/R-kintegrityd, PID: 100
    Name: kworker/R-kblockd, PID: 101
    Name: kworker/R-blkcg_punt_bio, PID: 102
    Name: kworker/8:1-events, PID: 103
    Name: irq/9-acpi, PID: 104
    Name: kworker/R-tpm_dev_wq, PID: 108
    Name: kworker/R-ata_sff, PID: 109
    Name: kworker/R-md, PID: 110
    Name: kworker/R-md_bitmap, PID: 111
    Name: kworker/R-edac-poller, PID: 112
    Name: kworker/R-devfreq_wq, PID: 113
    Name: kworker/10:1-cgroup_destroy, PID: 114
    Name: watchdogd, PID: 115
    Name: kworker/9:1H-events_highpri, PID: 116
    Name: kswapd0, PID: 117
    Name: ecryptfs-kthread, PID: 118
    Name: kworker/R-kthrotld, PID: 119
    Name: kworker/R-acpi_thermal_pm, PID: 120
    Name: hwrng, PID: 123
    Name: kworker/R-hfi-updates, PID: 124
    Name: kworker/R-mld, PID: 125
    Name: kworker/R-ipv6_addrconf, PID: 126
    Name: kworker/R-kstrp, PID: 135
    Name: kworker/R-charger_manager, PID: 154
    Name: kworker/0:1H-events_highpri, PID: 155
    Name: kworker/8:1H-events_highpri, PID: 179
    Name: kworker/11:1H-events_highpri, PID: 182
    Name: kworker/2:1H-events_highpri, PID: 197
    Name: kworker/5:1H-events_highpri, PID: 225
    Name: kworker/10:1H-events_highpri, PID: 226
    Name: kworker/6:1H-events_highpri, PID: 227
    Name: kworker/7:1H-kblockd, PID: 228
    Name: kworker/4:1H-events_highpri, PID: 229
    Name: kworker/1:1H-events_highpri, PID: 230
    Name: kworker/3:1H-events_highpri, PID: 231
    Name: kworker/R-nvme-wq, PID: 250
    Name: kworker/R-nvme-reset-wq, PID: 251
    Name: kworker/R-nvme-delete-wq, PID: 252
    Name: kworker/R-nvme-auth-wq, PID: 253
    Name: irq/158-ELAN0788:00, PID: 298
    Name: kworker/5:2-mm_percpu_wq, PID: 301
    Name: jbd2/nvme0n1p7-8, PID: 340
    Name: kworker/R-ext4-rsv-conversion, PID: 341
    Name: systemd-journald, PID: 395
    ...

Show total, used, free, and percentage disk usage.

    $ python3 usage.py
    Total disk space: 143.59 GB
    Used disk space: 69.78 GB
    Free disk space: 66.44 GB
    Disk usage: 51.2%


Display network I/O stats.

    $ python3 net.py
    Network I/O Stats:
    Bytes Sent     : 654.68 MB
    Bytes Received : 880.32 MB
    Packets Sent   : 1100586
    Packets Recv   : 1247983

Fetch https://example.com/ and display headers including content-type, server, etc.

    $ python3 fetch.py
    Response Headers from example.com:

    Content-Type: text/html
    Server: None
    All Headers:
    {'Accept-Ranges': 'bytes', 'Content-Type': 'text/html', 'ETag': '"84238dfc8092e5d9c0dac8ef93371a07:1736799080.121134"', 'Last-Modified': 'Mon, 13 Jan 2025 20:11:20 GMT', 'Vary': 'Accept-Encoding', 'Content-Encoding': 'gzip', 'Content-Length': '648', 'Cache-Control': 'max-age=940', 'Date': 'Mon, 02 Jun 2025 18:19:41 GMT', 'Alt-Svc': 'h3=":443"; ma=93600,h3-29=":443"; ma=93600,quic=":443"; ma=93600; v="43"', 'Connection': 'keep-alive'}

Use your github user api, Extract and print name, public repos, followers.

    $ python3 user.py 
    My GitHub User Info:
    
    Name: Titus James
    Public Repos: 42
    Followers: 16
