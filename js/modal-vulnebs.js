class ModalVulnebs {
    constructor(openButtonId, modalId, closeButtonId) {
        this.openButton = document.getElementById(openButtonId);
        this.modal = document.getElementById(modalId);
        this.closeButton = document.getElementById(closeButtonId);

        this.init();
    }

    init() {
        this.openButton.addEventListener('click', (event) => {
            event.preventDefault();
            this.open();
        });

        this.closeButton.addEventListener('click', () => {
            this.close();
        });

        this.modal.addEventListener('click', (event) => {
            if (event.target === this.modal) {
                this.close();
            }
        });
    }

    open() {
        this.modal.classList.remove('hidden');
    }

    close() {
        this.modal.classList.add('hidden');
    }
}

const modalVul = new ModalVulnebs('vulneb', 'vulneb-in', 'close-vulneb');
function DocResearch() {
    const query = encodeURIComponent('filetype:pdf|txt|docx intitle:"Confidencial"');
    const url = `https://www.google.com/search?q=${query}`;
    window.open(url, '_blank');
}
function PDPResearch() {
    const query = encodeURIComponent('filetype:xls intext:"nome" "CPF"');
    const url = `https://www.google.com/search?q=${query}`;
    window.open(url, '_blank');
}
function ContactResearch() {
    const query = encodeURIComponent('filetype:csv OR filetype:xls "email" "telefone"');
    const url = `https://www.google.com/search?q=${query}`;
    window.open(url, '_blank');
}
