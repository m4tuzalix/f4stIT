main_js = """
    const days = arguments[0];
    const city_selector = arguments[1];
    const link = arguments[2];
    const date = arguments[3];
    
    function justJoinScraper(){
        const date_posted = link.querySelector(date).innerText
        if(!String(date_posted).includes("New")){
            const regex = /\d+/g
            var results = date_posted.match(regex)
            console.log(results[0])
            if(results[0] > days){
                return false
            }
        }
        return true
    }
    return justJoinScraper()
"""
scroll_js = """
    const bar = arguments[0];
    const timer = arguments[1];
    const main_link = arguments[2];
    const scroll_bar = document.querySelector(bar).scroll(0,timer)
    if(main_link.includes("linkedin")){
        if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight){
            return "bottom"
        }
    }
"""