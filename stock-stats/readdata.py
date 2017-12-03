import pymongo
import matplotlib.pyplot as plt
from datetime import datetime
# reference official site : https://matplotlib.org/gallery/index.html
client = pymongo.MongoClient('localhost', 27017)
db = client["Stock"]  # equal to : client.Stock
col = db["AllTradeEveryDay"]  # equal to: db.AllTradeEveryDay

sh = []
sz = []
dt = []
off = []
allin = []
for i in col.find({}, {"Date": 1, "SHDealAmount": 1, "SZDealAmount": 1, "AmountOffset": 1}):
    sid = str(i["Date"])
    # print sid
    dt.append(datetime.strptime(sid, '%Y%m%d'))
    sh.append(i["SHDealAmount"])
    sz.append(i["SZDealAmount"])
    # print sid
    # print type(float(i["SZDealAmount"]) - float(i["SHDealAmount"]))
    off.append(float(i["SZDealAmount"]) - float(i["SHDealAmount"]))
    if "AmountOffset" in i:
        allin.append(i["AmountOffset"])
    else:
        allin.append(0)


fig = plt.figure(num=None, figsize=(23, 11))
plt.plot(dt, sh, 'ro-', label='SH Amount', linewidth=0.5)
plt.plot(dt, sz, 'g*-',  label='SZ Amount', linewidth=0.5)
plt.plot(dt, off, 'b*-',  label='SZAmount-SHAmount', linewidth=0.5)
plt.plot(dt, allin, 'y-',  label='Total Money In', linewidth=0.5)
# plt.axis('auto')

plt.legend()
plt.title("China Stock Deal Amount")
plt.grid(True, linestyle="-.", color="k", linewidth="1")
plt.show()
