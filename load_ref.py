# -*- coding: utf-8 -*-

import sys
import json
from pprint import pprint

wav_base_dir = "/nfs/yzhdong/data/wav/yue/heisenberg/"
scp_base_dir = "/nfs/yzhdong/data/scp/yue/heisenberg/"

id_dic = { "content": "yue.transcript",
           "user_id": "yue.speakerid" }
           
scp_wav_file = "yue-wav.scp"

with open('reference-content.json.0925') as data_file:    
    data = json.load(data_file)

def dump_wav_scp(outfile):
    print outfile
    res = []
    for uid in data.keys():
        value = "{}{}{}".format(wav_base_dir, uid.encode('utf-8'), ".raw.wav")
        res.append("{} {}\n".format(uid, value))
    out = open(outfile, "w")

    for line in res:
        out.write(line)
    out.close()
                 
def dump(key_name, outfile):
    print outfile
    res = []
    for uid in data.keys():
        value = data[uid][key_name]
        res.append("{} {}\n".format(uid.encode('utf-8'), value.encode('utf-8')))

    out = open(outfile, "w")

    for line in res:
        out.write(line)
    out.close()

if __name__ == "__main__":
    date = sys.argv[1]
    for key in id_dic:
        dump(key, "{}{}-{}".format(scp_base_dir, date, id_dic[key]))
    dump_wav_scp("{}{}-{}".format(scp_base_dir, date, scp_wav_file))
    
