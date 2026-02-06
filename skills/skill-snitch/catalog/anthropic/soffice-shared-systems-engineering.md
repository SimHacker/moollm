# office/soffice.py — Deep Probe: Systems Engineering Analysis

> Shared across docx, pptx, xlsx. The most technically remarkable script in the Anthropic repo.

**Trust**: YELLOW (runtime C compilation, LD_PRELOAD syscall interception) | **Lines**: 148 Python + 95 C

## What It Does

Detects whether AF_UNIX sockets are blocked (sandboxed environments), and if so:
1. Writes C source code to `/tmp/lo_socket_shim.c`
2. Compiles it with GCC: `gcc -shared -fPIC -o lo_socket_shim.so lo_socket_shim.c -ldl`
3. Sets `LD_PRELOAD` so LibreOffice loads the shim
4. The shim intercepts `socket()`, `listen()`, `accept()`, `close()` syscalls
5. When `socket(AF_UNIX)` fails, falls back to `socketpair()` with pipe-based blocking
6. When the listener socket is closed, calls `_exit(0)` — clean shutdown

## The C Shim (annotated)

```c
// Per-FD bookkeeping (FDs >= 1024 pass through unshimmed)
static int is_shimmed[1024];
static int peer_of[1024];    // socketpair partner
static int wake_r[1024];      // accept() blocks on this pipe
static int wake_w[1024];      // close() writes to this pipe

// socket(AF_UNIX) blocked → fall back to socketpair()
int socket(int domain, int type, int protocol) {
    if (domain == AF_UNIX) {
        int fd = real_socket(domain, type, protocol);
        if (fd >= 0) return fd;  // worked normally
        // Blocked! Use socketpair instead
        int sv[2];
        real_socketpair(domain, type, protocol, sv);
        // Set up pipe for accept() blocking
        ...
    }
}

// accept() blocks by reading from a pipe that close() writes to
int accept(...) {
    if (is_shimmed[sockfd]) {
        char buf;
        real_read(wake_r[sockfd], &buf, 1);  // block here
        errno = ECONNABORTED;
        return -1;
    }
}

// close() on listener → _exit(0) — conversion done
int close(int fd) {
    if (is_shimmed[fd]) {
        write(wake_w[fd], &c, 1);  // unblock accept()
        if (was_listener) _exit(0);  // clean shutdown
    }
}
```

## Security Surface

| Risk | Severity | Detail |
|------|----------|--------|
| Runtime C compilation | MEDIUM | Writes source to /tmp, compiles with GCC. If /tmp is writable by attacker, source could be replaced. |
| LD_PRELOAD | MEDIUM | Modifies process behavior at syscall level. The shim is benign but the mechanism is powerful. |
| `_exit(0)` | LOW | Shim kills the process when listener closes. Expected behavior for batch conversion but harsh. |
| FD limit | LOW | Only shims FDs 0-1023. FDs >= 1024 pass through unshimmed. Fine for LibreOffice. |

## MOOLLM Notes

**Don't import this.** It's a platform-specific workaround for sandboxed environments. The docx/pptx/xlsx skills that depend on it are too heavy for MOOLLM import — LibreOffice as a runtime dependency is a big ask.

**Worth documenting as**: an example of remarkable systems engineering in a skill script. This is the kind of deep problem-solving that earns respect. If we ever need LibreOffice integration in MOOLLM, reference this approach.

**Pattern worth naming**: "Runtime Environment Adaptation" — detect platform constraints, compile a workaround, inject it transparently. The Python code that does the detection (`_needs_shim()`) is elegant: try to create a Unix socket, if it fails, you need the shim.
