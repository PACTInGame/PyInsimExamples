import pyinsim

indicator = False

insim = pyinsim.insim(b'127.0.0.1', 29999, Admin=b'')


# Indicators can be turned on with 7,8,9 and turned off with 0 in LFS!


def outgauge_packet(outgauge, packet):
    global indicator

    # Checking for indicator lamp to come on
    if packet.ShowLights & (pyinsim.DL_SIGNAL_L or pyinsim.DL_SIGNAL_R):
        if not indicator:
            indicator = True
            insim.sendm(b"BLINK")
    elif indicator:
        indicator = False


# Initialize OutGauge. Set timeout to 30 seconds.
outgauge = pyinsim.outgauge(b'127.0.0.1', 30000, outgauge_packet, 30.0)

pyinsim.run()
