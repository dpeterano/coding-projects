let age = Number(prompt("Please enter your age:"));

while (age < 0 || age > 120) {
    alert("Invalid age. Please enter a valid age between 0 and 120.");
    age = Number(prompt("Please enter your age:"));
}
if (age < 18) {
    console.log("You're too young to have access to this website");
} else {
    document.getElementById("message").classList.add("shown");
}