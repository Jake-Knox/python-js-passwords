
const generateButton = document.getElementById("generateButton");
const passwordResult = document.getElementById("passwordResult");

generateButton.addEventListener("click", () => {
    const passwordLength = 10;
    fetch(`/generate-password/${passwordLength}`)
        .then(response => response.json())
        .then(data => {
            const generatedPassword = data.password;
            passwordResult.textContent = generatedPassword;
        })
        .catch(error => {
            console.error('Error:', error);
        });
});
