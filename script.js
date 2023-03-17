  document.getElementById('filterInput').addEventListener('keyup', function() {
    const filter = this.value.toUpperCase();
    const table = document.querySelector('.container > table:last-child tbody');
    const rows = table.querySelectorAll('tr');

    for (let i = 0; i < rows.length; i++) {
      const cells = rows[i].querySelectorAll('td');
      let shouldShowRow = false;

      for (let j = 0; j < cells.length; j++) {
        if (cells[j].textContent.toUpperCase().indexOf(filter) > -1) {
          shouldShowRow = true;
          break;
        }
      }

      rows[i].style.display = shouldShowRow ? '' : 'none';
    }
  });