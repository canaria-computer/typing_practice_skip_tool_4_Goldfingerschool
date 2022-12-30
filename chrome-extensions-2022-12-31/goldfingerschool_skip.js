document.body.addEventListener("keyup", event => {
    if((event.key==" " || event.key=="　") && event.ctrlKey) {
        ($1 = document.getElementById("textdata")).querySelectorAll("rp,rt").forEach(eath => eath.remove());
        document.getElementById("inputdata").value = $1.textContent.replace(new RegExp("□", "g"), "　").replace(new RegExp("↵", "g"), "\n");
        document.getElementById("checkbutton").click();
    }
},false);

