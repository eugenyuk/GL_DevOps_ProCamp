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
