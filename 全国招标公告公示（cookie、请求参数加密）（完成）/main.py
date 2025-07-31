import requests
import  execjs
import  json
import  time
#时效性cookies 已解密
ssxmod_itna  =  execjs.compile(open('G:\\爬虫\\js逆向\\全国招标公告公示（js代码混淆，AST反混淆技术，返回数据已解密）未完成\\cookie_ssxmod_itna加密.js').read()).call('main')
ssxmod_itna2   =  execjs.compile(open('G:\\爬虫\\js逆向\\全国招标公告公示（js代码混淆，AST反混淆技术，返回数据已解密）未完成\\cookie_ssxmod_itna2加密.js').read()).call('main')
timestamp = str(int(time.time()))



cookies = {
    'Hm_lvt_b966fe201514832da03dcf6cbf25b8a2': '1753343508,1753353049,1753671819,1753756897',
    'HMACCOUNT': '68267E256A119B3B',
    'acw_tc': '1a0c655e17538625829908892ee1b5b4350a6de37acb5e19081b783c58fdc3',
    'Hm_lpvt_b966fe201514832da03dcf6cbf25b8a2': timestamp,
    'ssxmod_itna': ssxmod_itna,
    'ssxmod_itna2': ssxmod_itna2 ,
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://ctbpsp.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0',
    'sec-ch-ua': '"Chromium";v="136", "Microsoft Edge";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'Hm_lvt_b966fe201514832da03dcf6cbf25b8a2=1753343508,1753353049,1753671819,1753756897; HMACCOUNT=68267E256A119B3B; acw_tc=1a0c652317537824538125878e0061249f3a1c4d2e17c7b87a153e7a560138; Hm_lpvt_b966fe201514832da03dcf6cbf25b8a2=1753782453; ssxmod_itna=Yq+x9DuQi=YGu4eKxmqBIYDIAPPxnDQKGHDyxWKG7DuxiK08D6QDB446TMYhawpuGNdKCouYqt9xGN4dKxiNDAPq0iDC8WjNtQz0bIP=o0CGP3e9rOiKIOBfnhqd3EjBwb9jLjUZMZSuihrK7eDU4GnD0=xN7eD4R3Dt4DIDAYDDxDWj4DLDYoDYRT5xGpdMQnrXQRTD0YDzqDg4gmdxi3DA4DjUlwQQYq=uDDlR0BQKYUxDYpdxZ07NoeDAqxioGGdx0UaDBLPSt7DGuk0u0Wi6KMpa3RHsPGuDG68ZQ2iArTWPc2p5lUGQ4wmjrjDIGD4BD3Bde7GNQ4sP2DhG6Q+X7GRQDGZinnPxt4DDctRD8zAr/GGCHlAypj5/KrbYDkCGbKi=2uYiGPnY7i+OtRtShtxRFnAqzB4ADPCBt5R5o+DD; ssxmod_itna2=Yq+x9DuQi=YGu4eKxmqBIYDIAPPxnDQKGHDyxWKG7DuxiK08D6QDB446TMYhawpuGNdKCouYqtKxDf1HKOh5GaKQ0iWedFDGN4d+bYucx86tij97F+KqlO+soQ=wq6Y+K9054AwNMSz9FutZiuj7/YfNRGXcQqx37nN5DjNu/0+YwMqSldKMiBwY1mRKNLT5rinEYGDSjRuL46X9i7NqwwGxAqreLaLfenhAF0+27Arhr0DUQmfuz=yujdKLiYc/jb2sHT=PnRL7ABQeTMXYTzjqPQ3q93iVlZ1dHjuxgjRLba/u4uXddjWFwdyO3o7GhrkFE8HutaYsV3QYY+QQrY+5F0D74F1kr=WCzkKhODNBNKGb4O7AwNj+1sQ1OQrUji9xwHOOj2Q6fkDRr6w1DbCGE8Wb=ad1rudGl7jWE4LaIfDsEkSwDY8DrlAB8vAr=rqWA23fQCrOLjEh2ozbrIz4r+PxfEkEu8roOSuO+ppoZpT2W62fi8KYSwh+=4LHWcr24=+d+nqrrmvelqEuQiK=NtrnLRIqFBRm8EsKG4xZ682+HOrrdis1RLEdIqQKfczLd4w8s8Ng88dDLI/F26tGdfzqIjZQtiCzbpPsDTZHGwFwhCF4TfxFsa3pqWw7xSxxMYQtixo3t1vDHdt+ybEsO62xFCxa13QAgCoZ0H/Tzew0YZVYMA5zdG7Tf+ywVt0x7eb0QiDD',
}

for  i  in   range(1,10):
    url  =  f'https://ctbpsp.com/cutominfoapi/recommand/type/5/pagesize/10/currentpage/{i}?province=&industry='
    type_1017  =  execjs.compile(open('G:\\爬虫\\js逆向\\全国招标公告公示（js代码混淆，AST反混淆技术，返回数据已解密）未完成\\main_type_2017.js','r',encoding='utf-8').read()) .call('main_type_1017',url)
    print(type_1017)
    params = {
        'province': '',
        'industry': '',
        'type__1017': type_1017,
    }

    response = requests.get(
        f'https://ctbpsp.com/cutominfoapi/recommand/type/5/pagesize/10/currentpage/{i}',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    # print(response.text)
    # print(response.cookies)
    data  =  json.loads(response.text)
    # print(data)

    data_params  =  execjs.compile(open('G:\\爬虫\\js逆向\\全国招标公告公示（js代码混淆，AST反混淆技术，返回数据已解密）未完成\\des返回值解密.js','r',encoding='utf-8').read()) .call('main123',data)
    print(data_params)