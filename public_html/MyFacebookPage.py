#!/usr/bin/python
import sys
import cgi
user_name = "aaa"
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


def is_friends(user1, user2):
    if user1 in find_friends(user2):
        return True
    elif user1==user2:
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

    return lst

def posts_html(lst):
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
<html style="font-family:Arial,Helvetica; sans-serif; color:#333">
<head>
  <title>HTML Layout using Tables</title>
</head>
<body style="background:#ccc; margin=0">
 <div id="container" style="width:960px; margin:0 auto; background:#999;">
   <div id="header" style="width:100%; height:80px; background:#333">
      <div id="logo" style="float:left; width:60px; height:60px; margin:10px; background:#ccc">logo</div>
      <div id="title" style="float:left; width:120px; height:60px; background:#666; margin:10px"><h1>MovMe</h1></div>
      <div id="top info" style="float:right; width:100px; height:60px; background:#666; margin:10px">top info</div>

      <div id="navbar" style="clear:both; height:20px; float:right">
        <ul style="margin:0; list-style-type:none; padding:0" >
           <li style="float:left; padding:5px">
              Welcome {2}!
           </li>
           <li style="float:left; padding:5px;">
              <a href="http://www.cs.mcgill.ca/~hshin5" style="font-size:15px; float:left; display:block;" >
                LogOut
              </a>
          </li>
        </ul>
      </div>
   </div>
   <div id="content area" style="width:700px; float:left; clear:both; margin:10px">
      <div id="banner" style="background:#666; height:70px; width:700px; clear:both; padding:10px">
         Share your ideas!
         <form action="MyFacebookPage.py" method="POST">
             Add Comments:<br />
             <input type="text" name="comment">
             <input type="submit" value="submit">
         </form>
      </div>
      <div id="left col" style="color:#fff; margin:10px; background:#000;" align="center">
         <iframe width="560" height="315" src="https://www.youtube.com/embed/yQ5U8suTUw0" frameborder="0" allowfullscreen>
         </iframe>
      </div>
   </div>
   <div id="right banner" style="float:right; width:150px; margin:10px">
      <div id="Members" style="flaot:left; background:#888; margin:0 0 5px 0; padding:5px"><b>Members</b>{1}</div>
      <div id="Friends" style="flaot:left; background:#888; clear:both; margin:0 0 5px 0; padding:5px"><b>Friends</b>{3}</div>
      <div id="add" style="flaot:left; background:#888; clear:both;padding:5px"><b>Add Friends</b>
        <form action="MyFacebookPage.py" method="POST">
           <input type="text" name="friend" size="12"><br />
           <input type="submit" value="Add">
         </form>
      </div>
   </div>
   <div id="recent_comments" style="padding:20px; background:#888; width:700px; margin:10px; float:left">
      recent_comments
      {0}
   </div>
 </div>
</body>
</html>"""

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
if form.has_key('user'):
    user = form['user'].value.strip()
    user_name = user


post = posts_html(recent_posts(user_name))
members = all_users()
members = '<ul style="margin:0; list-style-type:none; padding:0"> <li>' + '</li> <li>'.join(members) + '</li> </ul>'
friends = find_friends(user_name)
friends = '<ul style="margin:0; list-style-type:none; padding:0"> <li>' + '</li> <li>'.join(friends) + '</li> </ul>'
print("content-type:text/html\n\n")
print(message.format(post, members, user_name, friends))
