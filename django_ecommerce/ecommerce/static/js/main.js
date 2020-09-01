$(window).on('load', function() {
	/*------------------
		Preloder
	--------------------*/
	$(".loader").fadeOut();
	$("#preloder").delay(400).fadeOut("slow");

});

(function($) {
	/*------------------
		Navigation
	--------------------*/
	$('.main-menu').slicknav({
		prependTo:'.main-navbar .container',
		closedSymbol: '<i class="flaticon-right-arrow"></i>',
		openedSymbol: '<i class="flaticon-down-arrow"></i>'
	});


	/*------------------
		ScrollBar
	--------------------*/
	$(".cart-table-warp, .product-thumbs").niceScroll({
		cursorborder:"",
		cursorcolor:"#afafaf",
		boxzoom:false
	});


	/*------------------
		Category menu
	--------------------*/
	$('.category-menu > li').hover( function(e) {
		$(this).addClass('active');
		e.preventDefault();
	});
	$('.category-menu').mouseleave( function(e) {
		$('.category-menu li').removeClass('active');
		e.preventDefault();
	});


	/*------------------
		Background Set
	--------------------*/
	$('.set-bg').each(function() {
		var bg = $(this).data('setbg');
		$(this).css('background-image', 'url(' + bg + ')');
	});



	/*------------------
		Hero Slider
	--------------------*/
	var hero_s = $(".hero-slider");
    hero_s.owlCarousel({
        loop: true,
        margin: 0,
        nav: true,
        items: 1,
        dots: true,
        animateOut: 'fadeOut',
    	animateIn: 'fadeIn',
        navText: ['<i class="flaticon-left-arrow-1"></i>', '<i class="flaticon-right-arrow-1"></i>'],
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: true,
        onInitialized: function() {
        	var a = this.items().length;
            $("#snh-1").html("<span>1</span><span>" + a + "</span>");
        }
    }).on("changed.owl.carousel", function(a) {
        var b = --a.item.index, a = a.item.count;
    	$("#snh-1").html("<span> "+ (1 > b ? b + a : b > a ? b - a : b) + "</span><span>" + a + "</span>");

    });

	hero_s.append('<div class="slider-nav-warp"><div class="slider-nav"></div></div>');
	$(".hero-slider .owl-nav, .hero-slider .owl-dots").appendTo('.slider-nav');



	/*------------------
		Brands Slider
	--------------------*/
	$('.product-slider').owlCarousel({
		loop: false,
		nav: true,
		dots: false,
		margin: 30,
		autoplay: true,
		navText: ['<i class="flaticon-left-arrow-1"></i>', '<i class="flaticon-right-arrow-1"></i>'],
		responsive: {
			0 : {
				items: 1,
			},
			480 : {
				items: 2,
			},
			768 : {
				items: 3,
			},
			1200 : {
				items: 4,
			}
		}
	});


	/*------------------
		Popular Services
	--------------------*/
	$('.popular-services-slider').owlCarousel({
		loop: true,
		dots: false,
		margin: 40,
		autoplay: true,
		nav: true,
		navText:['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>'],
		responsive: {
			0 : {
				items: 1,
			},
			768 : {
				items: 2,
			},
			991: {
				items: 3
			}
		}
	});


	/*------------------
		Accordions
	--------------------*/
	$('.panel-link').on('click', function (e) {
		$('.panel-link').removeClass('active');
		var $this = $(this);
		if (!$this.hasClass('active')) {
			$this.addClass('active');
		}
		e.preventDefault();
	});


	/*-------------------
		Range Slider
	--------------------- */
	var rangeSlider = $(".price-range"),
		minamount = $("#minamount"),
		maxamount = $("#maxamount"),
		minPrice = rangeSlider.data('min'),
		maxPrice = rangeSlider.data('max');
	rangeSlider.slider({
		range: true,
		min: minPrice,
		max: maxPrice,
		values: [minPrice, maxPrice],
		slide: function (event, ui) {
			minamount.val('$' + ui.values[0]);
			maxamount.val('$' + ui.values[1]);
		}
	});
	minamount.val('$' + rangeSlider.slider("values", 0));
	maxamount.val('$' + rangeSlider.slider("values", 1));


	/*-------------------
		Quantity change
	--------------------- */
    var proQty = $('.pro-qty');
	proQty.prepend('<span class="dec qtybtn">-</span>');
	proQty.append('<span class="inc qtybtn">+</span>');
	proQty.on('click', '.qtybtn', function () {
		var $button = $(this);
		var oldValue = $button.parent().find('input').val();
		if ($button.hasClass('inc')) {
			var newVal = parseFloat(oldValue) + 1;
		} else {
			// Don't allow decrementing below zero
			if (oldValue > 0) {
				var newVal = parseFloat(oldValue) - 1;
			} else {
				newVal = 0;
			}
		}
		$button.parent().find('input').val(newVal);
	});



	/*------------------
		Single Product
	--------------------*/
	$('.product-thumbs-track > .pt').on('click', function(){
		$('.product-thumbs-track .pt').removeClass('active');
		$(this).addClass('active');
		var imgurl = $(this).data('imgbigurl');
		var bigImg = $('.product-big-img').attr('src');
		if(imgurl != bigImg) {
			$('.product-big-img').attr({src: imgurl});
			$('.zoomImg').attr({src: imgurl});
		}
	});


	$('.product-pic-zoom').zoom();



})(jQuery);


