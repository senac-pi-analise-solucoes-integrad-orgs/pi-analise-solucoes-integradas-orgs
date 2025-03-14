const API_URL = 'https://pi-analise-solucoes-integradas-production.up.railway.app/';
const BASE_URL = 'https://senac-pi-analise-solucoes-integrad-orgs.github.io/pi-analise-solucoes-integradas-orgs/';

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
                window.location.href = BASE_URL;
            })
    }
});
