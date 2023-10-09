document.addEventListener('DOMContentLoaded', function() {
    var runButton = document.getElementById('runButton');
    var activationSound = document.getElementById('activationSound');
    var successSound = document.getElementById('successSound');
    
    if (activationSound) {
        runButton.addEventListener('click', function() {
            activationSound.play();
        });
    }
    
    if (successSound) {
        successSound.play();
    }
});
