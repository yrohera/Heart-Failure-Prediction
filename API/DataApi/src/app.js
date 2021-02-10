//Required Modules
const express=require('express')
const chalk=require('express')
const fs=require("fs")
const {generate_Key}=require('../Utils/api_key.js')

//Data Retrieve
const GetData=(filePath)=>{
    const Data_Buffer=fs.readFileSync(filePath);
    return JSON.parse(Data_Buffer.toString())
}
const dws=GetData('data/JSON/dws.json')
const ds=GetData('data/JSON/ds.json')

//Setting up the App
const app=express()
const port=process.env.PORT || 3000

//API Key
const api_key=generate_Key()

const SecretKey="Yash_Rohera123"

app.get('/dws_data/'+api_key,(req,res)=>{
    if(req.query)
    {
        const data=fs.readFileSync('data/JSON/dws.json').toString()
        const json=JSON.parse(data)
        if(req.query.age)
        {json.push(req.query)}
        fs.writeFileSync('data/JSON/dws.json',JSON.stringify(json))
    }
    res.send(dws)
})


app.get('/ds_data/'+api_key||SecretKey,(req,res)=>{
    if(req.query)
    {
    const data=fs.readFileSync('data/JSON/ds.json').toString()
    const json=JSON.parse(data)
    if(req.query.age)
    {json.push(req.query)}
    fs.writeFileSync('data/JSON/ds.json',JSON.stringify(json))
    }
    res.send(ds)
})



app.listen(port,(error)=>{
    if(error)
    {
        return console.log("Some Error Occured")
    }

    console.log("Server is up on "+port)
    console.log("API KEY: "+api_key)
})




