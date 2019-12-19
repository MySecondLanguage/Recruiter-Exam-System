const axios = require('axios');

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

const host = window.location.hostname
const port = window.location.port

const protocol = window.location.protocol

// get root url
const rootUrl = port ? `${protocol}//${host}:${port}/` : `${protocol}//${host}/`;
const subUrl = 'api/v1/'

//  considered as api root url
const apiUrl = `${rootUrl}${subUrl}`

const apiHelper = {
    getQuestionList: () => axios.get(`${apiUrl}question-list/`),
    setResult: (data, params={}) => axios.post(`${apiUrl}create-result/`, data, {params}),
    getResultSummery: () => axios.get(`${apiUrl}result-summery/`),
};

export default apiHelper;