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
### On host:
```
$ cd Print_Metrics/
$ pip3 install psutil
$ python3 metrics.py cpu # or mem, or pids
```

### Within Docker container:
```
$ cd Print_Metrics/
$ docker build -t print_metrics .
$ docker run -it --rm -v $PWD:/app -v /etc/passwd:/etc/passwd:ro --pid=host print_metrics cpu # or mem, or pids
```
Some Docker options clarification: 

`-v $PWD:/app` - this option mounts current directory (which should be Print_Metrics/) as a volume into container's /app directory. So we can edit our script on a host and all changes are provisioned to a container instantly.

`-v /etc/passwd:/etc/passwd:ro` - this option mounts /etc/passwd file from host into a container in read-only mode. Need for `pids` metric to display usernames for processes running on the host machine from within the container.

`--pid=host` - this option allows to share host's PID namespace with the container. Need for `pids` metric to display information about processes running on the host machine from within the container.


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


