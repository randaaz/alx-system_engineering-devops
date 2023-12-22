#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - Creates an infinite loop to keep the program running
 *
 * Return: Always 0.
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Creates 5 zombie processes
 *
 * Return: Always 0.
 */

int main(void)
{
	pid_t pe_id;
	char i = 0;

	while (i < 5)
	{
		pe_id = fork();
		if (pe_id > 0)
		{
			printf("Zombie process created, PID: %d\n", pe_id);
			sleep(1);
			i++;
		}
		else
			exit(0);
	}

	infinite_while();

	return (EXIT_SUCCESS);
}
