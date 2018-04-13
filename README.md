Dixon Styres

secuPy



AI Tool to analyze network traffic in the effort to detect botnets.

secuPy uses KNN clasification to identify Botnet traffic on a psuedo live network setting. The classifier is trained on the CTU-13 dataset specifically in scenario 1 with the Neris Botnet. 

Built with python 2.7


loader.py: loads in an Argus binetflow and converts relevant features to numpy arrays/pickles

model.py: KNN model

start.py: Train model and listen for network traffic to classify

TCPServer.py: Threaded TCPServer to send Argus logs that have been run through data.py into our listener.
