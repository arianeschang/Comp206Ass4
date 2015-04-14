#!/usr/bin/python
import sys
import cgi


user_name=""
form = cgi.FieldStorage()

def find_friends(user):
    ref = open("members.csv", "r")
    lst = []
    friend_lst = []
    for line in ref:
        lst.append(line)
    ref.close()
    for x in range(0, len(lst)):
        lst[x] = lst[x].strip()
        lst[x] = lst[x].split(" ")
        if (lst[x][1] == user):
            for y in range(3, len(lst[x])):
                friend_lst.append(lst[x][y])
    return friend_lst

def is_friends(me, him):
    if him in find_friends(me):
        return True
    elif me==him:
        return True
    else:
        return False

def all_users():
    ref = open("members.csv", "r")
    lst = []
    users_lst = []
    for line in ref:
        lst.append(line)
    ref.close()
    for x in range(0, len(lst)):
        lst[x] = lst[x].strip()
        lst[x] = lst[x].split(' ')
        users_lst.append(lst[x][1])
    return users_lst

def recent_posts(user):
    ref = open("topics.csv", "r")
    lst = []
    name_lst = []
    comment_lst = []
    for line in ref:
        lst.append(line)
    ref.close()
    for x in range(0, len(lst)):
        if (x % 2 == 0):
            name_lst.append(lst[x].strip())
        else:
            comment_lst.append(lst[x].strip())
    name_lst.reverse()
    comment_lst.reverse()

    del lst[:]
    for x in range(0, len(name_lst)):
        a = name_lst[x]
        b = comment_lst[x]
        c = (a, b)
        if is_friends(a, user):
            lst.insert(x, c)
    lst=lst[0:10]
    return lst

def posts_html(lst):
    if lst==[]:
      string=""
    else:
      for i in range(0, len(lst)):
        lst[i]="</p> <blockquote>".join(lst[i])
        string = "<p>" + "</blockquote> <hr /> <p>".join(lst) + "</blockquote>"
    return string

def is_member(user):
    if user in all_users():
        return True
    else:
        return False

def add_friend(user1, user2):
    ref = open ("members.csv","r")
    lst = []
    for line in ref:
        lst.append(line)
    for x in range(0, len(lst)):
        lst[x] = lst[x].split()
        if lst[x][1]==user1:
            if (not is_friends(user1, user2)) and is_member(user2):
                lst[x].append(user2)
    for x in range(0, len(lst)):
        lst[x]=" ".join(lst[x])
    ref.close()
    lst = "\n".join(lst)
    ref = open ("members.csv","w")
    ref.write(lst)
    ref.close()
    return 0

