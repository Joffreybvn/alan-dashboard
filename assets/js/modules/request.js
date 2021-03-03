
const API_URL = "https://alandashboard.joffreybvn.be"

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

            // Check if a response is received
            .then(async response => {
                let json = await response.json()

                // If the status is true, return the settings
                if (json['status']) {
                    resolve([json['access_token'], json['settings']])
                }

                // If not, raise the error message
                else {
                    reject(json['message'])
                }
            }).catch(() => reject(false))
    })
}

let sendSettings = (access_token, settings) => {

    // Create the request body
    let body = settings
    body['access_token'] = access_token

    // Send the request
    return new Promise((resolve, reject) => {
        post(API_URL + "/settings/", body)

            // Check if response is received
            .then(async response => {
                resolve(true)
            })

            .catch((error) => {
                console.log(error)
                reject(error)
            })
    })
}

export {requestSettings, sendSettings}
