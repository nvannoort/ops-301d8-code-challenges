#!/usr/bin/env python3

# Script Name:                  Ops301d8 Day 11
# Author:                       Your Name: Nick Van Noort
# Date of latest revision:      06/13/2023
# Purpose:                      psutil in Python

import psutil

def fetch_cpu_times():
    cpu_times = psutil.cpu_times()

    print(f"Time spent by normal processes executing in user mode: {cpu_times.user} seconds")
    print(f"Time spent by processes executing in kernel mode: {cpu_times.system} seconds")
    print(f"Time when system was idle: {cpu_times.idle} seconds")
    print(f"Time spent by priority processes executing in user mode (nice): {cpu_times.nice} seconds")
    print(f"Time spent waiting for I/O to complete: {cpu_times.iowait} seconds")
    print(f"Time spent for servicing hardware interrupts: {cpu_times.irq} seconds")
    print(f"Time spent for servicing software interrupts: {cpu_times.softirq} seconds")
    print(f"Time spent by other operating systems running in a virtualized environment: {cpu_times.steal} seconds")
    print(f"Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel: {cpu_times.guest} seconds")

fetch_cpu_times()

# done