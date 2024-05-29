/*eslint-disable*/
document.addEventListener('DOMContentLoaded', () => {
    const listMoviesElement = document.getElementById('list_movies');

    fetch('https://swapi-api.hbtn.io/api/films/?format=json')
        .then(response => response.json())
        .then(data => {
            const films = data.results;
            films.forEach(film => {
                const listItem = document.createElement('li');
                listItem.textContent = film.title;
                listMoviesElement.appendChild(listItem);
            });
        })
        .catch(error => console.error('Error fetching films:', error));
});