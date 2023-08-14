const buttons = document.querySelectorAll('[data-chosen]');

const deguster = document.getElementById("deguster")
const back = document.getElementById("back")


deguster.onclick = () => {
    const value = document.querySelectorAll('[data-chosen~="true"]')[0]
    const intensity = value.dataset.intensity

    localStorage.setItem("intensity", JSON.stringify(intensity))

    window.location.href = "http://localhost:5000/success"
}
back.onclick = () => {
    window.location.href = "http://localhost:5000/chooseTaste"
}

const chooseThis = e => {
    const button = e.srcElement
    buttons.forEach(btn => {
        btn.dataset.chosen = false
    })
    button.dataset.chosen = true
}

buttons.forEach(btn => {
    btn.onclick = chooseThis
})

