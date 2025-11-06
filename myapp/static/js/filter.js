const buttons = document.querySelectorAll(".filter-btn");
const cards = document.querySelectorAll(".product-card");

buttons.forEach(btn => {
  btn.addEventListener("click", () => {
    buttons.forEach(b => b.classList.remove("active"));
    btn.classList.add("active");

    const category = btn.dataset.category;
    cards.forEach(card => {
      card.style.display = (category === "all" || card.dataset.category === category) 
        ? "block" 
        : "none";
    });
  });
});
