/**
 * @supported 2ABDBE39B3FF 8BCC0A25D731 E3CA0C025E9B
 */

 */

 */

 */

 */

 */

let body = $response.body
body=JSON.parse(body)
body['data']['relates'].forEach((element, index)=> {
   if(element.hasOwnProperty('is_ad')||!element.hasOwnProperty('aid')){      
      body['data']['relates'].splice(index,1)  
    }
})
delete body['data']['cms']
body=JSON.stringify(body)
$done({body})
