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
});
