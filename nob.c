#define NOB_IMPLEMENTATION
#define NOB_STRIP_PREFIX
#include "nob.h"

int main(int argc, char** argv) {
    NOB_GO_REBUILD_URSELF(argc, argv);

    mkdir_if_not_exists("build");

    Cmd cmd = {0};

    nob_log(INFO, "Building:");
    cmd_append(&cmd, "zip", "build/extension.zip", "fix.css", "manifest.json");
    if(!cmd_run_sync_and_reset(&cmd)) return 1;

    return 0;
}
