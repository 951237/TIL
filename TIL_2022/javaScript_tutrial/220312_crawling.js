const axios = require("axios");
const cheerio = require("cheerio");

const getHTML = async() => {
    try{
        URL = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%8C%80%EC%A0%84+%EC%97%B0%EA%B7%B9&oquery=%EB%8C%80%EC%A0%84+%EA%B3%B5%EC%97%B0&tqi=U8ozasprvxZsseDZaHlssssss1C-250912";
        return await axios.get(URL);
    } catch(error){
        console.error(error);
    }
};

getHTML()
    .then(html => {
        let ulList = [];
        const $ = cheerio.load(html.data);
        const $bodyList = $('ul').children('li');
        $bodyList.each(function(i, elem){
            ulList[i] = {
                title : $(this).find('div.title_box strong').text(),
                url : 'search.naver.com/search.naver' + $(this).find('a').attr('href'),
                img_url : $(this).find('div.item img').attr('src'),
                img_alt : $(this).find('div.item img').attr('alt'),
            }
        });
        const data = ulList.filter(n => n.title);
        return data;
    })
    .then(res => {
        console.log(res);
    });

