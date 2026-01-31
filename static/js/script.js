document.addEventListener("DOMContentLoaded", () => {

    // ---------- REGISTER ----------
    const registerForm = document.getElementById("registerForm");
    const registerMessage = document.getElementById("message");

    if (registerForm) {
        registerForm.addEventListener("submit", async (e) => {
            e.preventDefault();

            const email = document.getElementById("email").value;
            const password = document.getElementById("password").value;

            try {
                const response = await fetch("/register", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({ email, password })
                });

                const data = await response.json();
                registerMessage.innerText = data.message;

                if (response.ok) {
                    registerForm.reset();
                }
            } catch (error) {
                registerMessage.innerText = "Something went wrong. Try again.";
            }
        });
    }

    // ---------- LOGIN ----------
    const loginForm = document.getElementById("loginForm");
    const loginMessage = document.getElementById("loginMessage");

    if (loginForm) {
        loginForm.addEventListener("submit", async (e) => {
            e.preventDefault();

            const email = document.getElementById("loginEmail").value;
            const password = document.getElementById("loginPassword").value;

            try {
                const response = await fetch("/login", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({ email, password })
                });

                const data = await response.json();
                loginMessage.innerText = data.message;

                if (response.ok) {
                    window.location.href = "/portfolio";
                }
            } catch (error) {
                loginMessage.innerText = "Something went wrong. Try again.";
            }
        });
    }

});
