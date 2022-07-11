#/usr/bin/env python3
import shutil
import psutil

def check_disk_usage(disk):
    """
    Retornará verdadero si el espacio libre
    es mayor al 20%, falso si es menor al 20%
    """
    du = shutil.disk_usage(disk)
    free = du.free / du.total *100
    return free > 20

def check_cpu_usage():
    """
    Diremos que la máquina está bien si
    el uso de CPU es menor al 75%
    """
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR! ")
else:
    print("Everything is OK!")

