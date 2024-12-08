# max_bitrate.py
#
# Usage: python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz

# Parameters:
#  tx_w
#  tx_gain_db
#  freq_hz
#  dist_km
#  rx_gain_db
#  n0_j
#  bw_hz


# Written by Evan Fillmore

# import Python modules
import sys # argv
import math 

#Constants
c = 2.99792458*10**8

# initialize script arguments
tx_w = float("nan")
tx_gain_db = float("nan")
freq_hz = float("nan")
dist_km = float("nan")
rx_gain_db = float("nan")
n0_j = float("nan")
bw_hz = float("nan")

# parse script arguments
if len(sys.argv)==8:
    tx_w = float(sys.argv[1])
    tx_gain_db = float(sys.argv[2])
    freq_hz = float(sys.argv[3])
    dist_km = float(sys.argv[4])
    rx_gain_db = float(sys.argv[5])
    n0_j = float(sys.argv[6])
    bw_hz = float(sys.argv[7])
else:
    print(\
        'Usage: '\
        'python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz'\
    )
    exit()

# write script below this line
lambd = c/freq_hz
C = tx_gain_db*tx_w*((lambd/(4*math.pi*(dist_km*1000)))**2)*rx_gain_db
N = n0_j*bw_hz
r_max = bw_hz*math.log(1+(C/N),2)

print(math.floor(r_max))