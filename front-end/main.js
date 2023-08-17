let db = fetch("http://localhost:8080/card/").then(el => el.json())
db.then(el => {
    for (const key in el) {
        document.querySelector(".cards").innerHTML += `
            <div class="card">
                <span class="name">${el[key].name}</span>
                <span class="text">${el[key].text}</span>
            </div>
        `
    }
})