message="""

<html>

<head>
<title>MovMe</title>
</head>
<body bgcolor="ccffcc">
<table border="1px">
  <tr>
    <th rowspan="2">
      <img src="http://www.lemonchutney.com/wp-content/uploads/2013/04/10-greatest-movie-posters-ever-made-04-420-75.jpg" alt="Silence of the Lambs" width="100px">

      <img src="http://main-designyoutrust.netdna-ssl.com/wp-content/uploads/2012/11/titanic-movie-poster-1997-1020339699.jpg" alt="Titanic" width="100px">

      <br>
      <img src="http://www.movieposter.com/posters/archive/main/9/A70-4902" alt="Matrix" width="100px">
      
      <img src="http://www.freedesign4.me/wp-content/gallery/posters/free-movie-film-poster-harry-potter-phoenix.jpg" alt="HarryPotter" width="100px">

      <br>
      <img src="http://netdna.webdesignerdepot.com/uploads/2011/02/jurassicpark.jpg" alt="Jurassic Park" width="100px">
      
      <img src="http://images2.fanpop.com/images/photos/8400000/Movie-Posters-movies-8405245-1224-1773.jpg" alt="POC" width="100px">

      <br>
      <img src="http://www.kitaro10.com/wp-content/uploads/2010/03/film-poster-51.jpg" alt="Salt" width="100px">
      
      <img src="http://meetinthelobby.com/wp-content/uploads/2012/01/Jennifer_Lawrence_The_Hunger_Games_Movie_Poster.jpg" alt="The Hunger Games" width="100px">

    </th>
    <th colspan="2" align="center" valign="top" width="75%" height="150px">
      <font face="Abadi MT Condensed Light" size="8">
        MovMe  
      </font>

      <br>
      <img src=" https://scontent-lga.xx.fbcdn.net/hphotos-xaf1/v/t1.0-9/11102865_10153208606604483_3697769982336368912_n.jpg?oh=7477219f53b32e00a69df221a02c1048&oe=55E56669" alt="titlePic" width="90px">
      <br> 
      Welcome {2}
      <a href="http://www.cs.mcgill.ca/~aschan/welcome.html">
      LogOut
      </a>
    </th>
    <th rowspan="2">
      <img src="http://www.lemonchutney.com/wp-content/uploads/2013/04/10-greatest-movie-posters-ever-made-04-420-75.jpg" alt="Silence of the Lambs" width="100px">

      <img src="http://main-designyoutrust.netdna-ssl.com/wp-content/uploads/2012/11/titanic-movie-poster-1997-1020339699.jpg" alt="Titanic" width="100px">

      <br>
      <img src="http://www.movieposter.com/posters/archive/main/9/A70-4902" alt="Matrix" width="100px">
      
      <img src="http://www.freedesign4.me/wp-content/gallery/posters/free-movie-film-poster-harry-potter-phoenix.jpg" alt="HarryPotter" width="100px">

      <br>
      <img src="http://netdna.webdesignerdepot.com/uploads/2011/02/jurassicpark.jpg" alt="Jurassic Park" width="100px">
      
      <img src="http://images2.fanpop.com/images/photos/8400000/Movie-Posters-movies-8405245-1224-1773.jpg" alt="POC" width="100px">

      <br>
      <img src="http://www.kitaro10.com/wp-content/uploads/2010/03/film-poster-51.jpg" alt="Salt" width="100px">
      
      <img src="http://meetinthelobby.com/wp-content/uploads/2012/01/Jennifer_Lawrence_The_Hunger_Games_Movie_Poster.jpg" alt="The Hunger Games" width="100px">
  </th>
  </tr>
  <tr>
    <td align="center" valign="top" width="25%"><b>Share your ideas!</b>
      <form action="MyFacebookPage.py" method="POST">
        <input type="hidden" name="user" value="{4}">
          Add Comments:<br />
        <input type="text" name="comment" size="80">
        <input type="submit" value="submit"> <br /><br/>

         <iframe width="560" height="315" src="https://www.youtube.com/embed/yQ5U8suTUw0" frameborder="0" allowfullscreen>
         </iframe>
         <br/><br/>
          <b>Recent Comments...</b>
          {0}
      </form>
    </td>
    <td align="center" valign="top" width="15%">
      <div id="right banner" width="150px">
        <div id="Members"><b>Members</b><br />{1}</div><br/>
        <div id="Friends"><b>Friends</b><br />{3}</div><br/>
        <div id="add"><b>Add Friends<br />
        <form action="MyFacebookPage.py" method="POST">
          <input type="hidden" name="user" value="{5}">
          <input type="text" name="friend" size="12"><br />
          <input type="submit" value="Add">
        </form>
       </div>
      </div>
    </td>
  </tr>
</table>
</body>
</html>"""

if form.has_key('user'):
    user = form['user'].value.strip()
    user_name = user

if form.has_key('comment'):
    comment = form['comment'].value.strip()
    ref=open("topics.csv", "r+")
    ref.seek(-2,2)
    if(ref.read(2) == "\n\n"):
        ref.seek(-1,2)
    ref.write(user_name+"\n")
    ref.write(comment+"\n")
    ref.close()

if form.has_key('friend'):
    friend = form['friend'].value.strip()
    y=add_friend(user_name, friend)

post = posts_html(recent_posts(user_name))
members = all_users()
members = '<ul style="margin:0; list-style-type:none; padding:0"> <li>' + '</li> <li>'.join(members) + '</li> </ul>'
friends = find_friends(user_name)
friends = '<ul style="margin:0; list-style-type:none; padding:0"> <li>' + '</li> <li>'.join(friends) + '</li> </ul>'
print("content-type:text/html\n\n")
print(message.format(post, members, user_name, friends, user_name, user_name))
