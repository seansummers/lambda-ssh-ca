# lambda-ssh-ca

Lambda implementation of a stateless SSH CA.

If you need a key signed; this will sign and return a cert.

## TODO
* Document events supported (at least host and user signing request)
* figure out where to put the CA key (ENVIRONMENT, KMS, S3)
* determine how to configure (same options as CA storage)

### TBD
* how does the Lambda time affect key expiration?
