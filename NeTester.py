import pyspeedtest
from plyer import notification
import time
st=(pyspeedtest.SpeedTest())
ping1=st.ping()
down1=st.download()
up1=st.upload()
down2=down1/1000000
up2=up1/1000000
down2=round(down2,2)
up2=round(up2,2)
ping1=round(ping1,2)
print("""

.oPYo. 8                    8 .oPYo.         d'b   o                                
8    8 8                    8 8              8     8                                
8      8 .oPYo. o    o .oPYo8 `Yooo. .oPYo. o8P   o8P o   o   o .oPYo. oPYo. .oPYo. 
8      8 8    8 8    8 8    8     `8 8    8  8     8  Y. .P. .P .oooo8 8  `' 8oooo8 
8    8 8 8    8 8    8 8    8      8 8    8  8     8  `b.d'b.d' 8    8 8     8.     
`YooP' 8 `YooP' `YooP' `YooP' `YooP' `YooP'  8     8   `Y' `Y'  `YooP8 8     `Yooo' 
:.....:..:.....::.....::.....::.....::.....::..::::..:::..::..:::.....:..:::::.....:
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

""")
time.sleep(3)
mesaj2 = """
+-----------------------------------+
.---.  _                            |
: .; ::_;                |::::::::::|            
:  _.'.-.,-.,-. .--.     |::::::::::|
: :   : :: ,. :' .; :      {} Ms
:_;   :_;:_;:_;`._. ;    |::::::::::| 
                .-. :    |::::::::::|
                `._.                |
""".format(ping1)
mesaj3 = """
+--------------------------------------------------+
.-..-.      .-.                  .-.               |
: :: :      : :                  : :    |::::::::::|  
: :: :.---. : :   .--.  .--.   .-' :    |::::::::::|
: :; :: .; `: :_ ' .; :' .; ; ' .; :      {} Mbps
`.__.': ._.'`.__;`.__.'`.__,_;`.__.'    |::::::::::|
      : :                               |::::::::::|
      :_;                                          |
""".format(up2)
mesaj4 = """
+-----------------------------------------------------------------+
.---.                      .-.                  .-.    |::::::::::|
: .  :                     : :                  : :    |::::::::::|
: :: : .--. .-..-..-.,-.,-.: :   .--.  .--.   .-' :     {} Mbps
: :; :' .; :: `; `; :: ,. :: :_ ' .; :' .; ; ' .; :    |::::::::::|
:___.'`.__.'`.__.__.':_;:_;`.__;`.__.'`.__,_;`.__.'    |::::::::::|
------------------------------------------------------------------+                                                                                                                       
""".format(down2)
print(""+mesaj2+" "+mesaj3+" "+mesaj4+"")
speedg = down2
speed = speedg // 8
son = speed * 1024
time = 1024 * 1024 // son
dk = str(int(time // 60))
nea = down2
neas = str(int(nea // 8.000))
aa = ("""
+----------------------------------+
Ping = {} Ms                    |
-----------------------------------+
Upload = {} Mbps                 |
-----------------------------------+
Download = {}Mbps """+neas+""" Mb          |
-----------------------------------+
1Gb = """+dk+""" Minutes                    |
-----------------------------------+
""").format(ping1, up2, down2)
print(aa)
title = "Cloud Software Speed Tester"
message=("Ping = {} Ms\nUpload = {} Mbps\nDownload = {} Mbps "+neas+" Mb\n1Gb = "+dk+" Dk").format(ping1, up2, down2)
notification.notify(title=title,
                    message=message,
                    app_icon=None,
                    timeout=9,
                    toast=False)
