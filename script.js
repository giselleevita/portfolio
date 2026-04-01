const root = document.documentElement;
const toggle = document.getElementById("themeToggle");
const label = toggle?.querySelector(".toggle-label");
const storageKey = "giselleevita-theme";

function setTheme(theme) {
  root.setAttribute("data-theme", theme);
  if (label) {
    label.textContent = theme === "dark" ? "Dark" : "Light";
  }
  localStorage.setItem(storageKey, theme);
}

const savedTheme = localStorage.getItem(storageKey);
if (savedTheme === "dark" || savedTheme === "light") {
  setTheme(savedTheme);
}

toggle?.addEventListener("click", () => {
  const current = root.getAttribute("data-theme");
  setTheme(current === "dark" ? "light" : "dark");
});
