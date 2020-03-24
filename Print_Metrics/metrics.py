#!/usr/bin/env python3
#
# Script prints system utilization metrics

import psutil
import sys
import textwrap

ARG = 0


def print_usage_exit():
    msg = """\
            usage: {} (cpu | mem | pids)

            Print system utilization metrics.

            cpu - print CPU utilization metrics
            mem - print RAM utilization metrics
            pids - print current running processes info
            """.format(sys.argv[0])

    # textwrap.dedent removes leading spaces from msg
    print(textwrap.dedent(msg))
    sys.exit(1)

def validate_arg():
    if len(sys.argv) == 2:
        global ARG
        ARG = sys.argv[1]
    else:
        print_usage_exit()

    if ARG not in ('cpu', 'mem', 'pids'):
        print_usage_exit()

def print_cpu_metrics():
    cpu_metrics = psutil.cpu_times()
    #print(cpu_metrics)
    print("system.cpu.idle {}".format(cpu_metrics.idle))
    print("system.cpu.user {}".format(cpu_metrics.user))
    print("system.cpu.guest {}".format(cpu_metrics.guest))
    print("system.cpu.iowait {}".format(cpu_metrics.iowait))
    print("system.cpu.stolen {}".format(cpu_metrics.steal))
    print("system.cpu.system {}".format(cpu_metrics.system))

def print_mem_metrics():
    mem_metrics = psutil.virtual_memory()
    swap_metrics = psutil.swap_memory()
    #print(mem_metrics)
    #print(swap_metrics)
    print("virtual total {}".format(mem_metrics.total))
    print("virtual used {}".format(mem_metrics.used))
    print("virtual free {}".format(mem_metrics.free))
    print("virtual shared {}".format(mem_metrics.shared))
    print("swap total {}".format(swap_metrics.total))
    print("swap used {}".format(swap_metrics.used))
    print("swap free {}".format(swap_metrics.free))

def print_pids():
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        print("{:7} {:15} {}".format(proc.info['pid'], \
                                     proc.info['username'], \
                                     proc.info['name']))

def main():
    validate_arg()
    if ARG == 'cpu':
        print_cpu_metrics()
    elif ARG == 'mem':
        print_mem_metrics()
    elif ARG == 'pids':
        print_pids()

    return 0

if __name__ == '__main__':
    sys.exit(main())
