/**
 * @supported 2ABDBE39B3FF 8BCC0A25D731 E3CA0C025E9B
 */

 */

 */

 */

 */

 */

 */

 */

 */

let body = $response.body 
body=JSON.parse(body)
body['sub_webs'].splice(0,1)
body['sub_webs'].splice(1,1)
body=JSON.stringify(body)
$done({body})
