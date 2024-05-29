/*eslint-disable*/
document.addEventListener('DOMContentLoaded', () => {
    const updateHeaderButton = document.getElementById('update_header');
    const header = document.querySelector('header');

    updateHeaderButton.addEventListener('click', () => {
        header.textContent = 'New Header!!!';
    });
});