/**
 * @supported 2ABDBE39B3FF
 */

let body = $response.body
body=JSON.parse(body)
delete body['data']['notice']
body=JSON.stringify(body)
$done({body})
