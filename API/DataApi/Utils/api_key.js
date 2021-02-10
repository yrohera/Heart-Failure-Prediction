const string="A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z";
const string_array=string.split(" ")
const fs=require('fs')

const generate_Key=()=>{
    let api_key=""
    for(var i=0;i<10;i++)
    {
        api_key+=string_array[Math.floor(Math.random()*string_array.length)]
    }    
    for(var i=0;i<10;i++)
    {
        let time=(new Date().getTime().toString())
        api_key+=Math.floor(Math.random()*(time[time.length-1])).toString()+string_array[Math.floor(Math.random()*string_array.length)]
    }
    
    const api={API:api_key}
    fs.writeFileSync("API/api.json",JSON.stringify(api))
    return api_key
}

module.exports={
    generate_Key
}