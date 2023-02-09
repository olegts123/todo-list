var btnContainer = document.getElementById("leftside");
var btns = btnContainer.getElementsByClassName("leftside-item");
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("item-active");
    if (current.length > 0) {
        current[0].className = current[0].className.replace(" item-active", "");
    }
    this.className += " item-active";
  });
}