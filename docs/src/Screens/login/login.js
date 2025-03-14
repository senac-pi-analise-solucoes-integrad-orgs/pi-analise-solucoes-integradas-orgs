const API_URL = 'https://pi-analise-solucoes-integradas-production.up.railway.app/';

document.addEventListener('DOMContentLoaded', () => {
    const form = document.forms[0];
    form.addEventListener('submit', submitHandler);

    function submitHandler(e) {
        e.preventDefault();
        const url = `${API_URL}api-token-auth/`
        fetch(url, {
            method: 'post',
            body: new URLSearchParams(new FormData(form))
        })
            .then(response => response.json())
            .then(({token}) => {
                Cookies.set('token', token);
                window.location.href = '/';
            })
    }
});
