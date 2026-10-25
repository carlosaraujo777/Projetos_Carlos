const output = document.getElementById('output');
const input = document.getElementById('command-input');
const terminal = document.querySelector('.terminal');

function scrollToBottom() {
    terminal.scrollTop = terminal.scrollHeight;
}

function printText(text, className = "") {
    const p = document.createElement('p');
    p.textContent = text;
    if (className) p.className = className;
    output.appendChild(p);
    scrollToBottom();
}

input.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        const cmd = input.value.trim().toLowerCase();
        
        printText(`root@matrix:~$ ${input.value}`);
        input.value = "";

        switch(cmd) {
            case "":
                break;
            case "help":
                printText("Available commands:");
                printText("- help: Show this message");
                printText("- whoami: Print current user identity");
                printText("- matrix: Take the red pill");
                printText("- date: Show system date");
                printText("- sudo: Try your luck");
                printText("- hack: Start a fake exploit");
                printText("- clear: Clear the terminal screen");
                break;
            case "whoami":
                printText("You are Neo. The One. 👽");
                break;
            case "matrix":
                printText("Wake up, Neo... Follow the white rabbit. 🐇");
                break;
            case "date":
                printText(new Date().toString());
                break;
            case "sudo":
                printText("Nice try. But you don't have root privileges. 🚫");
                break;
            case "hack":
                printText("Initializing exploit...");
                setTimeout(() => printText("Bypassing firewall..."), 500);
                setTimeout(() => printText("Access granted. You are in. 🔓"), 1500);
                break;
                         case "clear":
                // Limpa tudo que tá dentro do terminal
                output.innerHTML = "";
                
                // Recria o cabeçalho bonito
                const header1 = document.createElement('p');
                header1.textContent = "MATRIX OS v4.0.1 (c) 2026";
                output.appendChild(header1);
                
                const header2 = document.createElement('p');
                header2.textContent = "Type 'help' to see available commands.";
                output.appendChild(header2);
                
                // Dá um espaço
                output.appendChild(document.createElement('br'));
                
                // Foca o input de novo pra você não precisar clicar
                input.focus();
                break;  
            default:
                printText(`Command not found: '${cmd}'. Type 'help'.`);
        }
        
        scrollToBottom();
    }
});

// ==========================================
// MATRIX RAIN (Fundo)
// ==========================================
const canvas = document.getElementById('matrix-canvas');
const ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Caracteres que vão cair na tela (Katakana + números + letras)
const letters = "アァカサタナハマヤャラワガザダバパイィキシチニヒミリヰギジヂビピウゥクスツヌフムユュルグズブヅプエェケセテネヘメレゲゼデベペオォコソトノホモヨョロゴゾドボポヴッン0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const fontSize = 16;
const columns = canvas.width / fontSize;

const drops = [];
for (let x = 0; x < columns; x++) {
    drops[x] = 1; 
}

function drawMatrix() {
    // Fundo preto semi-transparente pra criar o rastro
    ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = "#0F0";
    ctx.font = fontSize + "px monospace";

    for (let i = 0; i < drops.length; i++) {
        const text = letters.charAt(Math.floor(Math.random() * letters.length));
        ctx.fillText(text, i * fontSize, drops[i] * fontSize);

        // Reseta a gota pra voltar pro topo aleatoriamente
        if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
            drops[i] = 0;
        }
        drops[i]++;
    }
}

// Roda o desenho a cada 33 milissegundos (30 FPS)
setInterval(drawMatrix, 33);

// Ajusta o canvas se a janela for redimensionada
window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    // Recalcula as colunas pra chuva não bugar
    columns = canvas.width / fontSize;
    drops = [];
    for (let x = 0; x < columns; x++) {
        drops[x] = 1; 
    }
});