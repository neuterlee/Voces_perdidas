// File: /disappearance-web/disappearance-web/src/app.js

const fs = require('fs');
const path = require('path');
const axios = require('axios');

const textFilePath = path.join(__dirname, '../data/cedulassampledes.txt');
const displayElement = document.getElementById('disappearance-description');

async function fetchDescription() {
    try {
        const data = fs.readFileSync(textFilePath, 'utf8');
        const cases = data.split('\n').filter(line => line.trim() !== '');
        const randomCase = cases[Math.floor(Math.random() * cases.length)];
        const narrative = await generateNarrative(randomCase);
        displayElement.innerText = narrative;
    } catch (error) {
        console.error('Error reading the file or generating narrative:', error);
    }
}

async function generateNarrative(caseDescription) {
    try {
        const response = await axios.post('https://api.deepai.org/api/text-generator', {
            text: caseDescription
        }, {
            headers: {
                'api-key': 'YOUR_DEEPAI_API_KEY'
            }
        });
        return response.data.output;
    } catch (error) {
        console.error('Error generating narrative:', error);
        return 'Error generating description.';
    }
}

document.addEventListener('DOMContentLoaded', fetchDescription);