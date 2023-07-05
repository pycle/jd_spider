

function jd_get_h5st(str){
    CryptoJS = require('crypto-js')


const _appId = 'e1a98',
    fingerprint = "0793240933631978",
    _token = "tk02w9e451c0018nT7OEa4hf4TP6CrvGalyB9pi5vhJWvN7LNhE0ixj5tmclQmf7vcc0nICef618QJP12NjHzZYoyRGW",
    _version = "3.1";

// body
function sha256(text) {
    return CryptoJS.SHA256(text).toString()
}

// str = '{"tenantCode":"jgm","bizModelCode":5,"bizModeClientType":"M","externalLoginType":"1","clientType":"1","version":"v2","skuids":"100022006375,10065934638420,10065932781977,10065932401097,10065932401103,10065932401099,100024739270,10065932401108,10065934638421,10065932781980,10065932781976,10065934638419","debug":"false"}'
// data = sha256(str)
// console.log(data)

// collect
function collect() {
    let text = {
        "sua": "Linux; Android 6.0; Nexus 5 Build/MRA58N",
        "pp": {},
        "fp": fingerprint
    }
    let iv = CryptoJS.enc.Utf8.parse('0102030405060708'), // 偏移量
        key = CryptoJS.enc.Utf8.parse('wm0!@w_s#ll1flo('), // key
        data = CryptoJS.enc.Utf8.parse(JSON.stringify(text, null, 2));  // data
    aes = CryptoJS.AES.encrypt(data, key, {
        iv: iv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    return aes.ciphertext.toString()//aes.toString()

}

// a = collect()
// console.log(a)


// jd
function jd() {
    var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : Date.now()
        , t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : "yyyy-MM-dd"
        , r = new Date(e)
        , n = t
        , i = {
        "M+": r.getMonth() + 1,
        "d+": r.getDate(),
        "D+": r.getDate(),
        "h+": r.getHours(),
        "H+": r.getHours(),
        "m+": r.getMinutes(),
        "s+": r.getSeconds(),
        "w+": r.getDay(),
        "q+": Math.floor((r.getMonth() + 3) / 3),
        "S+": r.getMilliseconds()
    };
    return /(y+)/i.test(n) && (n = n.replace(RegExp.$1, "".concat(r.getFullYear()).substr(4 - RegExp.$1.length))),
        Object.keys(i).forEach(function (e) {
            if (new RegExp("(".concat(e, ")")).test(n)) {
                var t = "S+" === e ? "000" : "00";
                n = n.replace(RegExp.$1, 1 == RegExp.$1.length ? i[e] : "".concat(t).concat(i[e]).substr("".concat(i[e]).length))
            }
        }),
        n
}

// h5st

function h5st(t, r) {
    let s = Date['now'](),
        h = _appId,
        p = fingerprint,
        l = jd(s, 'yyyyMMddhhmmssSSS'),
        d = _token;
    let o = CryptoJS.HmacMD5(`${d}${p}${l}${h}eg4AqP30r1Cy`, d).toString()
    //let o = sha256(`${d}${p}${l}${h}eg4AqP30r1Cy`)
    console.log(`o ---> ${o}`)
    let join_text = ""
    t.forEach(function (element) {
        join_text = join_text + "&" + element.key + ":" + element.value
    });

    let A = CryptoJS.HmacSHA256(join_text.slice(1), o).toString(CryptoJS.enc.Hex)
    console.log(`A ---> ${A}`)
    let x = [""['concat'](l), ""['concat'](fingerprint), ""['concat'](_appId), ""['concat'](_token), "".concat(A), ""['concat'](_version), ""['concat'](s), ""['concat'](r)].join(";");
    console.log(`x ---> ${x}`)
    return x
    // 'appid:jd-cphdeveloper-m&body:0e9c74a186d8a8d37f812f418aa221fe72c5a926c3d3b2093338276cf96ec345&functionId:m_search_promise_realtime'
}


// str = '{"tenantCode":"jgm","bizModelCode":5,"bizModeClientType":"M","externalLoginType":"1","clientType":"1","version":"v2","skuids":"100022006375,10065934638420,10065932781977,10065932401097,10065932401103,10065932401099,100024739270,10065932401108,10065934638421,10065932781980,10065932781976,10065934638419","debug":"false"}'
body = sha256(str)
// console.log(data)


t = [
    {
        "key": "appid",
        "value": "jd-cphdeveloper-m"
    },
    {
        "key": "body",
        "value": body
    },
    {
        "key": "functionId",
        "value": "m_search_promise_realtime"
    }
]
r = collect()
// console.log(`collect --> ${r}`)
return h5st(t, r)

}