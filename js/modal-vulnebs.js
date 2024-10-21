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
