function showMenu() {
  document.getElementsByClassName('PhoneNavigation')[0].style.display = "block";
  document.getElementsByClassName('menuClose')[0].style.display = "inline-block";
  document.getElementsByClassName('menuOpen')[0].style.display = "none";
}
function closeMenu() {
  document.getElementsByClassName('PhoneNavigation')[0].style.display = "none";
  document.getElementsByClassName('menuClose')[0].style.display = "none";
  document.getElementsByClassName('menuOpen')[0].style.display = "inline-block";
}