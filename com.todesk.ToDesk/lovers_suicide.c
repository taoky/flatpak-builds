// Run given command with PR_SET_PDEATHSIG
#include <linux/prctl.h>
#include <stdio.h>
#include <sys/prctl.h>
#include <signal.h>
#include <unistd.h>

int main(int argc, char **argv) {
    prctl(PR_SET_PDEATHSIG, SIGKILL);
    char **args = argv + 1;
    extern char **environ;
    if (execve(args[0], args, environ) == -1) {
        perror("lovers_suicide: execve failed");
    }
    return 1;
}
