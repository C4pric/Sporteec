document.addEventListener('DOMContentLoaded', function() {
    const signUpButton = document.getElementById('signUp');
    const signInButton = document.getElementById('signIn');
    const container = document.getElementById('container');

    // Commentez ou retirez cette ligne pour ne pas activer le panneau "S'inscrire" par défaut
    // container.classList.add('right-panel-active');

    signUpButton.addEventListener('click', () => {
        container.classList.add('right-panel-active');
    });

    signInButton.addEventListener('click', () => {
        container.classList.remove('right-panel-active');
    });

    const passwordInputSignup = document.getElementById('passwordInputSignup');
    const togglePasswordButtonSignup = document.getElementById('togglePasswordSignup');
    const eyeIconSignup = document.getElementById('eyeIconSignup');

    let isPasswordVisibleSignup = false;

    togglePasswordButtonSignup.addEventListener('click', function() {
        if (isPasswordVisibleSignup) {
            passwordInputSignup.type = 'password';
            eyeIconSignup.src = 'static/css/img/eye_nv.png'; // Chemin correct de l'image
        } else {
            passwordInputSignup.type = 'text';
            eyeIconSignup.src = 'static/css/img/eye_v.png'; // Chemin correct de l'image
        }
        isPasswordVisibleSignup = !isPasswordVisibleSignup;
    });

    const passwordInputLogin = document.getElementById('passwordInputLogin');
    const togglePasswordButtonLogin = document.getElementById('togglePasswordLogin');
    const eyeIconLogin = document.getElementById('eyeIconLogin');

    let isPasswordVisibleLogin = false;

    togglePasswordButtonLogin.addEventListener('click', function() {
        if (isPasswordVisibleLogin) {
            passwordInputLogin.type = 'password';
            eyeIconLogin.src = 'static/css/img/eye_nv.png'; // Chemin correct de l'image
        } else {
            passwordInputLogin.type = 'text';
            eyeIconLogin.src = 'static/css/img/eye_v.png'; // Chemin correct de l'image
        }
        isPasswordVisibleLogin = !isPasswordVisibleLogin;
    });
});
