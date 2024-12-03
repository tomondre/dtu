const axios = require('axios');

async function callGPT(prompt, model) {
    try {
        const url = 'https://api.openai.com/v1/chat/completions';
        const response = await axios.post(url, {
            model: model,
            messages: [{ role: 'user', content: prompt }],
        }, {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`
            }
        });

        const gptOutput = response.data.choices[0].message.content.trim();
        return cleanOutput(gptOutput);
    } catch (error) {
        throw new Error(`Error calling GPT API: ${error.message}`);
    }
}

function cleanOutput(gptOutput) {
    gptOutput = gptOutput.replace('```json', '');
    gptOutput = gptOutput.replace('```', '');
    return gptOutput;
}

module.exports = {
    callGPT
};
