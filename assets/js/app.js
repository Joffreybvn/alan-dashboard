
import {retrieveToken} from './modules/url.js'
import {requestSettings} from './modules/request.js'

export function main() {

    let site_token = retrieveToken()

    requestSettings(site_token).then((response) => {
        console.log(response)
    })
}

window.addEventListener("load", main);


