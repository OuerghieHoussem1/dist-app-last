const image = document.getElementById("mainImage")


localStorage.removeItem("card")
localStorage.removeItem("taste")
localStorage.removeItem("intensity")


image.onclick = () => {
    window.location.href = "http://localhost:5000/chooseTaste"
}