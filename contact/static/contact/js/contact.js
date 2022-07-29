import {init as ejsInit, send as ejsSend} from 'https://cdn.jsdelivr.net/npm/@emailjs/browser@3/dist/email.min.js'

const email = document.getElementById('emailInput').innerHTML;
const message = document.getElementById('messageInput').innerHTML;
const name = document.getElementById('nameInput').innerHTML;

let formParams = {
    email: email,
    message: message,
    name: name,
}

(function () {
  ejsInit("XJZv54FJVNguUwp1E");
})();

$("#contactSubmit").on("click", ejsSend("service_rvciip4", "template_3whq2oq", formParams));
