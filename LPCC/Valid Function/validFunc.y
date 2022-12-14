%{
#include <stdio.h>
#include <ctype.h>
#define YYSTYPE char*
int count = 0;
extern YYSTYPE yytext;
%}
%token id fun err
%%
S: fun { printf("Built-in function found - %s", yytext); count++;}
     | id {}
   ;
%%
int main()
{
   printf("\nEnter the string:\n\n");
   yyparse();
   printf("\n");
   if(count==0)
     printf("No Built-in function found\n");
   return 0;
}
int yywrap()
{
   return 1;
}
int yyerror(char *mes) {
   return 0; 
}
