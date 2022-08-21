#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
int infinite_while(void);

/**
 *infinite_while - Creates an infinit loop
 *Return: 0 (success)
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
 *main - Entry point
 *Return: 0 (success)
 */
int main(void)
{
	pid_t ZOMBIE_PID;
	int i;

	for (i = 0; i < 5; i++)
	{
		if ((fork()) == 0)
		{
			dfprint(1, "Zombie process created, PID: %u\n", getpid());
			return (0);
		}
	}
	infinite_while();
	return (0);
}
