import firelink
links=[firelink.Facebook_link,firelink.Udemy_link,firelink.EL_Drive_link]
url=input("Choose Which Website to open\
      \n1: Facebook Link\n2: Udemy Link\n3: Embedded Linux Drive Link\n")
firelink.firefox(links[int(url)-1])