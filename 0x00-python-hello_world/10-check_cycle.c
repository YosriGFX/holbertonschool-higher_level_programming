#include "lists.h"

/**
 * check_cycle - check if list has a cycle
 * @head: pointer to list to be freed
 * Return: 0 if has no cycle or 1 if has cycle
 */
int check_cycle(listint_t *list)
{
listint_t *curr = list;
listint_t *next = list;

if (!list || list->next == NULL)
return (0);
while (curr && next && next->next && curr->next->next)
{
curr = curr->next;
next = next->next->next;
if (curr == next)
return (1);
}
return (0);
}
