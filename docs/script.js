function gerarSenha() {
    // Definindo os caracteres
    const letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    const numeros = "0123456789";
    const simbolos = "!@#$%^&*()_+~`|}{[]:;?><,./-=";
    
    const todos = letras + numeros + simbolos;
    const tamanho = 16; // Tamanho da senha
    let senha = "";

    // Loop para gerar os caracteres aleatórios
    for (let i = 0; i < tamanho; i++) {
        const indiceAleatorio = Math.floor(Math.random() * todos.length);
        senha += todos[indiceAleatorio];
    }

    // Coloca a senha na tela
    document.getElementById("resultado").innerText = senha;
}2
