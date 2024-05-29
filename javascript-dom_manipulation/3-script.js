/*eslint-disable*/
document.addEventListener('DOMContentLoaded', () => {
    const toggleHeaderButton = document.getElementById('toggle_header');
    const header = document.querySelector('header');

    toggleHeaderButton.addEventListener('click', () => {
        if (header.classList.contains('red')) {
            header.classList.remove('red');
            header.classList.add('green');
        } else {
            header.classList.remove('green');
            header.classList.add('red');
        }
    });
});