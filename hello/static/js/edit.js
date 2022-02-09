function mobil(selector) {
	// body...
	let element = document.querySelector(selector)
	return element
}

function checkmediaquery() {
	// body...
	const media_query =window.screen.availWidth;
	let element = mobil('.welcome-text')
	if (media_query < 600 ) {
		console.log("no no")
		console.log("aver ")
		element.style.padding = "39rem 7rem";
		element.style.margin = '20% 20%';
		element;
		console.log(media_query, window.screen.availHeight)
	} else if ( media_query > 768) {


		console.log( media_query)
		console.log(media_query, window.screen.availHeight)


	} else {
		if (element.attributes.length > 1) {
			// statement
			element.attributes.removeNamedItem('style');
		};
		console.log(media_query, window.screen.availHeight)

	}

};

// iniyalizar


checkmediaquery()

// inset event


addEventListener('resize', checkmediaquery)