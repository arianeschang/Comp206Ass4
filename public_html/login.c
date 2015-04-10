#include <stdio.h>
#include <stdlib.h>
#include <string.h>

 char* getfield(char* line, int num);

int main(){
    printf("Content-type: text/html\n\n");
    char string[200];
    char user[40];
    char pass[40];
    char c;
    int a=0;
    int n=atoi(getenv("CONTENT_LENGTH"));

    while ((c=getchar())!= EOF && a<n){
      if (a<200){
        string[a]=c;
        a++;
        }
    }
    string[a]=0;

    int i=5; int j=0; int k=0; int advance=0;

    for (i=5; i<n; i++){
      if (string[i]=='&'){
        advance=1;
        i=i+6;
      }
      if (string[i]!='&' && advance==0){
        user[j]=string[i];
        j++;
      }
      if (advance==1 && string[i]!=0){
        pass[k]=string[i];
        k++;
      }
    }
    user[j]=0;
    pass[k]=0;

    FILE *file=fopen("members.csv","r");

    int found=0;


    char line[1024];
    while(fgets(line,1024,file) && found==0){
      char* tmp = strdup(line);
      char* tmp2 = strdup(line);
      
      if(strcmp(getfield(tmp,2),user)==0){
        if(strcmp(getfield(tmp2,3),pass)==0){
        found=1;
        free(tmp);
        printf("<HTML><head><title>Welcome to MovMe!</title></head><body bgcolor='#c1ffc1' text='black'><table style='width:100%%' bgcolor='white'><col align='left' width='25%%'>\
          <col align='left'><col align='right' width='25%%'><tr><td><img src='http://www.lemonchutney.com/wp-content/uploads/2013/04/10-greatest-movie-posters-ever-made-04-420-75.jpg' alt='Silence of the Lambs' style='width:100px'>\
          <img src='http://main-designyoutrust.netdna-ssl.com/wp-content/uploads/2012/11/titanic-movie-poster-1997-1020339699.jpg' alt='Titanic' style='width:100px'><br>\
          <img src='http://www.movieposter.com/posters/archive/main/9/A70-4902' alt='Matrix' style='width:100px'><img src='http://www.freedesign4.me/wp-content/gallery/posters/free-movie-film-poster-harry-potter-phoenix.jpg' alt='HarryPotter' style='width:100px'>\
          <br><img src='http://netdna.webdesignerdepot.com/uploads/2011/02/jurassicpark.jpg' alt='Jurassic Park' style='width:100px'><img src='http://images2.fanpop.com/images/photos/8400000/Movie-Posters-movies-8405245-1224-1773.jpg' alt='POC' style='width:100px'>\
          <br><img src='http://www.kitaro10.com/wp-content/uploads/2010/03/film-poster-51.jpg' alt='Salt' style='width:100px'><img src='http://meetinthelobby.com/wp-content/uploads/2012/01/Jennifer_Lawrence_The_Hunger_Games_Movie_Poster.jpg' alt='The Hunger Games' style='width:100px'>\
          </td><td align=center valign=top><font face='Abadi MT Condensed Light' size='8'>MovMe</font><br><img src='https://scontent-lga.xx.fbcdn.net/hphotos-xaf1/v/t1.0-9/11102865_10153208606604483_3697769982336368912_n.jpg?oh=7477219f53b32e00a69df221a02c1048&oe=55E56669' alt='titlePic' width='90px' style='margin:0 auto'>\
          <br><h2> Share your favorite movies with your friends!</h2>\
          <h3> Login Successful!</h3><br><form action='MyFacebookPage.py' method='post'><br /><input type='hidden' name='user' value=%s><input type='submit' \
          value='Access Your Feed'></td><td align=right><img src='http://www.lemonchutney.com/wp-content/uploads/2013/04/10-greatest-movie-posters-ever-made-04-420-75.jpg' alt='Silence of the Lambs' style='width:100px'>\
          <img src='http://main-designyoutrust.netdna-ssl.com/wp-content/uploads/2012/11/titanic-movie-poster-1997-1020339699.jpg' alt='Titanic' style='width:100px'><br>\
          <img src='http://www.movieposter.com/posters/archive/main/9/A70-4902' alt='Matrix' style='width:100px'><img src='http://www.freedesign4.me/wp-content/gallery/posters/free-movie-film-poster-harry-potter-phoenix.jpg' alt='HarryPotter' style='width:100px'>\
          <br><img src='http://netdna.webdesignerdepot.com/uploads/2011/02/jurassicpark.jpg' alt='Jurassic Park' style='width:100px'><img src='http://images2.fanpop.com/images/photos/8400000/Movie-Posters-movies-8405245-1224-1773.jpg' alt='POC' style='width:100px'>\
          <br><img src='http://www.kitaro10.com/wp-content/uploads/2010/03/film-poster-51.jpg' alt='Salt' style='width:100px'><img src='http://meetinthelobby.com/wp-content/uploads/2012/01/Jennifer_Lawrence_The_Hunger_Games_Movie_Poster.jpg' alt='The Hunger Games' style='width:100px'></form></HTML>\
          </td></tr></table></body></html>",user);
      }
      }
      //printf("Usernames are %s\n", getfield(tmp, 2));
      //printf("%s\n", getfield(tmp,2));
  

    }
    
    if (found==0){
    printf("<HTML> <meta http-equiv='Refresh' content='1; url=loginFailed.html'></HTML>");
    }
    return 0;
}

 char* getfield(char* line, int num)
{
     char* tok;
    for (tok = strtok(line, " ");
            tok && *tok;
            tok = strtok(NULL, " \n"))
    {
        if (!--num)
            return tok;
    }
    return NULL;
}
