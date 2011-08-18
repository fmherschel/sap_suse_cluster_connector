

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <errno.h>

int fork_a_program(const char *result)
{
        pid_t childPid;
        int check_rc=0;
	int mye;
#define CMD_RETURN "./return"
        childPid=fork();
        switch ( childPid ) {
                case -1: /* got an error during fork */
                        printf("fork() failed\n");
                        break;
                case 0:  /* we have forked - childprocess */
                        execl(CMD_RETURN, CMD_RETURN, result, NULL);
			mye=errno;
                        printf("execl() failed %i %s\n", mye, strerror(mye));
			exit(99);
			check_rc=-1;
                        /*  we should never come to this line ;-) */
                        break;
                default: /* the current process (parent) */
			printf("forked process %li\n", childPid);
                        waitpid(childPid, &check_rc, 0);
			printf("Got check rc=%i div %i mod %i \n", check_rc, check_rc/256, check_rc % 256);
#if 0
                        if (WIFEXITED(check_rc)) {
                                printf("Command terminated normally\n");
                                check_rc=WEXITSTATUS(check_rc);
				printf("Got check rc=%i\n", check_rc);
                        } else {
                                mye=errno;
                                printf("Command terminated abnormally: errno: %i %s\n", mye, strerror(mye));
                                check_rc=-1;
                        }
#endif
                        break;
        }
        return check_rc;
}

int main(void) {
	fork_a_program("0");
	fork_a_program("1");
	fork_a_program("4");
	return 0;
}
