function show() {


if ( document.getElementById('menuClose').className === "menu") {

  document.getElementsByClassName('left')[0].style.display = "inline-block";
  document.getElementsByClassName('right')[0].style.display = "none";
  document.getElementById('menuClose').className = "menuOpen"
} else {

  document.getElementsByClassName('left')[0].style.display = "none";
  document.getElementsByClassName('right')[0].style.display = "inline-block";
  document.getElementById('menuClose').className = "menu"

}

  
  // document.getElementsByClassName('menuOpen')[0].style.display = "none";
}



// function close() {

//   document.getElementsByClassName('left')[0].style.display = "none";
//   document.getElementsByClassName('right')[0].style.display = "inline-block";

// }