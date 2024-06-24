
const display = document.getElementById('display');

function appendToDisplay(input) {

  display.value += input;

}

function clearDisplay() {

  display.value = "";

}

function calculate() {
  try {
    display.value = eval(display.value); // this built in function is new 
  }
  catch (error) {
    display.value = 'ERROR';
  }
}