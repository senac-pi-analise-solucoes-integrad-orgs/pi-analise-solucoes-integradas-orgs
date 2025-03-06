$(document).ready(function () {
    const form = document.forms[0];
    form.addEventListener('submit', submitHandler);
    function submitHandler(e) {
        e.preventDefault();
        fetch(form.action, {
            method: 'post',
            body: new URLSearchParams(new FormData(form))
        })
            .then(response => response.json())
            .then(data => console.log(data.token))
    }
});
