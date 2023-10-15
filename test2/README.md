# Task
* Target website： https://www.endata.com.cn/BoxOffice/BO/Year/index.html
* Task requirement： get the all data of the film rank list
---
# work description
1. There is no data in web source code, it's loaded through ajax.
2. The response is encrypted, so the most difficult is decrypt the response.
3. The web js use these names like _0x91fb5e.
4. I found it that the Object instance 'webDES' is related to decrypt the ciphertext, and it will return the Declassified plaintext.
5. The 'webDES' couldn't find in the initiator of the url requested.
6. I copy many codes that the 'webDES' need. I found it one step by step execute the js-code. Luckly, it's easy to see.
7. Js codes need navigator Object, but it is offered by browser. In my js-code, I defined it, but it couldn't work normally, and leaded to 'web.shell' return a None through a 'if' which need 'navigator'. Damn it.