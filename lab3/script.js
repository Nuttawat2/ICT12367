const textInput = document.getElementById('textInput');
const counter = document.getElementById('counter');

textInput.addEventListener('keyup', function() {
    counter.textContent = textInput.value.length;
});

textInput.addEventListener('paste', function() {
    setTimeout(() => {
        counter.textContent = textInput.value.length;
    }, 10);
});