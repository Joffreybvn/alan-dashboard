
let tokenInput = document.getElementById("token")
let sendNotificationInput = document.getElementById("send_notification")

let setInput = (input, value) => {
    input.value = value
}

let setCheckbox = (input, is_checked) => {
    input.checked = is_checked
}

let applySettings = (settings) => {

    // Set the BeCode Token if provided
    if ('becode_token' in settings) {
        setInput(tokenInput, settings['becode_token'])
    }

    // Set send_notification if provided
    if ('send_notification' in settings) {
        setCheckbox(sendNotificationInput, settings['send_notification'])
    }
}

let disableSettings = () => {

    // Disable all settings input
    tokenInput.disabled = true;
    sendNotificationInput.disabled = true;
}

let getSettings = () => {
    // Create and return a settings array

    return {
        "becode_token": tokenInput.value,
        "send_notification": sendNotificationInput.checked
    }
}

export {applySettings, disableSettings, getSettings}