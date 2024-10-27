function handleSubmit() {
    if (document.getElementById('searchbox').value !== "") {
        alert('Form is being submitted!');
        document.getElementById('myForm').submit(); // This line actually submits the form
        console.log("clean");
    } else {
        alert('Form is emprty');
    }
}