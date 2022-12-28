$(document).ready(function(){
    $("#nav_button").click(function(){
        $("#nav_link").toggle(500);
    })
})


function Incident(){
    var angle = document.getElementById("angle-up-down")
    if(angle.className == 'fa-sharp fa-solid fa-angle-down float-end p-1'){
        angle.className = 'fa-sharp fa-solid fa-angle-up float-end p-1'
    }
    else{
        document.getElementById('angle-up-down').className = 'fa-sharp fa-solid fa-angle-down float-end p-1'
    }
}