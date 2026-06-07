(function () {

  document.addEventListener("submit", function (e) {
    const form = e.target.closest("form[data-confirm]");
    if (!form) return;
    if (!window.confirm(form.dataset.confirm || "Are you sure?")) e.preventDefault();
  });

  const search = document.getElementById("webinar-search");
  const table  = document.getElementById("webinar-table");
  if (search && table) {
    search.addEventListener("input", function () {
      const q = this.value.trim().toLowerCase();
      table.querySelectorAll("tbody tr").forEach(row => {
        const text = (row.dataset.search || row.textContent).toLowerCase();
        row.classList.toggle("adm-hidden", q.length > 0 && !text.includes(q));
      });
    });
  }

})();
