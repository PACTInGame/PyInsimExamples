import pyinsim


def message_out(insim, mso):
    # Print out the MSO message.
    # Note: ^L means Latin character, ^J japanese etc... ^0-^9 refer to colors.
    print(mso.Msg)


def insim_state(insim, sta):
    print(b"Currently driving on Track: " + sta.Track)


# Init new InSim object.
insim = pyinsim.insim(b'127.0.0.1', 29999, Admin=b'')

# Bind ISP_MSO packet to message out method.
insim.bind(pyinsim.ISP_MSO, message_out)
# Bind ISP_STA packet to insim state method.
insim.bind(pyinsim.ISP_STA, insim_state)

# Start pyinsim.
pyinsim.run()
