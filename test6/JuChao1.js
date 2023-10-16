var CryptoJS = require('crypto-js');
function tEKkv(_0x60c3f3, _0x1beeba) {
            return _0x60c3f3 / _0x1beeba;
        };
function gxgNE(_0x5d0c06, _0x5c2e80) {
                        return tEKkv(_0x5d0c06, _0x5c2e80);
                    };
function getResCode() {
                        var
                           _0xfc0ed3 = CryptoJS.AES.encrypt(CryptoJS.enc.Utf8.parse(Math['floor'](gxgNE(new Date()['getTime'](), 0xab5 + -0x1cb2 + -0x1 * -0x15e5))), CryptoJS.enc.Utf8.parse('1234567887654321' || "1234567887654321"), {
                            'iv': CryptoJS.enc.Utf8.parse('1234567887654321'),
                            'mode': CryptoJS.mode.CBC,
                            'padding': CryptoJS.pad.Pkcs7
                        });
                        return CryptoJS.enc.Base64.stringify(_0xfc0ed3['ciphertext']);
                    }
                    ;
return getResCode()