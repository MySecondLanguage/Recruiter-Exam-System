const axios = require('axios');

const host = window.location.hostname
const port = window.location.port
const protocol = window.location.protocol

// get root url
const rootUrl = port ? `${protocol}//${host}:8000/` : `${protocol}//${host}/`;
const subUrl = 'api/v1/'

//  considered as api root url
const apiUrl = `${rootUrl}${subUrl}`

const apiHelper = {
    getQuestionList: () => axios.get(`${apiUrl}question-list/`),
};

export default apiHelper;