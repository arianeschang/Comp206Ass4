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
        printf("<HTML><head><title>Welcome to MovMe!</title></head><body bgcolor='red' text='black'><h2> Share your favorite movies with your friends!</h2><h3> Login Successful!</h3><br><form action='MyFacebookPage.py' method='post'><br /><input type='hidden' name='user' value=%s><input type='submit' value='Access Your Feed'></form></HTML>",user);
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
