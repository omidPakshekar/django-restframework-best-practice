const contentContainer = document.getElementById('content-container')
const loginForm = document.getElementById('login-form')
const SearchForm = document.getElementById('search-form')

const baseEndpoint = "http://localhost:8000/api"

if (loginForm) {
    loginForm.addEventListener('submit', handleLogin)
}

if (SearchForm) {
    SearchForm.addEventListener('submit', handleSearch)
}



function handleLogin(event){
    console.log(event)
    event.preventDefault()
    const loginEndpoint = `${baseEndpoint}/token/`
    let loginFormData  = new FormData(loginForm)
    let loginObjectData = Object.fromEntries(loginFormData)
    console.log(loginObjectData);
    const options = {
        method: "POST",
        headers : {
            "Content-Type" : "application/json"            
        },
        body: JSON.stringify(loginObjectData)
    }
    // request.POST
    fetch(loginEndpoint, options) //promise
    .then(response => {
        console.log(response);
        return response.json()
    })
    .then(authData => {
        handleAuthData(authData, getProductList)
    }
       
    )
    .catch( err => {
        console.log('err', err);
    })
}


function handleSearch(event){
    console.log(event)
    event.preventDefault()
    let formData  = new FormData(SearchForm)
    let data = Object.fromEntries(formData)
    let searchParams = new URLSearchParams(data)
    
    const endpoint = `${baseEndpoint}/search/?${searchParams}`
    
    const headers = {
        "Content-Type" : "application/json",
    }
    const authToken = localStorage.getItem('access')
    console.log("authToken", authToken);
    if (authToken){
        headers['Authorization'] = `Bearer ${authToken}`
    }
    const options = {
        method: "GET",
        headers : headers

    }
    // request.POST
    fetch(endpoint, options) //promise
    .then(response => {
        console.log(response);
        return response.json()
    })
    .then(data => {
        const validData = isTokenNotValid(data)
        if (validData && contentContainer){
            contentContainer.innerHTML = ""
            if (data && data.hits){
                let htmlStr = ""
                for(let result of data.hits){
                    htmlStr += "<li>" + result.title + "</li>"
                    console.log("htmlstr ", htmlStr);
                }
                contentContainer.innerHTML = htmlStr
                if (data.hits.length == 0){
                    contentContainer.innerHTML = "<p>no results found</p>"
                }
            } else {
                contentContainer.innerHTML = "<p>no results found</p>"
            }
        }
        
    
    }
       
    )
    .catch( err => {
        console.log('err', err);
    })
}


function handleAuthData(authData, callback) {
    localStorage.setItem('access', authData.access)
    localStorage.setItem('refresh', authData.refresh)
    if (callback){
        callback()
    }
}
function getFetchOptions(method, body) {
        return  {
        method: method === null ? "GET" : method,
        headers : {
            "Content-Type" : "application/json",            
            "Authorization" : `Bearer ${localStorage.getItem('access')}`
        }, 
        body : body ? body : null
    }
}
function writeToContainer(data) {

    if (contentContainer){
        contentContainer.innerHTML = "<pre>" + JSON.stringify(data, null, 4) + "</pre>"
    }
    
}

function isTokenNotValid(jsonData) {
    if (jsonData.code && jsonData.code === 'token_not_valid'){
        // run a refresh token fetch
        alert('please login again')
        return false
    }
    return true
}

function getProductList() {
    const endpoint = `${baseEndpoint}/products/`
    const options = getFetchOptions()
    fetch(endpoint, options) //promise
    .then(response =>  response.json())
    .then(data => {
        console.log(data);
        const validData = isTokenNotValid(data)
        if (validData){
            writeToContainer(data)
        }
    })
    .catch( err => {
        console.log('err', err);
    })

}


function validJWTToken() {
    const endpoint = `${baseEndpoint}/token/verify/`
    const options = {
        method: "POST",
        headers : {
            "Content-Type" : "application/json"            
        },
        body: JSON.stringify({
            token: localStorage.getItem('access')
        })
    } 
    fetch(endpoint, options)
    .then(response => response.json())
    .then(
        x=>{
            //refresh
        }
    ) 
}


const searchClient = algoliasearch('OK09IW9FRF', 'dbe4ec98dd2b5ed94813490d6c531621');

   
const search = instantsearch({
  indexName: 'cfe_Product',
  searchClient,
});

search.addWidgets([
  instantsearch.widgets.searchBox({
    container: '#searchbox',
  }),

  instantsearch.widgets.refinementList({
    container: "#user-list",
    attribute : 'user'
  }),

  instantsearch.widgets.refinementList({
    container: "#public-list",
    attribute : 'public'
  }),

  instantsearch.widgets.clearRefinements({
    container: "#clear-refinements"
  }),

  instantsearch.widgets.hits({
    container: '#hits',
    templates: {
        item: `
            <div>
            <div>{{#helpers.highlight}}{"attribute" : "title"}{{/helpers.highlight}}</div> 
                <div>{{ body }}</div>
                <div>{{price}} {{ user }}</div>
            </div>`
        
        
    }
  })
]);

search.start();


