document.addEventListener("DOMContentLoaded", async function () {
    const urlUF = "https://servicodados.ibge.gov.br/api/v1/localidades/estados";
    const uf = document.getElementById("uf");
    const cidade = document.getElementById("cidade");
    const buscarBtn = document.querySelector(".form_pes_botao");
    const clinicasSP = document.querySelectorAll("#clinica-saopaulo"); // Seleciona todas as divs com esse ID

    // Esconde todas as divs das clínicas no início
    clinicasSP.forEach(clinica => clinica.style.display = "none");

    // Carregar as UFs
    const requestUF = await fetch(urlUF);
    const responseUF = await requestUF.json();

    uf.innerHTML = '<option value="">Selecione o estado</option>';
    responseUF.forEach(function (estado) {
        uf.innerHTML += `<option value="${estado.sigla}">${estado.nome}</option>`;
    });

    // Atualiza as cidades ao selecionar um estado
    uf.addEventListener("change", async function () {
        if (uf.value === "") {
            cidade.innerHTML = '<option value="">Selecione a cidade</option>';
            return;
        }

        const urlCidades = `https://servicodados.ibge.gov.br/api/v1/localidades/estados/${uf.value}/municipios`;
        const requestCidades = await fetch(urlCidades);
        const responseCidades = await requestCidades.json();

        cidade.innerHTML = '<option value="">Selecione a cidade</option>';
        responseCidades.forEach(function (municipio) {
            cidade.innerHTML += `<option value="${municipio.nome}">${municipio.nome}</option>`;
        });
    });

    // Exibir todas as clínicas quando UF e cidade forem São Paulo
    buscarBtn.addEventListener("click", function (event) {
        event.preventDefault(); // Evita o comportamento padrão do link

        const estadoSelecionado = uf.value;
        const cidadeSelecionada = cidade.value;

        if (estadoSelecionado === "SP" && cidadeSelecionada === "São Paulo") {
            clinicasSP.forEach(clinica => clinica.style.display = "block");
        } else {
            clinicasSP.forEach(clinica => clinica.style.display = "none");
        }
    });
});
