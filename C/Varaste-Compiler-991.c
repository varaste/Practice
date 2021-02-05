/* A simple One-Pass Compiler */
/* global.h */

#include <stdio.h>  /* include declarations for i/o routines */
#include <ctype.h>  /* ... and for character test routines */
#include <stdlib.h> /*and for some standard routines, such as exit*/
#include <string.h> /* ... and for string routines */
#include<math.h>

#define BSIZE  128  /* buffer size */
#define NONE   -1
#define EOS    '\0'

#define NUM    256
#define DIV    257
#define MOD    258
#define ID     259
#define DONE   260

extern int tokenval;   /*  value of token attribute */  
extern int lineno;

struct entry {  /*  form of symbol table entry  */
  char *lexptr; 
  int  token;    
};


int MAXSIZE = 80;       
int stack[80];     
int top = -1; 
int Oprand1;
int Oprand2;
int Result;
int i = 0;
//int PA;
//int Nama;


extern void error(char* m);  /*  generates all error messages  */
extern int lexan();  /*  lexical analyzer  */
extern void parse();  /*  parses and translates expression list  */
extern int insert(char *s, int tok);  /*  returns position of entry for s */
extern int lookup(char *s);  /*  returns position of entry for s */
extern void emit (int t, int tval);  /*  generates output  */
extern struct entry symtable[];  /* symbol table  */

//-----------------------------------------------------
/* lexer.c */

char lexbuf[BSIZE];
int  lineno = 1;
int paranmatch=0;
int paranmatchinp=0;
int columno=0;
int  tokenval = NONE;
char buffer[BSIZE];

void parse();

int lexan (){  /*  lexical analyzer  */
  int t;
  while(1) {
  	columno=columno+1;
    t=getchar();
    if(t==')') paranmatchinp=paranmatchinp+1;
    if(t==')'){
    	if(paranmatch!=paranmatchinp){
    		error("No ( was opened !");parse();
    	}
    } 
    if (t == '#') exit(1);
     if (t == ' ' || t == '\t')
      ;  /*  strip out white space  */
    else if (t == '\n'){
	   columno=0;lineno = lineno + 1;
	   printf("--> %d : ",lineno);
	}
    else if (t == '*'){
    	t=getchar();
    	if (t == '*') return '^';
    	else{
    		ungetc(t,stdin);
    		return '*';
    	}
    }
    else if (isdigit (t)) {  /*  t is a digit  */
      ungetc(t, stdin);
      scanf("%d", &tokenval);
      return NUM;
    }
    else if (isalpha(t)) {  /*  t is a letter */
      int p, b = 0;
      while (isalnum(t)) {  /* t is alphanumeric  */
		lexbuf [b] = t; 
        t = getchar ();
        b = b + 1;
        if (b >= BSIZE)
          error("Identifier's name should be less than 128 characters!");
      }
      lexbuf[b] = EOS;
      if (t != EOF)
        ungetc(t, stdin);
      p = lookup (lexbuf);
      if (p == 0)
        p = insert (lexbuf, ID);
      tokenval = p;
      return symtable[p].token;
    }
    else if (t == EOF)
      return DONE;
    else {
      tokenval = NONE;
      return t;
    }
  }
}

//-----------------------------------------------------
/*Stack*/

int isempty() {
   if(top == -1)
      return 1;
   else
      return 0;
}
   
int isfull() {
   if(top == MAXSIZE)
      return 1;
   else
      return 0;
}  

int peek() {
   return stack[top];
}

int pop() {
   int data;
   if(!isempty()) {
      data = stack[top];
      top = top - 1;   
      return data;
   } else {
      printf("Could not retrieve data, Stack is empty.\n");
   }
}

int push(int data) {
   if(!isfull()) {
      top = top + 1;   
      stack[top] = data;
   } else {
      printf("Could not insert data, Stack is full.\n");
   }
}

//-----------------------------------------------------
/* parser.c -- without the optimizations */

int lookahead;
void match(int);
void matchpower();
void start();
void list();
void expr();
void moreterms();
void term();
void morefactors();
void factor();


void parse()  { 
  /*  parses and translates expression list  */
  lookahead = lexan();
  start();
}

void start (){
  /* Just one production for start, so we don't need to check lookahead */
  list();
  match(DONE);
}


//( 5 -->>-3)*(2+1)
void list(){
  if (lookahead == '(' || lookahead == ID || lookahead == NUM) {
    expr(); 
	match(';'); 
	list();
  }
  else {
    /* Empty */
  }
}

void expr (){
  /* Just one production for expr, so we don't need to check lookahead */
  term(); 
  moreterms();
}

void moreterms(){
  if (lookahead == '+') {
    match('+'); 
	term(); 
	emit('+', tokenval); 
	moreterms();
  }
  else if (lookahead == '-') {
    match('-'); 
	term(); 
	emit('-', tokenval); 
	moreterms();
  }
  else if(lookahead=='.'){
  	error(". is not an operator !");
	parse();
  }
  else if(lookahead== 92){
  	error("\\ is not an operator !");
	parse();
  }
  else {
    /* Empty */
  }
}
void power(){
  /* Just one production for term, so we don't need to check lookahead */
  if (lookahead == '(') {
    match('('); 
	expr(); 
	match(')');
  }
  else if (lookahead == ID) {
    int id_lexeme = tokenval;
    match(ID);
    emit(ID, id_lexeme);
  }
  else if (lookahead == NUM) {
    int num_value = tokenval;
    match(NUM);
    emit(NUM, num_value);
  }
  else if(lookahead ==')'){
  	error("No ( was opened ! ");
	parse();
  }
  else
    error("Expected an expression like (E), an identifier, or a number after an operand!");  
}
void morepowers(){
  if (lookahead == '^') {
	{match('^');
	factor();
	emit('^', tokenval);
	}
  }

  else{
  	/*empty*/
  }
}
void term (){
  /* Just one production for term, so we don't need to check lookahead */
  factor();
  morefactors();
}


