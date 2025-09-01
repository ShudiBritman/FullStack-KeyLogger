document.getElementById("button1").onclick = yor_age;

function yor_age(){
let age = document.getElementById("input_serch").value;

  if (age === "")
    return;

  age = Number(age);
  if (isNaN(age))
    alert("לא הוכנס מספר")

  else if (age < 21)
     alert("אתה צעיר מידי, התוכנית מיועדת לגילאי 21-28.");
  else if (age > 28)
     alert("אתה מבוגר מידי, התוכנית מיועדת לגילאי 21-28.");    
  else
     alert("מעולה בא נעבור לשלב הבא")
}
