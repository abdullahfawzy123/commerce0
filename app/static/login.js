document.addEventListener('DOMContentLoaded', () => {

  alert("ff");
  document.querySelector('#button').onclick = () => {

     username = document.querySelector('#username').value ;
     password = document.querySelector('#password').value ;

    if (username.length < 10) {
      alert("username must be at least 10 characters");
}

    else if (password.length < 10) {
      alert("password must be at least 10 characters ");
}

})
