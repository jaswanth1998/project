import midea
import fresh_tomatoes

raja_rani= midea.Movie("Raja Rani","The greast love story","http://chennaionline.com/images/gallery/2013/August/20130820092949/Raja-Rani-Movie-Posters-Wallpapers-02.jpg","https://youtu.be/9cU-CxcXksI")
#print(toy_story.storyline)
chenni_express = midea.Movie("Chenni Exprees","The Comedey entner","http://www.indicine.com/images/gallery/bollywood/movies/chennai-express/103901-chennai-express-poster-large.jpg","https://youtu.be/rARol7Dk2zo")
premam = midea.Movie("Premam","the beautifull love stories","https://in.bmscdn.com/iedb/movies/images/website/poster/large/premam-telugu-et00040912-10-10-2016-03-34-56.jpg","https://www.youtube.com/watch?v=eEH2ba3VGjc")
#print(chenni_express.storyline)
#chenni_express.show_tralier()
toy_story=midea.Movie("Toy story","my childhood best movie","http://orig11.deviantart.net/44ff/f/2015/014/9/f/toy_story_4_fan_poster_by_jubaaj-d8dw15h.jpg","https://www.youtube.com/watch?v=Bj4gS1JQzjk&t=8s")
jualiyi=midea.Movie("jualiyi","brain is god ","http://content.gulte.com/content/2012/06/photos/movies/Julayi%20Movie%20Posters/normal/Julayi%20Movie%20Posters_20.jpg","https://www.youtube.com/watch?v=jxYa6VkL4Oc")
kathi=midea.Movie("kathi","Attudie is every thing ","http://www.vijayfansclub.com/wp-content/uploads/2014/09/kaththi-exclusive-hd-stills-09.jpg","https://www.youtube.com/watch?v=bMf0IyzyKt4")
movies = [jualiyi,kathi,raja_rani,toy_story,chenni_express,premam]
fresh_tomatoes.open_movies_page(movies)
