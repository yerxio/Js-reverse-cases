# Task
* Target website： https://www.chinaindex.net/ranklist/4
* Task requirement： get the all data of film list
---
# work description
1. There is no data in web source code, it's loaded through ajax.
2. The response i get is encrypt, so the most difficult is decrypt the response.
3. I found it that the js-funtion 'dataFilter' is related to decrypt the ciphertext, and it will return the Declassified plaintext.
4. I copy many codes that the 'ciphertext' need, and run 'ciphertext' to get the plaintext. 
5. But not completely execute 'dataFilter' could get the plaintext.
6. There is .AES and '...cryptor', but perhaps it's work not the key for decrypt work. haha..
