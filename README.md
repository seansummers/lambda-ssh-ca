# lambda-ssh-ca

Lambda implementation of a stateless SSH CA.

If you need a key signed; this will sign and return a cert.

## TODO
* Document events supported (at least host and user signing request)
* figure out where to put the CA key (ENVIRONMENT, KMS, S3)
* determine how to configure (same options as CA storage)

### TBD
* how does the Lambda time affect key expiration?

### (Possible) SSH login options see https://github.com/openssh/openssh-portable/blob/master/PROTOCOL.certkeys
* restrict (all forwarding, and no pty or rc unless readded)
* command="program"
* environment="NAME=value"
* from="pattern-list" (see PATTERNS in ssh_config)
* [no-]agent-forwarding
* [no-]port-forwarding
* [no-]pty
* [no-]user-rc
* [no-]X11-forwarding
* permitopen="host:port"
* principals="name1[,name2,...]"
* tunnel="n"

