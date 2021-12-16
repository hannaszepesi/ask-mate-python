// you receive an array of objects which you must sort in the by the key "sortField" in the "sortDirection"
function getSortedItems(items, sortField, sortDirection) {
    console.log(items)
    console.log(sortField)
    console.log(sortDirection)

    // === SAMPLE CODE ===
    // if you have not changed the original html uncomment the code below to have an idea of the
    // effect this function has on the table
    //
    if (sortDirection === "asc") {
        for (let i=0; i<items.length; i++) {
            const firstItem = items.shift()
            if (firstItem) {
                items.push(firstItem)
            }
        }
    }
    else {
        const lastItem = items.pop()
        if (lastItem) {
            items.push(lastItem)
        }
    }

    return items
}

// you receive an array of objects which you must filter by all it's keys to have a value matching "filterValue"
function getFilteredItems(items, filterValue) {
    console.log(items)
    console.log(filterValue)
    let result = []
    // === SAMPLE CODE ===
    // if you have not changed the original html uncomment the code below to have an idea of the
    // effect this function has on the table
    //
    for (let i=0; i<items.length; i++) {
        if (filterValue[0] === "!") {
            if (filterValue.substring(1, 13) === "Description:") {
                if (!(items[i]['Description'].includes(filterValue.substring(13, filterValue.length)))) {
                    result.push(items[i])
                }
            }
            else if (!(items[i]['Description'].includes(filterValue.substring(1, filterValue.length)) || items[i]['Title'].includes(filterValue.substring(1, filterValue.length)))) {
                result.push(items[i])
            }
        } else if (filterValue.substring(0, 12) === "Description:" && items[i]['Description'].includes(filterValue.substring(12, filterValue.length))) {
            result.push(items[i])
        } else if (items[i]['Title'].includes(filterValue) || items[i]['Description'].includes(filterValue)) {
            result.push(items[i])
        }
    }

    return result
}

function darkMode() {
    console.log("toggle theme")
    var element = document.body;
    var content = document.getElementById("theme-button");
    element.className = "dark-mode";
    content.innerText = "Dark Mode is ON";
}

function lightMode() {
    var element = document.body;
    var content = document.getElementById("DarkModetext");
    element.className = "light-mode";
    content.innerText = "Dark Mode is OFF";
}

function increaseFont() {
    console.log("increaseFont")
}

function decreaseFont() {
    console.log("decreaseFont")
}