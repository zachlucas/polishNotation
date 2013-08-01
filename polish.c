#include<stdlib.h>
#include<stdio.h>

typedef struct node {
    int value;
    struct node *next; 
} node_t;

void push(int value, node_t **stack){
    node_t *temp = (node_t*)malloc(sizeof(node_t));
    temp->value=value;
    temp->next = *stack;
    *stack = temp;
    //free(temp);
}


int pop(node_t **stack){
    node_t *temp = *stack;
    int value = temp->value;
    *stack=(*stack)->next;
    free(temp);
    return value;
}

int main(){
    printf("F");
    char* expression = "6 3 - 9 +";
    //scanf("%c", expression);
    int result; 
    node_t *stack = NULL;

    int i;
    
    for(i=0;expression[i]!='\0';i++){
    
    
        if (expression[i] == ' ')
            continue;
   
        else if (expression[i] == '+' || expression[i] == '-'){
            if (expression[i] == '+')
                result = pop(&stack)+pop(&stack);
            else{
                int var1 = pop(&stack);
                int var2 = pop(&stack);
                result = var2-var1;
                }
            push(result, &stack);
        }
        else
            push(atoi(&expression[i]),&stack);
     
    }
    
    printf("Done y'all, result is %d\n", result);
    
   return 0;
    

}
