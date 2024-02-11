document.addEventListener('DOMContentLoaded', function () {
  const listMoviesElement = document.getElementById('list_movies');

  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      const movies = data.results;

      movies.forEach(movie => {
        const title = movie.title;
        const listItem = document.createElement('li');
        listItem.textContent = title;
        listMoviesElement.appendChild(listItem);
      });
    })
    .catch(error => {
      console.error('Error fetching data:', error.message);
    });
});
