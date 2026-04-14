const express = require('express');
const axios = require('axios');

const app = express();

app.get('/', async (req, res) => {
  try {
    const response = await axios.get('https://api.github.com');
    res.send('Hello DevSecOps 🚀');
  } catch (err) {
    res.status(500).send('Error');
  }
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
