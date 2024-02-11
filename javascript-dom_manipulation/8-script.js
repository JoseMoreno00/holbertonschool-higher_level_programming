document.addEventListener('DOMContentLoaded', function () {
  const helloElement = document.getElementById('hello');

  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      const helloTranslation = data.hello;
      helloElement.textContent = helloTranslation;
    })
    .catch(error => {
      console.error('Error fetching data:', error.message);
    });
});
