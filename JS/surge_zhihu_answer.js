/**
 * @supported 2ABDBE39B3FF 8BCC0A25D731
 */

let body = $response.body
body=JSON.parse(body)
delete body['ad_info']
body['data'].forEach((element, index)=> {
    if(element['author']['name']=="盐选推荐"){ 
          body['data'].splice(index,1)  
     }
 })
body=JSON.stringify(body)
$done({body})
