// Dark/Light toggle
const toggle = document.getElementById("themeToggle");
const savedTheme = localStorage.getItem("theme");
const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;

if (savedTheme) {
  document.documentElement.setAttribute("data-theme", savedTheme);
  toggle.textContent = savedTheme === "dark" ? "☀️" : "🌙";
} else if (prefersDark) {
  document.documentElement.setAttribute("data-theme", "dark");
}

toggle.addEventListener("click", () => {
  const current = document.documentElement.getAttribute("data-theme");
  const next = current === "dark" ? "light" : "dark";
  document.documentElement.setAttribute("data-theme", next);
  localStorage.setItem("theme", next);
  toggle.textContent = next === "dark" ? "☀️" : "🌙";
});

// Live API predict function
async function predict() {
  const text = document.getElementById("emailText").value;
  const resultDiv = document.getElementById("result");

  if (!text.trim()) {
    resultDiv.innerHTML = "⚠️ Please enter an email.";
    return;
  }

  resultDiv.innerHTML = "⏳ Analyzing...";

  try {
    const response = await fetch("https://spam-email-detector-ja5l.onrender.com/predict", {  // <-- your live API URL
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text })
    });

    const data = await response.json();

    resultDiv.innerHTML =
      data.prediction === "spam"
        ? "🚨 This looks like SPAM (${data.confidence}% confidence)"
        : "✅ This looks SAFE (${100 - data.confidence}% confidence)";

  } catch (error) {
    console.error(error);
    resultDiv.innerHTML = "❌ API error. Try again later.";
  }
}
