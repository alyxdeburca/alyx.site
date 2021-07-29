var i = 0;
var txt = "Hi, I'm Alyx";
var speed = 100;

function typeWriter() {
if (i < txt.length) {
    document.getElementById("scrolling").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
    }
setTimeout(loadIntro, 1300)
}

function loadIntro() {
    document.getElementById('intro').style.display='block';
    loadIntro1()
}
function loadIntro1() {
    document.getElementById('intro1').style.display='block';
    loadIntro2()
}
function loadIntro2() {
    document.getElementById('intro2').style.display='block';
    loadContact()
}

function loadContact() {
    document.getElementById('contact').style.display='block';
}
