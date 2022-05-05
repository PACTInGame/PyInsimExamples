import pyinsim

# Initialize the InSim system
insim = pyinsim.insim(b'127.0.0.1', 29999, Admin=b'')

# Send message 'Hello, InSim!' to the game
insim.sendm(b'Hello, InSim!')

# Start pyinsim.
pyinsim.run()