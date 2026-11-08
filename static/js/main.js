document.querySelectorAll('.demo-form').forEach(form => {
  form.addEventListener('submit', event => {
    event.preventDefault();
    form.querySelector('.demo-result').textContent = 'Dimostrazione completata: nessun dato è stato inviato o salvato.';
    form.reset();
  });
});
