const current_time = document.querySelector(".time")
const current_date = document.querySelector(".date")
const container = document.querySelector(".moves")
const total_amount = document.querySelector(".amount")
const worker_name = document.querySelector(".w_name")
const kopa_number = document.querySelector(".kopa_num")
const btn = document.querySelector("button")

let names;
let prices;
let totals;

btn.addEventListener("click", function(){
    print()
})

eel.expose(recieve2)
function recieve2(data1, data2, data3){
    console.log("runn")
    recieve(data1, data2, data3)
}

function start() {
    eel.send_data()(function(data1, data2, data3){
        names = data1
        prices = data2
        totals = data3
        
        //getting the current date with js
        let dateObj = new Date();
            let month = String(dateObj.getMonth() + 1).padStart(2, '0');
            let day = String(dateObj.getDate()).padStart(2, '0');
            let year = dateObj.getFullYear();
            let output = day + '/' + month + '/' + year;
            current_date.textContent = output;
        
        //getting the current time with python
        eel.get_time()(function(time){
            current_time.textContent = time
        })

        eel.send_info()(function(name, kopa, total){
            total_amount.textContent = total
            worker_name.textContent = name
            kopa_number.textContent = kopa
        })
        
        recieve2(names, prices, totals)
    })
}


function recieve(nameo, prices, totals) {
    for (let i=0; i < nameo.length; i++) {
        let new_move = `
            <div class="items">
                <div class="item_name">${nameo[i]}</div>
                <div class="item_price">${prices[i]}</div>
                <div class="item_total_price">${totals[i]}</div>
            </div>
        `
        container.insertAdjacentHTML("afterbegin", new_move)
    }

}


start()