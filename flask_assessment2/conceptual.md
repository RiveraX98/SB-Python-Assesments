### Conceptual Exercise

Answer the following questions below:

- What is RESTful routing?
    Representational state transfer 
        -Architectural styling constraints for creating web services. (Standardized protocol for setting up API's)

- What is a resource?
    A resource is an object with a type, associated data and possible relationships to other resources. Represented as a model and has specified methods.

- When building a JSON API why do you not include routes to render a form that when submitted creates a new user?
    When building a JSON API you should always respod with JSON because the client is asking for data to either send or recieve.

- What does idempotent mean? Which HTTP verbs are idempotent?
    An operation that is idempotent is one that can be preformed many times (with the same data) and getting the same as if it was done once. 
    (produces no side affects)
        - Idempotent operations : GET, PUT, PATCH, DELETE
        

- What is the difference between PUT and PATCH?
    Put - Updates an entire resource (every piece of data associated)
    Patch - Updates part of a resource


- What is one way encryption?
    Cryptographic hash functions- hash functions that use one way functionality


- What is the purpose of a `salt` when hashing a password?
    Differentiates hasing for similar password and prevents collision
        -adds an extra layer of security 


- What is the purpose of the Bcrypt module?
    Bcrypt hashes and applies a salt to a given password 


- What is the difference between authorization and authentication?
    Authentication - Verifying identity through credentials 
    Authorization - Permmision to do and not do certain things
