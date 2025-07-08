const express = require('express');
const axios = require('axios');
const app = express();

// Целевой URL
const TARGET_URL = 'https://hyperttp2.github.io/VNShow/ ';

app.get('/*', async (req, res) => {
    try {
        const url = TARGET_URL + req.params[0]; // передаём весь путь
        const response = await axios.get(url);
        res.set(response.headers);
        res.send(response.data);
    } catch (err) {
        console.error('Ошибка:', err.message);
        res.status(500).send('Ошибка загрузки контента');
    }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`🚀 Прокси-сервер запущен на порту ${PORT}`);
});
