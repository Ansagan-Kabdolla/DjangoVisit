function CardArea(idCardArea) {
    Container.call(this, idCardArea);

    this.countCard = 0; //Общее количество товаров
    this.renderCardList();
}

CardArea.prototype = Object.create(Container.prototype);
CardArea.prototype.constructor = CardArea;

let cardItems = [];
let allCardItems = [];
let idCardItems = [];
let renderCardItems = [];
let currentPage = 1;
let lastId;
let cardItemsLength;

CardArea.prototype.renderCardList = function () {

    var json = new XMLHttpRequest();
    json.open('GET', '../ajax.json', true);
    json.send();
    json.onreadystatechange = function () {
        if (json.readyState === 4 && json.status === 200) {
            console.log("state = 4");
            var cardDB = JSON.parse(json.responseText);

            //////////////////////////////////////////

            let cardCount = 0;
            let allowItems;

            if ($("body").attr("class").includes("wts")) {
                let cardCount = 0;
                allowItems = 6;

                for (let itemKey of cardDB.wts) {
                    allCardItems.push(itemKey);
                }

                for (let itemKey of allCardItems) {
                    if (cardCount < 6) {
                        idCardItems.push(itemKey.id);
                        var newCard = new Card("wts", itemKey.id, itemKey.title, itemKey.photo, itemKey.link, itemKey.price, itemKey.HType, itemKey.stars, itemKey.review);
                        newCard.render();
                        cardCount++;
                    }
                }
            } else if ($("body").attr("class").includes("wtg")) {
                let cardCount = 0;
                allowItems = 8;

                for (let itemKey of cardDB.wtg) {
                    allCardItems.push(itemKey);
                }

                for (var itemKey of allCardItems) {
                    if (cardCount < 8) {
                        idCardItems.push(itemKey.id);
                        let newCard = new Card("wtg", itemKey.id, itemKey.title, itemKey.photo, itemKey.link, itemKey.price, itemKey.HType, itemKey.stars, itemKey.review);
                        newCard.render();
                        cardCount++;
                    }
                }
            } else if ($("body").attr("class").includes("event")) {
                let cardCount = 0;
                allowItems = 8;

                for (let itemKey of cardDB.event) {
                    allCardItems.push(itemKey);
                }

                for (let itemKey of allCardItems) {
                    if (cardCount < 8) {
                        idCardItems.push(itemKey.id);
                        let newCard = new Card("event", itemKey.id, itemKey.title, itemKey.photo, itemKey.link, itemKey.date, itemKey.place, '', '');
                        newCard.render();
                        cardCount++;
                        lastId = itemKey.id;
                    }
                }
            } else if ($("body").attr("class").includes("wte")) {
                let cardCount = 0;
                allowItems = 6;

                for (let itemKey of cardDB.wte) {
                    allCardItems.push(itemKey);
                }

                for (let itemKey of allCardItems) {
                    if (cardCount < 6) {
                        idCardItems.push(itemKey.id);
                        var newCard = new Card("wte", itemKey.id, itemKey.title, itemKey.photo, itemKey.link, itemKey.price, itemKey.HType, itemKey.stars, itemKey.review);
                        newCard.render();
                        cardCount++;
                    }
                }
            }

            var card_area = $(".pag_page");

            cardItemsLength = allCardItems.length / allowItems;

            if(cardItemsLength < 1){
                cardItemsLength = 1;
            }
            console.log(allowItems)
            console.log(cardItemsLength)


            if (cardItemsLength > cardItemsLength.toFixed()) {
                cardItemsLength = cardItemsLength.toFixed();
                cardItemsLength++;
            } else{
                cardItemsLength = cardItemsLength.toFixed();
            }

            let maxli = 5;

            for (let i = 1; i <= (cardItemsLength > 5 ? maxli : cardItemsLength) ; i++) {

                let $page_num_link = $("<a />", {
                    class: "page-link page_number",
                    text: i
                });

                if( i !== 5){

                    let $page_list_item = $("<li />", {
                        class: "page-item page-item_" + i
                    });

                    $page_list_item.append($page_num_link);
                    $(".pagination").append($page_list_item);
                } else{

                    let $page_list_item = $("<li />", {
                        class: "page-item page-item_" + i + " page-item_last"
                    });

                    $page_list_item.append($page_num_link);
                    $(".pagination").append($page_list_item);
                }
            }

            if(cardItemsLength == 1){
                $(".page_next").addClass("disabled");
            }
            $(".page-item_" + currentPage).addClass("active");

        } else {
            console.log("status is not 4");
        }
    };
};

