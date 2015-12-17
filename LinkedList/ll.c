struct node
{
int data;
struct node *next;
};

/* Given a reference (pointer to pointer) to the head of a list
   and an int, inserts a new node on the front of the list. */

node push(struct node** head_ref, int new_data)
{
struct node* new_node=(struct node*) malloc (sizeof(struct node));
new_node->data=new_data;
new_node->next=(*head_ref)

}
