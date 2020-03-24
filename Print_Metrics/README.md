# Metrics Collection

## General info
This is a script which prints basic information about OS to console.
This is the entry project of GL DevOps ProCamp.

## Technologies
Project is created with:
* Python 3.8
* psutil library
	
## Setup
To run a script directly:
```
$ cd Print_Metrics/
$ pip3 install psutil
$ python3 metrics.py (cpu | mem)
```

To run a script in a Docker container:
```
$ cd Print_Metrics/
$ docker build -t print_metrics .
$ docker docker run -it --rm -v $PWD:/app print_metrics (cpu | mem)
```

## Examples

* print cpu utilization metrics (directly):
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
