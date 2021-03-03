
const API_URL = "https://api.turingbot.ml"

let post = (url, body) => {
    return fetch(url, {method: "POST", body: JSON.stringify(body)});
}

let requestSettings = (site_token) => {

    // Create the request body
    let body = {
        "token": site_token
    }

    // Send the request
    return new Promise((resolve, reject) => {
        post(API_URL + "/site/", body)

            // Return a response if received
            .then(response => {
                resolve(response)

            // Raise an error if triggered
            }).catch(error => {
                reject(error)
        });
    })
}

export {requestSettings}
