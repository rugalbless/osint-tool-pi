document.addEventListener('DOMContentLoaded', () => {
    const gridContainer = document.querySelector('.grid-container');
    const cols = window.innerWidth < 640 ? 20 : 10; // 20x20 no mobile, 10x10 telas grandes

    // configura a grade com base no número de colunas/linhas
    gridContainer.style.gridTemplateColumns = `repeat(${cols}, 1fr)`;
    gridContainer.style.gridTemplateRows = `repeat(${cols}, 1fr)`;

    const totalCells = cols * cols;

    for (let i = 0; i < totalCells; i++) {
        const cell = document.createElement('div');
        cell.className = 'border border-white/20 bg-white/8';
        gridContainer.appendChild(cell);
    }
});

document.addEventListener('DOMContentLoaded', () => {
    const shapes = document.querySelectorAll('.blur-shape');

    const moveShapes = () => {
        shapes.forEach(shape => {
            // Calcular posições aleatórias dentro da tela
            const windowWidth = window.innerWidth;
            const windowHeight = window.innerHeight;

            const randomX = Math.random() * (windowWidth - shape.offsetWidth);
            const randomY = Math.random() * (windowHeight - shape.offsetHeight);

            // aplicar a nova posição com um pequeno movimento aleatório
            shape.style.transform = `translate(${randomX}px, ${randomY}px)`;
        });
    };

    // Mover os shapes a cada 3 segundos
    setInterval(moveShapes, 3000);
});

