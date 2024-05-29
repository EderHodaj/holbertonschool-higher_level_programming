/*eslint-disable*/
document.addEventListener('DOMContentLoaded', () => {
    const redHeaderButton = document.getElementById('red_header');
    const header = document.querySelector('header');

    redHeaderButton.addEventListener('click', () => {
        header.style.color = '#FF0000';
    });
});