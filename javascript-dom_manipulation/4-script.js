/*eslint-disable*/
document.addEventListener('DOMContentLoaded', () => {
    const addItemButton = document.getElementById('add_item');
    const myList = document.querySelector('ul.my_list');

    addItemButton.addEventListener('click', () => {
        const newItem = document.createElement('li');
        newItem.textContent = 'Item';
        myList.appendChild(newItem);
    });
});