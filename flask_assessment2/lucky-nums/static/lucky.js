/** processForm: get data from form and make AJAX call to our API. */

async function processForm(evt) {
    evt.preventDefault()
    let name= $("#name").val()
    let email = $("#email").val()
    let year = $("#year").val()
    let color = $("#color").val()

    let resp = await axios.post("http://127.0.0.1:5000/api/get-lucky-num", {name:name,year:year,color:color})
    console.log(resp)
    handleResponse(resp)

}

/** handleResponse: deal with response from our lucky-num API. */

function handleResponse(resp) {
    if (resp.data.errors){
        console.log(resp.data)
        console.log(resp.data.errors)
        for (let error of Object.values(resp.data.errors)){
        $("#lucky-results").append(`<p>${error}</p>`)
        console.log(error)}
    
        
    }
    $("#lucky-results").append(`<p>Your lucky number is ${resp.data.num.num}! ${resp.data.num.fact}</p>`)
    $("#lucky-results").append(`<p>Your birth year is ${resp.data.year.year}! ${resp.data.year.fact}</p>`)   
}


$("#lucky-form").on("submit", processForm);