void morefactors (){
  if (lookahead == '*') {
    match('*'); 
	factor(); 
	emit('*', tokenval);
  }
  else if (lookahead == '/') {
    match('/'); 
	factor(); 
	emit('/', tokenval);
  }

  else if (lookahead == DIV) {
    match(DIV); 
	factor(); 
	emit(DIV, tokenval); 
	morefactors();
  }
  else if (lookahead == MOD) {
    match(MOD); 
	factor(); 
	emit(MOD, tokenval); 
	morefactors();
  }
  else {
    /* Empty */
  }
}

void factor (){
	power();
	morepowers();
}
void match(int t){	
  if(t=='(') paranmatch=paranmatch+1;
  if (lookahead == t)
    lookahead = lexan();
  else{
    	if(t==')') error("expected ) at the end of expression");
	}
}

//-----------------------------------------------------
/* emitter.c */
void emit (int t, int tval){
  
//(5-3)*(2+1);
  switch(t) {
  case NUM:
  	push(tval);
  	//printf("%d ", tval);
    //printf("Pushed to stack.\n\n");

 break;
  case '+':
    Oprand1 = pop();
    Oprand2 = pop();
	Result = Oprand1+Oprand2;
	push(Result);
	printf("Result of ");	
	printf("%d", Oprand1);
	printf(" + ");
	printf("%d", Oprand2);
	printf(" is: ");
	printf("%d ", Result);
	printf("\n\n"); 
	break;

  case '-' : 
    Oprand1 = pop();
    Oprand2 = pop();
	Result = Oprand2-Oprand1;
	push(Result);
	printf("Result of ");	
	printf("%d", Oprand2);
	printf(" - ");
	printf("%d", Oprand1);
	printf(" is: ");
	printf("%d ", Result);
	printf("\n\n"); 
	break;
  
  case '*' : 
    Oprand1 = pop();
    Oprand2 = pop();
	Result = Oprand2*Oprand1;
	push(Result);
	printf("Result of ");	
	printf("%d", Oprand1);
	printf(" * ");
	printf("%d", Oprand2);
	printf(" is: ");
	printf("%d ", Result);
	printf("\n\n"); 
	break;

  case '/':  	
    Oprand1 = pop();
    Oprand2 = pop();
	Result = Oprand2/Oprand1;
	push(Result);
	printf("Result of ");	
	printf("%d", Oprand2);
	printf(" / ");
	printf("%d", Oprand1);
	printf(" is: ");
	printf("%d ", Result);
	printf("\n\n"); 
	break;

  case '^':
  	Oprand2 = pop();
    Oprand1 = pop();
    Result = pow(Oprand1, Oprand2);
	push(Result);
	printf("Result of ");	
	printf("%d", Oprand1);
	printf(" ^ ");
	printf("%d", Oprand2);
	printf(" is: ");
	printf("%d ", Result);
	printf("\n\n"); 
	break;

  case '%':  	
    Oprand1 = pop();
    Oprand2 = pop();
	Result = Oprand2%Oprand1;
	push(Result);
	printf("Result of ");	
	printf("%d", Oprand2);
	printf(" % ");
	printf("%d", Oprand1);
	printf(" is: ");
	printf("%d ", Result);
	printf("\n\n"); 
	break;

  }
}

//-----------------------------------------------------
/* symbol.c */

#define STRMAX 999  /*  size of lexemes array  */
#define SYMMAX 100  /*  size of symbol table */

char lexemes[STRMAX];
int  lastchar = - 1;  /*  last used position in lexemes   */
struct entry symtable[SYMMAX];
int lastentry = 0;    /*  last used position in symtable  */

int lookup(char *s){  /*  returns position of entry for s */
  int p;
  for (p = lastentry; p > 0; p = p - 1)
    if (strcmp(symtable[p].lexptr, s) == 0)
      return p;
  return 0;
}

int insert(char *s, int tok){/*returns position of entry for s*/
  int len;
  len = strlen(s);  /*  strlen computes length of s     */
  if (lastentry + 1 >= SYMMAX)
    error ("symbol table full");
  if (lastchar + len + 1 >= STRMAX)
    error ("lexemes array full");
  lastentry = lastentry + 1;
  symtable[lastentry].token = tok;
  symtable[lastentry].lexptr = &lexemes[lastchar + 1];
  lastchar = lastchar + len + 1;
  strcpy(symtable[lastentry].lexptr, s);
  return lastentry;
}

//-----------------------------------------------------
/* init.c */

struct entry keywords[] = {
  { "div", DIV },
  { "mod", MOD, },
  { 0,     0 }
};

void init(){  /*  loads keywords into symtable  */
  struct entry *p;
  for (p = keywords; p->token; p++)
    insert(p->lexptr, p->token);
}


//-----------------------------------------------------
/* error.c */

void error(char* m){  /* generates all error messages  */
  fprintf(stderr, "@ : line %d column %d: %s\n", lineno, columno, m);
  //exit(EXIT_FAILURE);  /*  unsuccessful termination  */
}


//-----------------------------------------------------
/* main.c */
void welcome(){
	printf("**************************************************************************\n");
	printf("Enter ((;)) at the end of your expression.\n");
	printf("To exit the program, type # and then hit enter!\n");
	printf("**************************************************************************\n");
	printf("--> 1 : ");
}

int main(){
	welcome();
    init();
    parse();
    exit(0);    /*  successful termination  */
}









