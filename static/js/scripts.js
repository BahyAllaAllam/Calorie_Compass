// Show password button
document.addEventListener('DOMContentLoaded', function() {
    // Toggle password visibility and change the icon
    const eyeIcon = document.getElementById('eye-icon');
    const eyeIcon_oldpassword = document.getElementById('eye-icon-oldpassword');
    const oldpasswordField = document.getElementById('id_oldpassword');
    let passwordField;
    if (document.getElementById('id_password')) {
        passwordField = document.getElementById('id_password')
    } else {
        passwordField = document.getElementById('id_password1')
    }
    if (eyeIcon){
        eyeIcon.addEventListener('click', function() {
            if (passwordField.type === 'password') {
                passwordField.type = 'text';
                eyeIcon.classList.remove('fa-eye');
                eyeIcon.classList.add('fa-eye-slash'); // Change to eye-slash icon
            } else {
                passwordField.type = 'password';
                eyeIcon.classList.remove('fa-eye-slash');
                eyeIcon.classList.add('fa-eye'); // Change back to eye icon
            }
        });
    }
    if (eyeIcon_oldpassword){
        eyeIcon_oldpassword.addEventListener('click', function() {
            if (oldpasswordField.type === 'password') {
                oldpasswordField.type = 'text';
                eyeIcon_oldpassword.classList.remove('fa-eye');
                eyeIcon_oldpassword.classList.add('fa-eye-slash'); // Change to eye-slash icon
            } else {
                oldpasswordField.type = 'password';
                eyeIcon_oldpassword.classList.remove('fa-eye-slash');
                eyeIcon_oldpassword.classList.add('fa-eye'); // Change back to eye icon
            }
        });
    }

    //Get the button:
    mybutton = document.getElementById("myBtn");

    // Add an event listener to trigger the scroll to top function when the button is clicked
    mybutton.addEventListener('click', topFunction);
    // When the user scrolls down 60px from the top of the document, show the button
    window.onscroll = function() {
        scrollFunction()
    };

    function scrollFunction() {
      if (window.scrollY > 60) {
        mybutton.style.display = "block";
      } else {
        mybutton.style.display = "none";
      }
    }

    // When the user clicks on the button, scroll to the top of the document
    function topFunction() {
        window.scrollTo ({
            top:0,
            left:0,
            behavior: "smooth"
        });

    }
});
