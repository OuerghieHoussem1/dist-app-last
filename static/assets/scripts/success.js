const card = JSON.parse(localStorage.getItem("card"))
const taste = JSON.parse(localStorage.getItem("taste"))
const intensity = JSON.parse(localStorage.getItem("intensity"))
setTimeout(() => {
    window.location.href = "http://localhost:5000/"
}, 3000);