document.addEventListener("DOMContentLoaded", function() {
    const dateElement = document.getElementById("conference-date");
    const currentDate = new Date();
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    dateElement.textContent = currentDate.toLocaleDateString('es-ES', options);
});
