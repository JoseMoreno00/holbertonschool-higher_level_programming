document.querySelector('#add_item').addEventListener('click', () => {
  const lista = document.querySelector('.my_list');
  lista.innerHTML += '<li>Item</li>';
});
