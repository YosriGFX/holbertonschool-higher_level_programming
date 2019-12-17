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
		int count = 0, a, b;
		listint_t *temp;
		listint_t *ver;

		temp = *head;
		while (temp)
		{
			temp = temp->next;
			count++;
		}
		temp = *head;
		ver = *head;
		for (a = 0; a < (count / 2); a++)
		{
			for (b = 0; b < (count - a); b++)
				ver = ver->next;
			temp = temp->next;
			if (ver->n != temp->n)
				return (0);
			ver = *head;
		}
		return (1);
	}
	else
		return (1);
}
