#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * reverse_listint - reverses a list
 * @head: ptr to head ptr
 * Return: head ptr
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *previous = NULL;

	while (node)
	{
		next = node->next;
		node->next = previous;
		previous = node;
		node = next;
	}
	*head = previous;
	return (*head);
}
/**
 * is_palindrome - checks for palindromes
 * @head: pointer to head ptr
 * Return: 1 on success 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *rev, *mid;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	temp = *head;
	while (temp)
	{
		size++;
		temp= temp->next;
	}
	temp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		temp = temp->next;
	if ((size / 2) == 0 && temp->n != temp->next->n)
		return (0);
	temp = temp->next->next;
	rev = reverse_listint(&temp);
	mid = rev;
	temp = *head;
	while (rev)
	{
		if (temp->n != rev->n)
			return (0);
		temp = temp->next;
		rev = rev->next;
	}
	reverse_listint(&mid);
	return (1);
}
