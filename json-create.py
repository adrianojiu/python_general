# -*- coding: utf-8 -*-
import pandas as pd
from IPython.display import display
import mpu

# Manipulete files using pandas, creating json output based in a Excel file.

efile = r"C:\Temp\jsonchannels.xlsx"
ch_excel = pd.read_excel(efile)

for eindex in ch_excel.index:
    eid = ch_excel["id"][eindex]
    eidstr = str(eid)
    echannel = ch_excel["channel"][eindex]
    echannel_replace_dash =  str(echannel.replace(" ", "-").replace("í", "i")).lower()
    echannel_replace_under = str(echannel.replace(" ", "_").replace("í", "i")).lower()
    eimage = ch_excel["image"][eindex]

    output_channel = \
    " " +'"'+echannel_replace_under+'"'": { \
            "+'"'+'id'+'"'": 0, \
            "+'"'+'liveId'+'"'": "+eidstr+", \
            "+'"'+'name'+'"'": "+'"'+echannel+'"'" , \
            "+'"'+'channelName'+'"'": "+'"'+echannel_replace_dash+'"'", \
            "+'"'+'type'+'"'": "+'"''olympics''"'", \
            "+'"'+'source'+'"'": "+'"''globosat''"'", \
            "+'"'+'maxStreams'+'"'": 0, \
            "+'"'+'logo'+'"'": "+'"''/img/channels/'""+eimage+'"'" , \
            "+'"'+'channelLogo'+'"'": "+'"''sportv''"'", \
            "+'"'+'stamp'+'"'": null, \
            "+'"'+'isHd'+'"'": false, \
            "+'"'+'hasLive'+'"'": false, \
            "+'"'+'is4GFree'+'"'": false, \
            "+'"'+'hasAdvertising'+'"'": false, \
            "+'"'+'showChannelContent'+'"'": false \
        }, "
    
    display(output_channel)

    #mpu.io.write('channels-teste.json', output_channel)

