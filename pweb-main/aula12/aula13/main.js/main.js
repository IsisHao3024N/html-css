/*
menu-principal menu-princnipal--fechado*/

let botao = document.querySelector('.menu-principal__btn');
//console.log(botao);
let menu = document.querySelector('.menu-principal');

botao.addEventListener("click",abreMenu);

function abreMenu(){
    menu.classList.toggle("menu-principal--fechado");
}