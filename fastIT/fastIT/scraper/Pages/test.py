import webbrowser

web = webbrowser
web.register("chrome", web.Chrome)
web.get("chrome")
web.open("https://allegro.pl/listing?string=opaski%20na%20nadgarstki&bmatch=dict210105-ctx-spo-1-5-0112", new=0)