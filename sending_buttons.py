
import pyinsim

# Init new InSim object.
insim = pyinsim.insim(b'127.0.0.1', 29999, Admin=b'')

# Send BTN packets with the message 'Hello, InSim!' to the game.
insim.send(pyinsim.ISP_BTN, ReqI=255, ClickID=1, BStyle=pyinsim.ISB_LIGHT, T=119, L=90, W=20, H=10,
           Text=b"Hello, Insim")

insim.send(pyinsim.ISP_BTN, ReqI=255, ClickID=2, BStyle=pyinsim.ISB_LIGHT, T=129, L=90, W=20, H=10,
           Text=b"^1Hello, Red Insim")

insim.send(pyinsim.ISP_BTN, ReqI=255, ClickID=3, BStyle=pyinsim.ISB_LIGHT, T=139, L=90, W=20, H=10,
           Text=b"^4Hello, Blue Insim")

insim.send(pyinsim.ISP_BTN, ReqI=255, ClickID=4, BStyle=pyinsim.ISB_DARK, T=109, L=90, W=20, H=10,
           Text=b"^7Hello, Dark Insim")

insim.send(pyinsim.ISP_BTN, ReqI=255, ClickID=5, BStyle=pyinsim.ISB_LMB, T=99, L=90, W=30, H=10,
           Text=b"^7Hello, Transparent Insim")

# Start pyinsim.
pyinsim.run()
