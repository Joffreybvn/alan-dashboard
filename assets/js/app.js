
import {retrieveToken} from './modules/url.js'
import {requestSettings, sendSettings} from './modules/request.js'
import {applySettings, disableSettings, getSettings} from './modules/form.js'

const SITE_URL = "https://turingbot.ml/"
let saveButton = document.getElementById('save')

export function main() {

    // Get the site token
    let site_token = retrieveToken()
    let access_token;

    // Use it to retrieve the user settings
    requestSettings(site_token).then((result) => {

        // Get the token and settings
        let token, settings
        [token, settings] = result

        // Save the access token and display the settings
        access_token = token
        applySettings(settings)

    }).catch((message) => {
        //document.location.href= SITE_URL + "error.html"
    })

    // Triggered when the user save
    saveButton.addEventListener('click', () => {

        // Disable the inputs
        disableSettings()

        // Send the new settings
        sendSettings(access_token, getSettings()).then(() => {
            // document.location.href= SITE_URL + "confirm.html"
        })
    })
}

window.addEventListener("load", main);



