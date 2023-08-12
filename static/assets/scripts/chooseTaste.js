const container = document.getElementById("container")

const onDrinksLoad = (drinks) => {

    drinks.forEach(drink => {
        const drinkElement = document.createElement("img")
        switch (drink.className){
            case "Cassis":
                drinkElement.src = "./assets/images/1.png"
                break;
            case "CitronVert":
                drinkElement.src = "./assets/images/12.png"
                break;
            case "Pasteque":
                drinkElement.src = "./assets/images/123.png"
                break;
            case "FiguedeBarbarie":
                drinkElement.src = "./assets/images/1234.png"
                break;
            case "PecheetFruitdelaPassion":
                drinkElement.src = "./assets/images/12345.png"
                break;
            case "Eau":
                drinkElement.src = "./assets/images/1234567.png"
                break;
        }

        drinkElement.classList.add("drink")
        drinkElement.dataset.saveur = drink.saveur

        drinkElement.onclick = (e)=>{
            localStorage.setItem("saveur",JSON.stringify(e.srcElement.dataset.saveur))
            window.location.href = "http://127.0.0.1:5500/templates/chooseIntensity.html"
        }

        container.appendChild(drinkElement)
    });
}

setTimeout(onDrinksLoad, 100,[
    {className:"Cassis",saveur:1},
    {className:"CitronVert",saveur:2},
    {className:"Pasteque",saveur:3},
    {className:"FiguedeBarbarie",saveur:4},
    {className:"PecheetFruitdelaPassion",saveur:5},
    {className:"Eau",saveur:6}
]);