const axios = require("axios");
const cheerio = require("cheerio");

const getHTML = async() => {
    try{
        return await axios.get(URL);
    } catch(error){
        console.error(error);
    }
};