/*------------------
	Mega Menu Click to open/close child categories dropdown
--------------------*/
const megaMenuItems = document.getElementsByClassName('triangle-down');
for (let i=0; i < megaMenuItems.length; i++) {
	if (megaMenuItems[i].classList.contains('slicknav_parent')) {
		continue
	}
	megaMenuItems[i].addEventListener("click", function(event) {
		if (!megaMenuItems[i].classList.contains('main-menu-clicked')) {
			megaMenuItems[i].classList.add('main-menu-clicked')
			megaMenuItems[i].getElementsByClassName('sub-menu')[0].setAttribute("style", "visibility: visible; opacity: 1; margin-top: 0;");
		}
		else {
			megaMenuItems[i].classList.remove('main-menu-clicked')
			megaMenuItems[i].getElementsByClassName('sub-menu')[0].setAttribute("style", "visibility: hidden; opacity: 0; margin-top: 50;")
		}

		document.addEventListener('click', function(event) {
			var isClickInside = megaMenuItems[i].contains(event.target);
	
			if (!isClickInside) {
				megaMenuItems[i].classList.remove('main-menu-clicked')
				megaMenuItems[i].getElementsByClassName('sub-menu')[0].setAttribute("style", "visibility: hidden; opacity: 0; margin-top: 50;")
			}
	})
})};


/*------------------
	Mega Menu Click to open/close child categories dropdown inside dropdown
--------------------*/
const megaMenuDropdownItems = document.getElementsByClassName('triangle-right');
for (let i=0; i < megaMenuDropdownItems.length; i++) {
	if (megaMenuDropdownItems[i].classList.contains('slicknav_parent')) {
		megaMenuDropdownItems[i].classList.remove('triangle-right')
		i -= 1
		continue
	}
	megaMenuDropdownItems[i].addEventListener('mouseover', function(event) {
		megaMenuDropdownItems[i].getElementsByClassName('dropdown-sub-menu')[0].setAttribute("style", "visibility: visible; opacity: 1;")
		}
	)
	megaMenuDropdownItems[i].addEventListener('mouseout', function(event) {
		megaMenuDropdownItems[i].getElementsByClassName('dropdown-sub-menu')[0].setAttribute("style", "visibility: hidden; opacity: 0;")
		}
	)
};


/*------------------
	Mobile Mega Menu Click to open link inside categories dropdown
--------------------*/
const mobileMegaMenuItems = document.getElementsByClassName('slicknav_item slicknav_row')
for (let i=0; i < mobileMegaMenuItems.length; i++) {
	let mobileLink = mobileMegaMenuItems[i].children[0].pathname
	mobileMegaMenuItems[i].children[0].addEventListener('click', function(event) {
		location.href = mobileLink
	})
};


/*------------------
	Mobile Mega Menu Click changing background inside categories dropdown for closed dropdown
--------------------*/
const mobileDropdownList = document.getElementsByClassName('slicknav_item slicknav_row')
for (let mobileDropdown of mobileMegaMenuItems) {
	mobileDropdown.addEventListener('click', function(event) {
		if (!mobileDropdown.classList.contains('slicknav_clicked')) {
			mobileDropdown.classList.add('slicknav_clicked')
		}
		else {
			mobileDropdown.classList.remove('slicknav_clicked')
		}
	})
};


/*------------------
	Adjusting products label "on sale" and "new". If they both are present on product, then "on sale" will be displayed on left and "new" on right.
	If only one label on product, then it will be displayed on right
--------------------*/
const productOnImageLabelItems = document.getElementsByClassName('product-on-image-labels')
for (let productLabels of productOnImageLabelItems) {
	if (productLabels.childElementCount >= 2){
		for (let child of productLabels.children) {
			if (child.classList.contains('tag-sale')) {
				child.classList.add('tag-sale-moved-left')
			}
		}
	}
};