
function SwapDivsWithClick(div1,div2)
{
   d1 = document.getElementById(div1);
   d2 = document.getElementById(div2);
   if( d2.style.display == "none" )
   {
      d1.style.display = "none";
      d2.style.display = "block";
   }
   else
   {
      d1.style.display = "block";
      d2.style.display = "none";
   }
}

function invisible(formID)
{
configureForm = document.getElementsByClassName("configure-forms");
for (var i = 0, max = configureForm.length; i < max; i++) {
   configureForm[i].style.display = "none";
}
formID.style.display="block";
}