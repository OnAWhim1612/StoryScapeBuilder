function checkInput() {
    const userInput = document.getElementById("userInput").value; // No need to convert to lowercase
  
    // Define the correct text
    const correctText = "P@$$w0rd!Cyb3r#Sec21";
  
    // Check if the user input matches the correct text
    if (userInput === correctText) {
      document.getElementById("feedback").innerText = "Correct";
    } else {
      document.getElementById("feedback").innerText = "Wrong";
    }
  }




 