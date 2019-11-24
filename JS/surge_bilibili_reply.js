/**
 * @supported 2ABDBE39B3FF 8BCC0A25D731
 */



let body = $response.body
body=JSON.parse(body)
delete body['data']['notice']
body=JSON.stringify(body)
$done({body})
