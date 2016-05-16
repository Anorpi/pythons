HOST='192.168.1.1'
sotr='GET /chat HTTP/1.1\r\n'
sotr+='Host: '+HOST+':8080\r\n'
sotr+='User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0\r\n'
sotr+='Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n'
sotr+='Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3\r\n'
sotr+='Accept-Encoding: gzip, deflate\r\n'
sotr+='Sec-WebSocket-Version: 13\r\n'
print sotr
