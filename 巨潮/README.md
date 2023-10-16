# Task
* Target website： https://webapi.cninfo.com.cn/#/marketDataDate
* Task requirement： 抓取证券代码、证券简称、交易日期、开盘价、最高价、最低价、收盘价、成交数量（股）
---
# work description
* The 'Accept-EncKey' in the requests headers is crypted. This web use crypto-js but the code is obfuscated. 
* Find what function is from crypto-js, and use crypto-js to finish the cryption.