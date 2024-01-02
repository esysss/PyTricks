import time
import os
print(os.getcwd())
os.mkdir('new')
time.sleep(2)
os.rename('new','new2')
time.sleep(2)
os.rmdir('new2')