#include "lists.h"
/*
 * is_palindrome - check if list palandrome
 * @head: head to list
 * Return: 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	if (*head)
	{
		int count = 0;
		listint_t *temp;
		temp = *head;
		while (temp[count])
			count++;
		return (count);
	}
	else
		return (1);
}
