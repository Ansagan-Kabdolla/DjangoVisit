function Card(str_type, id, title, photo, link, price, type, stars, review) {
    Container.call(this, id);
    this.str_type = str_type;
    this.id = id;
    this.title = title;
    this.link = link;
    this.photo = photo;
    this.price = price;
    this.type = type;
    this.stars = stars;
    this.review = review;

    // if(this.type == undefined){
    //     this.type = '';
    // } else if(this.review == undefined){
    //     this.review = 0;
    // } else if(this.stars == undefined){
    //     this.type = 0;
    // }
}

Card.prototype = Object.create(Container.prototype);
Card.prototype.constructor = Card;

Card.prototype.render = function () {

    if(this.str_type == "wts"){

        var $cardContainer = $('<div />', {
            class: 'views-row views-row-first'
        });

        var $cardContainer_1= $('<div />', {
            class: 'views-field views-field-nothing'
        });

        var $cardContainer_2= $('<span />', {
            class: 'field-content'
        });

        var $cardContainer_3= $('<div />', {
            class: 'row'
        });

        var $card_area = $(".wts_list");

        var $cardImgContainer= $('<div />', {
            class: 'col-md-4 col-xs-12 blo_imghei'
        });

        var $img = $('<img />', {
            class: 'img-responsive stay_img',
            src: this.photo,
            width: "280",
            height: "222",
            alt: "Hotel"
        });

        var $cardContent = $('<div />', {
            class: 'col-md-5 zg_block',
            "data-id": this.id,
            "data-price": this.price
        });

        var $cardContentIn = '<a href="../tmp/gostevye-doma.html" typeof="skos:Concept" property="rdfs:label skos:prefLabel">' + this.type + '</a><div class="zg_hotel"><a href="' + this.link + '">' + this.title + '</a></div><img src="../img/' + this.stars + '.png "><div class="kolvo">' + this.review + ' отзывов</div><p><img style="margin-top: -5px; margin-right: 5px;" src="../img/nakarte.png">Посмотреть на карте</p>';

        var $cardPrice = '<div class="col-md-3 cena_block"><div class="cena_hotel"><p>Цена от: <span>' + this.price + '</span>тенге</p></div></div>';

        var $cardBtn = $('<a />', {
            class: 'rmenu_content_item_btn',
            'data-id': this.id,
            text: 'Add to card'
        });

        $cardImgContainer.append($img);
        $cardContent.append($cardContentIn);
        $cardContainer_3.append($cardImgContainer);
        $cardContainer_3.append($cardContent);
        $cardContainer_3.append($cardPrice);
        $cardContainer_2.append($cardContainer_3);
        $cardContainer_1.append($cardContainer_2);
        $cardContainer.append($cardContainer_1);
        $card_area.append($cardContainer);

    } else if(this.str_type == "wtg") {

        var $cardContainer = $('<div />', {
            class: 'views-row content_item'
        });

        var $cardContainer_1= $('<div />', {
            class: 'views-field views-field-nothing'
        });

        var $cardContainer_2= $('<span />', {
            class: 'field-content'
        });

        var $cardContainer_3 = $('<div />', {
            class: 'event_page_b'
        });

        var $card_area = $(".wtg_list");

        let $wtg_content = '<a href="' + this.link  + '"><div class="imgtimer"><img typeof="foaf:Image" class="img-responsive event_img" src="' + this.photo + ' "width="325" height="215" alt="PHOTO"></div> <div class="event_zagol"> <p>' + this.title + '</p></div> </a>';


        $cardContainer_3.append($wtg_content);
        $cardContainer_2.append($cardContainer_3);
        $cardContainer_1.append($cardContainer_2);
        $cardContainer.append($cardContainer_1);
        $card_area.append($cardContainer);

    } else if(this.str_type == "event") {

        var $cardContainer = $('<div />', {
            class: 'views-row content_item'
        });

        var $cardContainer_1= $('<div />', {
            class: 'views-field views-field-nothing'
        });

        var $cardContainer_2= $('<span />', {
            class: 'field-content'
        });

        var $cardContainer_3 = $('<div />', {
            class: 'event_page_b'
        });

        var $card_area = $(".event_list");

        let $event_content = '<div class="imgtimer"><img typeof="foaf:Image" class="img-responsive event_img" src="' + this.photo + '" width="325" height="215" alt=""></div><div class="event_zagol"> <p>' +  this.title  +  '</p> </div> <div class="timer"> <p class="timer_text">Дата</p><span class="date-display-single" property="dc:date" datatype="xsd:dateTime" content="2019-05-11T11:15:00+06:00">' + this.price + '</span> </div> <div class="event_mesto">' +  this.type + '</div>';

        $cardContainer_3.append($event_content);
        $cardContainer_2.append($cardContainer_3);
        $cardContainer_1.append($cardContainer_2);
        $cardContainer.append($cardContainer_1);
        $card_area.append($cardContainer);

    } else if(this.str_type == "wte") {

        var $cardContainer = $('<div />', {
            class: 'views-row views-row-first'
        });

        var $cardContainer_1= $('<div />', {
            class: 'views-field views-field-nothing'
        });

        var $cardContainer_2= $('<span />', {
            class: 'field-content'
        });

        var $cardContainer_3= $('<div />', {
            class: 'row'
        });

        var $card_area = $(".wte_list");

        var $cardImgContainer= $('<div />', {
            class: 'col-md-4 col-xs-12 blo_imghei'
        });

        var $img = $('<img />', {
            class: 'img-responsive item_img',
            src: this.photo,
            width: "280",
            height: "222",
            alt: "Hotel"
        });

        var $cardContent = $('<div />', {
            class: 'col-md-5 zg_block',
            "data-id": this.id,
            "data-price": this.price
        });

        var $cardContentIn = '<a href="../tmp/gostevye-doma.html" typeof="skos:Concept" property="rdfs:label skos:prefLabel">' + this.type + '</a><div class="zg_hotel"><a href="' + this.link + '">' + this.title + '</a></div><div class="kolvo">' + this.review + ' отзывов</div><p><img style="margin-top: -5px; margin-right: 5px;" src="../img/nakarte.png">Посмотреть на карте</p>';

        var $cardPrice = '<div class="col-md-3 cena_block"><div class="cena_hotel"><p>Средний чек: <span>' + this.price + '</span>тенге</p></div></div>';


        $cardImgContainer.append($img);
        $cardContent.append($cardContentIn);
        $cardContainer_3.append($cardImgContainer);
        $cardContainer_3.append($cardContent);
        $cardContainer_3.append($cardPrice);
        $cardContainer_2.append($cardContainer_3);
        $cardContainer_1.append($cardContainer_2);
        $cardContainer.append($cardContainer_1);
        $card_area.append($cardContainer);
    }
};