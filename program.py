import Search_movie
import requests



def main():
    print_function()
    search_event_loop()


def print_function():
    print('------------------------------------------------')
    print('-----------------MOVIE SEARCH APP---------------')
    print('------------------------------------------------')

def search_event_loop():
    try:

        search= 'ONCE_THROUGH_LOOP'

        while search != 'x':
            search= input('What would you like to search? Click x if you wish to exit')
            if search!= 'x':
                results=Search_movie.find_movies(search)
                print ('Found {} results.'.format(len (results)))
                for result in results:
                    print("{}-----{}".format(result.year, result.title))
    except ValueError:
        print ("Where's the value?")
    except requests.exceptions.ConnectionError as ce:
        print ("Error: Check your wifi connection. {}".format(ce))
    except Exception as x:
        print ("Yikes, that didn't work. Here's why {}".format (x))



    print ('exiting.....')



if __name__=='__main__':
    main()

