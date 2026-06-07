(function () {

  // ---- confirm on destructive forms ----
  document.addEventListener("submit", function (e) {
    const form = e.target.closest("form[data-confirm]");
    if (!form) return;
    if (!window.confirm(form.dataset.confirm || "Are you sure?")) e.preventDefault();
  });

  // ---- inline edit toggle ----
  document.addEventListener("click", function (e) {

    const trigger = e.target.closest(".adm-edit-trigger");
    if (trigger) {
      const block = document.getElementById(trigger.dataset.target);
      if (!block) return;
      const isOpen = block.style.display !== "none";
      block.style.display = isOpen ? "none" : "block";
      trigger.textContent = isOpen ? "Edit" : "Cancel";
      return;
    }

    const cancel = e.target.closest(".adm-edit-cancel");
    if (cancel) {
      const block = document.getElementById(cancel.dataset.target);
      if (block) block.style.display = "none";
      const trigger = document.querySelector(`.adm-edit-trigger[data-target="${cancel.dataset.target}"]`);
      if (trigger) trigger.textContent = "Edit";
      return;
    }

    // ---- password toggle ----
    const pwdToggle = e.target.closest(".adm-pwd-toggle");
    if (pwdToggle) {
      const field = document.getElementById(pwdToggle.dataset.target);
      const input = field.querySelector("input");
      const isOpen = field.style.display !== "none";
      field.style.display = isOpen ? "none" : "block";
      input.disabled = isOpen;
      pwdToggle.textContent = input.disabled ? "Change password" : "Password unlocked";
    }

  });

  // ---- live search ----
  const search = document.getElementById("user-search");
  const table  = document.getElementById("user-table");
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
