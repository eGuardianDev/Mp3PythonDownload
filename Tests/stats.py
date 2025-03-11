import os, time
from stat import * # ST_SIZE etc

# try:
#     st = os.stat("Empire Fall - Losing It (Official Visualizer).mp3")
# except IOError:
#     print( "failed to get information")
# else:
#     print ("file size: ")
#     print(  st[ST_SIZE])
#     print ("file modified:")
#     print(time.asctime(time.localtime(st[ST_MTIME])))