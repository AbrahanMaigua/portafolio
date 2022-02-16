// The following code is based off a toggle menu by @Bradcomp
// source: https://gist.github.com/Bradcomp/a9ef2ef322a8e8017443b626208999c1
(function() {
    var burger = document.querySelector('.burger');
    var menu = document.querySelector('#'+burger.dataset.target);
    burger.addEventListener('click', function() {
        burger.classList.toggle('is-active');
        menu.classList.toggle('is-active');
    });
})();


function mobil(selector) {
	// body...
	let element = document.querySelector(selector)
	return element
}

function checkmediaquery() {
	// body...
	const media_query =window.screen.availWidth;
	let element = mobil('.welcome-text')
	if (media_query < 652 ) {
		console.log("no no")
		console.log("aver ")
		element.style.padding = "16rem 7rem";
		//element.style.margin = '20% 20%';
		element;
		console.log(media_query, window.screen.availHeight)
	} else if ( media_query > 768) {


		console.log( media_query)
		console.log(media_query, window.screen.availHeight)


	} else {
		if (element.attributes.length > 1) {
			// statement
			element.attributes.removeNamedItem('style');
			console.log("delete")
		};
		console.log(media_query, window.screen.availHeight)

	}

};

// iniyalizar


checkmediaquery()

// inset event


addEventListener('resize', checkmediaquery)