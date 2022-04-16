console.log(document.forms["enigm1"]["code1"]);
document.forms["enigm1"].addEventListener("submit", (e) => {
  var erreur;
  var inputs = this.getElementsByTagName("code1");
  if ((inputs.value[0] = "123")) {
    erreur = "Bravo";
  } else {
    erreur = "Recommence";
  }
});
document.getElementsById("alerte").innerHTML = erreur;
