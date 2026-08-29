function realizarLogin() {
    // Captura dos valores
    const usuario = document.getElementById("usuario").value.trim();
    const senha = document.getElementById("senha").value.trim();

    // Validação de campos vazios
    if (usuario === "" || senha === "") {
        document.getElementById("mensagem").innerText = "Preencha todos os campos.";
        return;
    }

    // Verificação de login
    if (usuario === "admin" && senha === "123") {
        alert("Login realizado com sucesso!");
        window.location.href = "page.html";
    } else {
        document.getElementById("mensagem").innerText = "Usuário ou senha incorretos.";
    }
}