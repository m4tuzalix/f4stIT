new Vue({
    delimiters: ['[[', ']]'],
    el:"#main",
    data: { 
        search: "",
        selected: [],
        cities_to_pass: "",
        cities: [
            {text:"Remote", value:"Remote"},
            {text:"Wrocław", value:"Wrocław"},
            {text:"Warszawa", value:"Warszawa"},
            {text:"Poznań", value:"Poznań"},
            {text:"Kraków", value:"Kraków"},
            {text:"Katowice", value:"Katowice"},
            {text:"Łódź", value:"Łódź"},
            {text:"Inne", value:"Inne"},

        ]
    },
    methods: {
        CityDropdown(bool){
            this.$refs.city_dropdown.visible = bool
        },
        AllCities(){
            var link = ""
            this.selected.map((e)=>{
                link += e
                if(this.selected.indexOf(e) != this.selected.length-1){
                    link += ","
                }
            })
            return link
        },
    }
})