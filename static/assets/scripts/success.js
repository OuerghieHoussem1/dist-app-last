const card = JSON.parse(localStorage.getItem("card"))
const taste = JSON.parse(localStorage.getItem("taste"))
const intensity = JSON.parse(localStorage.getItem("intensity"))


fetch(`http://localhost:5000/taste/${taste}/${intensity}`)
    .then(response => {
        if (!response.ok) {
            throw new Error("Network response was not ok");
        }
        return response.json();
    })
    .then(data => {
        // Handle the data
        console.log(data);
        window.location.href = "http://localhost:5000/"
    })