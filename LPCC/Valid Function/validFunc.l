%{
#include<stdio.h>
#include "y.tab.h"
%}
%%

[\t ]+                    /* ignore whitespace */ ;
printf |
scanf |
strlen |
strcpy |
malloc |
realloc |
memcpy |
memset |
isalpha |
isdigit |
islower |
isupper    { return fun; }


[a-zA-Z]+ { yylval=*yytext; return id; }

\n { return(0); }
. { return err; }

%%
