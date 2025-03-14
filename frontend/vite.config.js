import dotenv from 'dotenv';

dotenv.config();

export default {
    root: "./src",
    build: {
        outDir: "../dist",
        emptyOutDir: true,
        rollupOptions: {
            input: {
                index: "./src/index.html",
                login: "./src/login.html",
                cadastro: "./src/cadastro.html",
                cadastro_profissional: "./src/cadastro_profissional.html",
                perfil: "./src/perfil.html",
            },
        },
    },
};