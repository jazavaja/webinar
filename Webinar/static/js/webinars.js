// Test js And run If not work do not merge that!

const CATEGORIES = [
  "All",
  "technology",
  "web-development",
  "ai-machine-learning",
  "cybersecurity",
  "data-science",
  "cloud-computing",
  "business",
  "entrepreneurship",
  "marketing",
  "finance",
  "python",
  "java",
  "c++",
  "science",
  "math",
  "programming-language",
  "leadership",
  "education",
  "career-growth",
  "design",
  "ui-ux",
  "content-creation",
  "health-wellness",
  "productivity",
  "gaming",
  "lifestyle",
  "networking",
  "workshops",
  "startups",
  "freelancing",
  "software-development"
];

const PRICE_FILTERS = [
  { id: "any", label: "Any" },
  { id: "free", label: "Free" },
  { id: "under20", label: "Under €20" },
  { id: "under50", label: "Under €50" },
];

const state = {
  q: "",
  cats: new Set(["All"]),
  price: "any",
  page: 1
};

const $ = (s) => document.querySelector(s);
const grid = $("#grid");
const meta = $("#meta");
const empty = $("#empty");

let WEBINARS = [];

async function loadPage(page) {
  const params = new URLSearchParams();
  params.set("page", page);
  params.set("q", state.q);
  params.set("price", state.price);
  state.cats.forEach(c => params.append("cats", c));

  const response = await fetch(`/get_webinar_by_js/?${params}`, {
    headers: { "X-Requested-With": "XMLHttpRequest" }
  });

  const data = await response.json();
  WEBINARS = data.webinars;
  state.page = data.current_page;

  $("#current-page").value = data.current_page;
  $("#next-btn").disabled = !data.has_next;
  $("#prev-btn").disabled = !data.has_previous;

  render();
}

function renderPills() {
  $("#cat-pills").innerHTML = CATEGORIES.map(c =>
    `<button class="pill${state.cats.has(c) ? " active" : ""}" data-cat="${c}">${c}</button>`
  ).join("");

  $("#price-pills").innerHTML = PRICE_FILTERS.map(p =>
    `<button class="pill${p.id === state.price ? " active" : ""}" data-price="${p.id}">${p.label}</button>`
  ).join("");

  document.querySelectorAll("[data-cat]").forEach(btn => {
    btn.onclick = () => {
      const cat = btn.dataset.cat;
      if (cat === "All") {
        state.cats = new Set(["All"]);
      } else {
        state.cats.delete("All");
        state.cats.has(cat) ? state.cats.delete(cat) : state.cats.add(cat);
        if (state.cats.size === 0) state.cats.add("All");
      }
      // back first page
      loadPage(1);
    };
  });

  document.querySelectorAll("[data-price]").forEach(btn => {
    btn.onclick = () => {
      state.price = btn.dataset.price;
      loadPage(1);
    };
  });
}

function cardHTML(w) {
  const cats = (w.categories || []).map(c => `<span class="tag">${c}</span>`).join("");
  const price = Number(w.price) === 0
    ? `<span class="price free">Free</span>`
    : `<span class="price">€${w.price}</span>`;
  const image = w.image ? `<img src="${w.image}" class="w-image" alt="${w.title}">` : "";

  return `
    <article class="w-card">
      <a href="/webinar/detail/${w.id}/">
        ${image}
        <div class="w-top">
          <div class="tags">${cats}</div>
          ${price}
        </div>
        <h3>${w.title}</h3>
        <p class="w-blurb">${w.blurb}</p>
        <div class="w-meta">
          <div>
            <div class="w-when">${w.when}</div>
            <div class="seats">${w.seatsLeft} seats left</div>
          </div>
        </div>
      </a>
    </article>
  `;
}

function render() {
  renderPills();
  grid.innerHTML = WEBINARS.map(cardHTML).join("");
  meta.textContent = `SHOWING ${WEBINARS.length} WEBINARS`;
  empty.hidden = WEBINARS.length !== 0;
  grid.hidden = WEBINARS.length === 0;
}

let searchTimer;
// Wait For search 400mili secound
$("#q").addEventListener("input", e => {
  state.q = e.target.value;
  clearTimeout(searchTimer);
  searchTimer = setTimeout(() => loadPage(1), 400);
});

$("#next-btn").onclick = () => loadPage(state.page + 1);
$("#prev-btn").onclick = () => { if (state.page > 1) loadPage(state.page - 1); };

loadPage(1);




