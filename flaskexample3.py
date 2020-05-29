const express=require('express');
const app=express();
app.get('/',(req,res) => {
    console.log("In get method");
    res.send("In the get method");
});
app.post('/hello',(req,res) =>{
    console.log("I am in POST method");
    res.send("This is POST method");
})
app.listen(8082,() =>console.log("Server started on port 8082"));
