/**
 * @supported 2ABDBE39B3FF 8BCC0A25D731 E3CA0C025E9B
 */

 */

let body = $response.body
body=JSON.parse(body)
body['data'].forEach((element, index)=>{
     if(element.hasOwnProperty('ad')){      
       body['data'].splice(index,1)  
    }
})
body=JSON.stringify(body)
$done({body})
