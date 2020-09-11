var microphone = document.querySelector('.microphone');
microphone.onclick = function () {
    microphone.classList.add("record");
    var recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition || window.mozSpeechRecognition || window.msSpeechRecognition)();
    recognition.lang = 'en-US';
    recognition.start();

    recognition.onresult = function (event) {
        document.querySelector('.form-control').value = event.results[0][0].transcript;
        microphone.classList.remove("record");
    };

    recognition.onerror = function(event){
        recognition.stop();
    };
};