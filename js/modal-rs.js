class ModalRs {
    constructor(openButtonId, modalId, closeButtonId) {
        this.openButton = document.getElementById(openButtonId);
        this.modal = document.getElementById(modalId);
        this.closeButton = document.getElementById(closeButtonId);
        this.optionButtons = this.modal.querySelectorAll('.option-button');
        this.selectedOption = null;
        this.searchInput = document.getElementById('search-input');

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

        this.optionButtons.forEach(button => {
            button.addEventListener('click', () => {
                this.selectOption(button);
            });
        });
    }

    open() {
        this.modal.classList.remove('hidden');
    }

    close() {
        this.modal.classList.add('hidden');
    }

    selectOption(button) {
        if (this.selectedOption) {
            this.selectedOption.classList.remove('bg-blue-500', 'text-white');
            this.selectedOption.classList.add('bg-gray-200', 'text-black');
        }
        button.classList.remove('bg-gray-200', 'text-black');
        button.classList.add('bg-blue-500', 'text-white');
        this.selectedOption = button;
    }
}

const modalRs = new ModalRs('modal-rs', 'modal-rs-in', 'close-modal');

function search() {
    const selectedOption = modalRs.selectedOption;
    const searchInput = modalRs.searchInput.value;

    if (selectedOption && searchInput) {
        const query = encodeURIComponent(`site:${selectedOption.dataset.option} comments from "${searchInput}"`);
        const url = `https://www.google.com/search?q=${query}`;
        window.open(url, '_blank');
    } else {
        alert("Por favor, selecione uma opção e digite uma pesquisa.");
    }
}