const display=document.getElementById("display");
const buttons=document.querySelectorAll(".calc-btn");

buttons.forEach(btn => {
  btn.addEventListener("click", () => {
    const value = btn.dataset.value;

    if (value === "=") {
      try {
        display.value = eval(display.value);
      } catch {
        display.value = "Error";
      }
    } else if (btn.id === "clear") {
      display.value = "";
       } else if (btn.id === "backspace") {
      display.value = display.value.slice(0, -1);
       } else if (btn.id === "sqrt") {
      display.value = "נו באמת שורש זה סתם מסובך";
    } else {
      display.value += value;
    }
  });
});