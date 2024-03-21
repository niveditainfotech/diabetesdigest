let dropav=document.getElementById('1')
let drop=document.querySelector('.drop');


drop.addEventListener('click',()=>{
    dropav.classList.toggle('work');
})

let mbtn=document.querySelector('.menuout')
let nav=document.querySelector('.naviout1')

mbtn.addEventListener('click',()=>{
    nav.classList.toggle('naviout2')
})