import fresh_tomatoes
import media

the_holy_grail = media.Movie("Monty Python and The Holy Grail","1975",
                             "932 AD, King Arthur travel throughout Britain"
                             " searching the Knights of the Round Table. "
                             "To find the Holy Grail.",
                             "https://upload.wikimedia.org/wikipedia/en/0/08/Monty-Python-1975-poster.png", # NOQA
                             "https://youtu.be/urRkGvhXc8w")

and_now_for_something_completely_different = media.Movie("And Now for Something Completely Different","1971","And Now for Something Completely Different is a 1971 British sketch comedy film based on the television comedy series Monty Python's Flying Circus featuring sketches from the first two series. The title was taken from a catchphrase used in the television show.","https://upload.wikimedia.org/wikipedia/en/e/ee/ANFSCD_poster.jpg","https://youtu.be/IDtepG8EvHE")

life_of_brian = media.Movie("Monty Python's Life of Brian","1979","Brian Cohen is born in a stable next door to the one in which Jesus is born, which initially confuses the three wise men who come to praise the future King of the Jews. Brian grows up an idealistic young man who resents the continuing Roman occupation of Judea. While attending Jesus' Sermon on the Mount, Brian becomes infatuated with an attractive young rebel, Judith. His desire for her and hatred for the Romans lead him to join the People's Front of Judea, one of many fractious and bickering independence movements, who spend more time fighting each other than the Romans.","https://upload.wikimedia.org/wikipedia/en/1/18/Lifeofbrianfilmposter.jpg","https://youtu.be/TKPmGjVFbrY")

live_at_the_hollywood_bowl = media.Movie("Monty Python Live at the Hollywood Bowl", "1982", "Monty Python Live at the Hollywood Bowl is a 1982 British concert comedy film directed by Terry Hughes (with the film segments by Ian MacNaughton) and starring the Monty Python comedy troupe (Graham Chapman, John Cleese, Terry Gilliam, Eric Idle, Terry Jones, and Michael Palin) as they perform many of their sketches at the Hollywood Bowl.", "https://upload.wikimedia.org/wikipedia/en/d/d2/MontyPythonHollywoodBowlPoster.jpg", "https://youtu.be/3Fg3-Ma-HA8")

the_meaning_of_life = media.Movie("Monty Python's The Meaning of Life", "1983", "A group of fish in a posh restaurant's tank swim together casually, until they look at the customers outside of the tank and see their friend Howard being eaten. This leads them to question the meaning of life. The question is explored in the first sketch, The Miracle of Birth, which features a woman in labour being ignored by the doctors in favour of impressing the hospital's administrator. In Yorkshire, a Roman Catholic man loses his job and returns home to tell his numerous children that he will have to sell them off for scientific experiments due to the Catholic church's opposition to contraception; this leads to the musical number Every Sperm is Sacred. Meanwhile, a Protestant man and his wife discuss having non-reproductive sex.", "https://upload.wikimedia.org/wikipedia/en/9/91/Meaningoflife.jpg", "https://youtu.be/LH8aTeouR4Y", )

live_mostly = media.Movie("Monty Python Live (Mostly)", "2014", "In 2013, the Pythons lost a legal case to Mark Forstater, the producer of their second film, Holy Grail, over royalties for its musical adaptation Spamalot. They owed a combined 800,000 ($994,600) in legal fees and back royalties to Forstater. To pay these, a reunion show was proposed.", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Monty_Python_Live_%28Mostly%29.jpg/440px-Monty_Python_Live_%28Mostly%29.jpg", "https://youtu.be/yBcYuwlWFRM")

movies = [the_holy_grail, and_now_for_something_completely_different, life_of_brian, live_at_the_hollywood_bowl, the_meaning_of_life, live_mostly]

print(media.Movie.__module__)
fresh_tomatoes.open_movies_page(movies)
