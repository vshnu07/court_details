document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("caseForm");
  form.addEventListener("submit", function (e) {
    const year = document.getElementById("case_year").value;
    const number = document.getElementById("case_number").value;
    const captcha = form.captcha.value.trim();

    if (isNaN(number) || number === "") {
      alert("Please enter a valid case number.");
      e.preventDefault();
    }

    if (!/^\d{4}$/.test(year)) {
      alert("Please enter a 4-digit year.");
      e.preventDefault();
    }

    if (captcha.length === 0) {
      alert("Please enter the CAPTCHA.");
      e.preventDefault();
    }
  });
});
// JS for interactivity
