const title = document.querySelector("#title");

const CLICKED_CLASS = "clicked"; // html의 클래스 이름 

function handleClick() {
    const hasClass = title.classList.contains(CLICKED_CLASS); // 타이틀 클래스에 클래스가 포함되어 있는지 체크
    if (hasClass) {
        title.classList.remove(CLICKED_CLASS); // 클래스 리스트에서 클래스명 삭제
    } else {
        title.classList.add(CLICKED_CLASS); // 클래스 리스트에서 클래스명 추가
    }
}

function init() {
    title.addEventListener("click", handleClick);
}

init();