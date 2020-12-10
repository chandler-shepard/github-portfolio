function openNav() {
    // document.querySelectorAll('.mySidenav').style.width = "250px"; 
    // document.querySelectorAll('#main').style.marginLeft = "250px"; 
    console.log(document.querySelectorAll('#mySidenav').style.width);
}

function closeNav() {
    document.querySelectorAll('#mySidenav').style.width = "0"; 
    document.querySelectorAll('#main').style.marginLeft = "0"; 
    console.log("closed");
  }

document.querySelector('.openbtn')
  .addEventListener('click', openNav);

document.querySelector('.closebtn')
  .addEventListener('click', closeNav);