CardArea.prototype.refreshPage = function (card_type) {
    let lastPage = $(".page-item_last").text();
    let firstPage = lastPage - 4;

    if(lastPage > cardItemsLength){
        lastPage = cardItemsLength;
    }

    $(".page-item_" + currentPage).addClass("active");
    $(".view-content").empty();

    if(currentPage == cardItemsLength){
        $(".page_next").addClass("disabled");
    }else {
        $(".page_next").removeClass("disabled");
    }
    if(currentPage > 1){
        $(".page_prev").removeClass("disabled");
    } else{
        $(".page_prev").addClass("disabled");
    }

    console.log(" first - " + firstPage);
    console.log(" last - " + lastPage)
    console.log(" last - " + cardItemsLength)

    if(currentPage == lastPage && lastPage <= cardItemsLength -1 ){
        lastPage++;
        firstPage = lastPage - 4;

        $(".pagination").empty();

        for (let i = lastPage - 4; i <= lastPage; i++) {

            let $page_num_link = $("<a />", {
                class: "page-link page_number",
                text: i
            });

            if( i !== lastPage){

                let $page_list_item = $("<li />", {
                    class: "page-item page-item_" + i
                });

                $page_list_item.append($page_num_link);
                $(".pagination").append($page_list_item);
            } else{

                let $page_list_item = $("<li />", {
                    class: "page-item page-item_" + i + " page-item_last"
                });

                $page_list_item.append($page_num_link);
                $(".pagination").append($page_list_item);
            }
        }
        $(".page-item_" + currentPage).addClass("active");
    }

    if(currentPage == firstPage && firstPage >= 2){
        firstPage--;
        lastPage = firstPage + 4;

        $(".pagination").empty();

        for (let i = firstPage; i <= lastPage; i++) {

            let $page_num_link = $("<a />", {
                class: "page-link page_number",
                text: i
            });

            if( i !== lastPage){

                let $page_list_item = $("<li />", {
                    class: "page-item page-item_" + i
                });

                $page_list_item.append($page_num_link);
                $(".pagination").append($page_list_item);
            } else{

                let $page_list_item = $("<li />", {
                    class: "page-item page-item_" + i + " page-item_last"
                });

                $page_list_item.append($page_num_link);
                $(".pagination").append($page_list_item);
            }
        }
        $(".page-item_" + currentPage).addClass("active");
    }


    for (let itemKey of renderCardItems) {
        if (card_type !== 'event') {
            let newCard = new Card(card_type, itemKey.id, itemKey.title, itemKey.photo, itemKey.link, itemKey.price, itemKey.HType, itemKey.stars, itemKey.review);
            newCard.render();
        } else {
            let newCard = new Card(card_type, itemKey.id, itemKey.title, itemKey.photo, itemKey.link, itemKey.date, itemKey.place, '', '');
            newCard.render();
        }
    }
}


CardArea.prototype.add = function (type, btn_type, num_type) {
    let btnType = btn_type;
    let card_type = type;
    let numType = num_type;

    if (btnType.includes("page_number")) btnType = "num"
    if (btnType.includes("page_link_next")) btnType = "next"
    if (btnType.includes("page_link_prev")) btnType = "prev"

    let cardCount = 0;
    let allowItems;
    if (card_type == "wtg" || card_type == "event") {
        allowItems = 8;
    } else if (card_type == "wts" || card_type == "wte") {
        allowItems = 6;
    }

    renderCardItems.length = 0;

    if (btnType === "next") {
        cardCount = 0;
        $(".page-item_" + currentPage).removeClass("active");
        currentPage++;

        if(currentPage > cardItemsLength){
            currentPage = cardItemsLength;
        }

        for (let itemKey of allCardItems) {
                if (cardCount < allowItems) {
                    if (itemKey.id > (currentPage * allowItems - allowItems) && itemKey.id <= currentPage * allowItems) {
                    idCardItems.push(itemKey.id);
                    renderCardItems.push(itemKey);
                    cardCount++;
                    lastId = itemKey.id;
                }
            }
        }

        this.refreshPage(card_type);

    } else if (btnType === "prev") {
        cardCount = 0;
        $(".page-item_" + currentPage).removeClass("active");
        currentPage--;

        if(currentPage < 1){
            currentPage = 1;
        }

        for (let itemKey of allCardItems) {
            let boolId = false;
            if (itemKey.id > (currentPage * allowItems - allowItems) && itemKey.id <= currentPage * allowItems) {
                if (cardCount < allowItems) {
                    idCardItems.push(itemKey.id);
                    renderCardItems.push(itemKey);
                    cardCount++;
                    lastId = itemKey.id;
                }
            }
        }

        this.refreshPage(card_type);
    } else if (btnType === "num") {
        cardCount = 0;
        $(".page-item_" + currentPage).removeClass("active");
        currentPage = numType;

        for (let itemKey of allCardItems) {
            let boolId = false;
            if (itemKey.id > (currentPage * allowItems - allowItems) && itemKey.id <= currentPage * allowItems) {
                if (cardCount < allowItems) {
                    idCardItems.push(itemKey.id);
                    renderCardItems.push(itemKey);
                    cardCount++;
                    lastId = itemKey.id;
                }
            }
        }

        this.refreshPage(card_type);
    }

};


CardArea.prototype.refresh = function () {
    var CardArea_area = $(".view_content");
    CardArea_area.empty();
    this.renderCardList();
};
