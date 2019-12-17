#include "lists.h"
/**
 * is_palindrome - function check if list palandrome
 * @head: head to list
 * Return: 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	if (*head)
	{
		int count = 0, a, b, v, e;
		listint_t *temp = malloc(sizeof(listint_t));
		temp = *head;
		while (temp)
		{
			temp = temp->next;
			count++;
		}
		free(temp);
		temp = *head;
		for (a = 0; a < (count / 2); a++)
		{	
			listint_t *ver = malloc(sizeof(listint_t));
			ver = *head;
			for (b = 0; b < (count - a - 1); b++)
			{
				if (ver->next)
					ver = ver->next;
				v = ver->n;
			}
			e = temp->n;
			if (e != v)
			{
				return (0);
			}
			temp = temp->next;
		}
		return (1);
	}
	else
		return (1);
}
