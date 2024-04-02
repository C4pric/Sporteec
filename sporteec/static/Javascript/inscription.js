document.addEventListener('DOMContentLoaded', function() {
    const signUpButton = document.getElementById('signUp');
    const signInButton = document.getElementById('signIn');
    const container = document.getElementById('container');

    // Toujours activer le panneau "S'inscrire" par défaut
    container.classList.add('right-panel-active');

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
            eyeIconSignup.src = 'Sporteec/css/img/eye_v.png'; // Changer l'image de l'œil ouvert
        } else {
            passwordInputSignup.type = 'text';
            eyeIconSignup.src = 'Sporteec/css/img/eye_nv.png'; // Changer l'image de l'œil barré
        }
        isPasswordVisibleSignup = !isPasswordVisibleSignup; // Inverser le statut de visibilité du mot de passe
    });

    const passwordInputLogin = document.getElementById('passwordInputLogin');
    const togglePasswordButtonLogin = document.getElementById('togglePasswordLogin');
    const eyeIconLogin = document.getElementById('eyeIconLogin');

    let isPasswordVisibleLogin = false;

    togglePasswordButtonLogin.addEventListener('click', function() {
        if (isPasswordVisibleLogin) {
            passwordInputLogin.type = 'password';
            eyeIconLogin.src = 'Sporteec/css/img/eye_v.png'; // Changer l'image de l'œil ouvert
        } else {
            passwordInputLogin.type = 'text';
            eyeIconLogin.src = 'Sporteec/css/img/eye_nv.png'; // Changer l'image de l'œil barré
        }
        isPasswordVisibleLogin = !isPasswordVisibleLogin; // Inverser le statut de visibilité du mot de passe
    });
});

