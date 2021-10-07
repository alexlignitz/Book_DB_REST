# Book_DB_REST
Application fetching and processing data from external API

Original book list available under: /viewset/books

Filtering queries examples: /viewset/books/?published_date=2012
                            /viewset/books/?author=tolkien
                            
Sorting queries examples: /viewset/books/?sort=published_date                           
                          /viewset/books/?sort=-published_date
                          
Updating database with new books available under= /db
                                                  queryset {"q":"_keyword_"}
