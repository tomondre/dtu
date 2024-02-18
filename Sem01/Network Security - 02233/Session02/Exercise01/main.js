function encrypt(message, key) {
    let encryptedMessage = '';
    for (let i = 0; i < message.length; i++) {
        const charCode = message.charCodeAt(i);
        const encryptedCharCode = charCode + key % 2;
        encryptedMessage += String.fromCharCode(encryptedCharCode);
    }
    return encryptedMessage;
}

function decrypt(encryptedMessage, key) {
    let decryptedMessage = '';
    for (let i = 0; i < encryptedMessage.length; i++) {
        const charCode = encryptedMessage.charCodeAt(i);
        const decryptedCharCode = charCode - key % 2;
        decryptedMessage += String.fromCharCode(decryptedCharCode);
    }
    return decryptedMessage;
}

const message = "Hello, World!";
const key = 0;

const encrypted = encrypt(message, key);
console.log("Encrypted:", encrypted);

const decrypted = decrypt(encrypted, key);
console.log("Decrypted:", decrypted);
