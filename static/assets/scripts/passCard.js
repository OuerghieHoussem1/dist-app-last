const socket = io.connect();

socket.on('connect', () => {
    console.log('WebSocket connected');
    // You can perform any actions when the WebSocket is connected
});

socket.on('disconnect', () => {
    console.log('WebSocket disconnected');
    // You can perform any actions when the WebSocket is disconnected
});

const words = document.getElementById("words") 


const onSuccess = (cardData) => {
    words.innerText = `Welcome ${cardData.cardName}`
    localStorage.setItem("card",JSON.stringify(cardData))

    setTimeout(() => {
        window.location.href = "http://127.0.0.1:5500/templates/chooseTaste.html"
    }, 3000);
}

/* setTimeout(onSuccess, 3000, {cardName:"Houssem"}); */