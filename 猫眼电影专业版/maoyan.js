var CryptoJS = require("C:\\Users\\God\\AppData\\Roaming\\npm\\node_modules\\crypto-js");

function createOutputMethod(t) {
    var hash = CryptoJS.MD5(t);
    var hexString = hash.toString(CryptoJS.enc.Hex);
    return hexString
}

function get_key() {
    var e = {
        "query": {
            "orderType": 0,
            "uuid": "18b34e9de35c8-08fcca423466f7-745d5774-4b9600-18b34e9de35c8"
        },
        "ua": {
            "isPro": false,
            "isAnd": false,
            "isIos": false,
            "isAndPro": false,
            "isIosPro": false,
            "isIPhoneX": false,
            "isWeChat": false,
            "isMiniprogram": false,
            "isMobile": false,
            "isMaoYan": false,
            "isTuanApp": false,
            "isSamSung": false,
            "isDianping": false,
            "isQQ": false,
            "isBaiduSmart": false,
            "isBaiduMiniprogram": false,
            "isToutiao": false,
            "isWeibo": false,
            "isVivo": false,
            "isGewara": false,
            "isUC": false,
            "isQQBrowser": false,
            "isHuawei": false,
            "isOppo": false,
            "isXiaomi": false,
            "appnm": "moviepro_i",
            "appVersion": null,
            "useKNB": true,
            "isSeries": false,
            "isMeida": false,
            "allowAd": true,
            "noTitle": null,
            "noScheme": false,
            "isPc": true
        },
        "timeStamp": new Date().getTime()
    }

    var d = {
        method: "GET",
        timeStamp: new Date,
        "User-Agent": "TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExOC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTguMC4yMDg4LjQ2",
        index: Math['floor'](1e3 * Math['random']() + 1),
        channelId: e.ua,
        sVersion: 2,
        key: 'A013F70DB97834C0A5492378BD76C53A'
    };
    var t = e.query;
    var c = 'method=GET&timeStamp=' + e.timeStamp + '&User-Agent=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExOC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTguMC4yMDg4LjQ2&index=815&channelId=40009&sVersion=2&key=A013F70DB97834C0A5492378BD76C53A'
    ;
    var key = createOutputMethod(c['replace'](/\s+/g, " "));

    return key
}


