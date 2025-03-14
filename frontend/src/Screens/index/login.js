import Cookies from "js-cookie";

document.addEventListener("DOMContentLoaded", () => {
    const btnProfile = document.querySelector(".btn-sair a");
    const updateBtnProfile = () => btnProfile.textContent = Cookies.get("token") ? "Sair" : "Entrar"
    const handleBtnProfileClick = (e) => {
        if (Cookies.get("token")) {
            Cookies.remove("token");
            e.preventDefault();
            updateBtnProfile();
        }
    }
    updateBtnProfile();
    btnProfile.addEventListener("click", handleBtnProfileClick);
});