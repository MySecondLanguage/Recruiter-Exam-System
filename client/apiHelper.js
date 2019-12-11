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
    setResult: (question='none', choice_1='none', choice_2='none', choice_3='none', choice_4='none') => (
        axios.get(`${apiUrl}create-result/?question_id=${question}&choice_1=${choice_1}&choice_2=${choice_2}&choice_3=${choice_3}&choice_4=${choice_4}`)
    ),
};

export default apiHelper;