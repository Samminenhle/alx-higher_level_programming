#ifndef LISTS_H
#define LISTS_H

/**
 * struct list_s - lists
 * @n: integer
 * @next: pointer to the next node
 *
 * Description: Linked list 
 * Return number of nodes
 */
typedef struct list_s
{
	unsigned int n;
	struct list_s *next;
}list_t;


