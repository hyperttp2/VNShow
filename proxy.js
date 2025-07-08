const express = require('express');
const axios = require('axios');
const app = express();

// Базовый URL твоего сайта
const TARGET_URL = 'https://hyperttp2.github.io/VNShow/ ';

app.use((req, res) => {
    const url = TARGET_URL + req.url;
    axios.get(url)
        .then(response => {
            res.set(response.headers);
            res.send(response.data);
        })
        .catch(err => {
            console.error('Ошибка:', err.message);
            res.status(500).send('Произошла ошибка');
        });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Прокси-сервер запущен на http://localhost:${PORT}`);
});
