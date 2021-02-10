

class MainApp extends React.Component
{
    render()
    {
        return(
            <div>
            <Header/><br></br><br></br><br></br><br></br>
            <Form/>
            </div>
        )
    }
}

class Header extends React.Component
{
    render()
    {
        return <div>
            <h1>Heart Failure Prediction</h1>
        </div>
    }  
}

class Form extends React.Component
{
    GetPrediction(e)
    {
        e.preventDefault();
        const array=["age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal"]
        const values=[e.target.age.value,
            e.target.sex.value,
            e.target.cp.value,
            e.target.trestbps.value,
            e.target.chol.value,
            e.target.fbs.value,
            e.target.restecg.value,
            e.target.thalach.value,
            e.target.exang.value,
            e.target.oldpeak.value,
            e.target.slope.value,
            e.target.ca.value,
            e.target.thal.value]
        let url="http://localhost:5000/predict?"
        for(var i=0;i<array.length;i++)
        {
            url+=array[parseInt(i)]+"="+values[i]
            if(parseInt(i)!=array.length-1)
            {
                url+="&"
            }
        }
        const prediction=document.getElementById("prediction");
        prediction.innerHTML="loading...."
        fetch(url,{headers : { 
            'Content-Type': 'application/json'
           }}).then((response)=>
            response.json()).then((data)=>
            {
                if(data.prediction==1)
                {
                    prediction.innerHTML="POSITIVE";
                }

                else
                {
                    prediction.innerHTML="NEGATIVE";
                }
            })
        
        console.log(url);
    }
    render()
    {
        return (
            <div>
                <form method="get" autoComplete="off" onSubmit={this.GetPrediction}>
                    <input id="age" name="age" placeholder="AGE" required/><br></br><br></br>
                    <input id="sex" name="sex" placeholder="SEX" required /><br></br><br></br>
                    <input id="cp" name="cp" placeholder="CP" required/><br></br><br></br>
                    <input id="trestbps" name="trestbps" placeholder="TRESTBPS" required/><br></br><br></br>
                    <input id="chol" name="chol" placeholder="CHOL" required/><br></br><br></br>
                    <input id="fbs" name="fbs" placeholder="FBS" required/><br></br><br></br>
                    <input id="restecg" name="restecg" placeholder="RESTECG" required/><br></br><br></br>
                    <input id="thalach" name="thalach" placeholder="THALACH" required/><br></br><br></br>
                    <input id="exang" name="exang" placeholder="EXANG" required/><br></br><br></br>
                    <input id="oldpeak" name="oldpeak" placeholder="OLDPEAK" required/><br></br><br></br>
                    <input id="slope" name="slope" placeholder="SLOPE" required/><br></br><br></br>
                    <input id="ca" name="ca" placeholder="CA" required/><br></br><br></br>
                    <input id="thal" name="thal" placeholder="THAL" required/><br></br><br></br>
                    <button>PREDICT</button>
                </form>
            </div>
        )
    }
}


const app=document.getElementById("mainform")
ReactDOM.render(<MainApp/>,app)


