document.body.addEventListener("keyup", event => {
    if((event.key==" " || event.key=="　") && event.ctrlKey) {
        ($1=document.getElementById("textdata")).querySelectorAll("rp,rt").forEach(eath=>eath.remove())
        document.getElementById("inputdata").value=$1.textContent
        document.getElementById("checkbutton").click()
    }
},false);
