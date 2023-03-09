var a = document.getElementById('why');
a.onkeydown = function(e) {
    if (e.key === "Enter") {
    document.getElementById('btn').click();
    }

};