import time
import psutil

last_received = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent
last_total = last_received + last_sent

while True:
    bytes_received = psutil.net_io_counters().bytes_recv
    bytes_sent = psutil.net_io_counters().bytes_sent
    bytes_total = bytes_received + bytes_sent

    diff_received = bytes_received - last_received
    diff_sent = bytes_sent - last_sent
    diff_total = bytes_total - last_total

    mb_received = diff_received / 1024 / 1024
    mb_sent = diff_sent / 1024 / 1024
    mb_total = diff_total / 1024 / 1024

    print(f"{mb_received:.2f} MB Received, {mb_sent:.2f} MB Sent, {mb_total:.2f} MB Total")

    last_received = bytes_received
    last_sent = bytes_sent
    last_total = bytes_total

    time.sleep(1)