
let retrieveToken = () => {

    // Get the hash
    let hash = location.hash;

    // Return the token part
    return hash.substring(1)
}

export {retrieveToken}