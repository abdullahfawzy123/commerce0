document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('#button').onclick = () => {

     username = document.querySelector('#username').value ;
     email = document.querySelector('#email').value ;
     password = document.querySelector('#password').value ;
     c_password = document.querySelector('#c_password').value ;


    if (username.length < 10) {
      alert("username must be at least 10 characters");
}

    else if (email.length < 25) {
      alert("email must be at least 25 characters");
}

    else if (password.length < 10) {
      alert("password must be at least 10 characters ");
}
    else if (c_password.length < 10) {
      alert("confirm password must be at least 10 characters ");
}
    else if (password != c_password) {
      alert("password doesn't match");
}

}
})
