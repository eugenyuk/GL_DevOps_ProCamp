# Print metrics

## General info
This is a script which prints basic information about OS to console.
This is the entry project of GL DevOps ProCamp.

## Technologies
Project is created with:
* Python 3.8
* psutil library
* Docker 19.0.3

## Usage

```
usage: /app/metrics.py (cpu | mem | pids)

Print system utilization metrics.

cpu - print CPU utilization metrics
mem - print RAM utilization metrics
pids - print current running processes info
```

## Setup
To run a script on a host:
```
$ cd Print_Metrics/
$ pip3 install psutil
$ python3 metrics.py (cpu | mem | pids)
```

To run a script within Docker container:
```
$ cd Print_Metrics/
$ docker build -t print_metrics .
$ docker run -it --rm -v $PWD:/app -v /etc/passwd:/etc/passwd:ro --pid=host print_metrics (cpu | mem | pids)
```

## Examples

* print cpu utilization metrics (on a host):
```
$ ./metrics.py cpu
system.cpu.idle 39670.22
system.cpu.user 6557.26
system.cpu.guest 0.0
system.cpu.iowait 1048.69
system.cpu.stolen 0.0
system.cpu.system 2569.34
```

* print mem utilization metrics (using Docker container):
```
$ docker run -it --rm -v $PWD:/app print_metrics mem
virtual total 12461645824
virtual used 4300693504
virtual free 4929290240
virtual shared 782360576
swap total 8589930496
swap used 0
swap free 8589930496
```

* print pids info (on a host):
```
$ ./metrics.py pids
...
    798 avahi           avahi-daemon
    800 root            rngd
    809 rtkit           rtkit-daemon
    816 dbus            dbus-broker-launch
    830 chrony          chronyd
    833 root            abrtd
    835 dbus            dbus-broker
    845 avahi           avahi-daemon
    846 root            abrt-dump-journal-xorg
...
```

* print pids info (within a container):
```
$ docker run -it --rm -v $PWD:/app -v /etc/passwd:/etc/passwd:ro --pid=host metrics pids
...
    798 avahi           avahi-daemon
    800 root            rngd
    809 rtkit           rtkit-daemon
    816 dbus            dbus-broker-launch
    830 chrony          chronyd
    833 root            abrtd
    835 dbus            dbus-broker
    845 avahi           avahi-daemon
    846 root            abrt-dump-journal-xorg
...
```


