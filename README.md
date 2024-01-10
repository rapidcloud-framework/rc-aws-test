# Custom module dev process


## Create home dir for RC bundle and all modules:

`.../rapid-cloud-custom-modules/`


## Install bundle:

```
.../rapid-cloud-custom-modules
.../kc-rapid-cloud
```

## Test installation:

`kc version`

_note: always test your modules or run kc command or start console from bundle home dir_


## Module repos you're working on:

```
.../rapid-cloud-custom-modules/
    rc-aws-net
    rc-eks-net
    ...
    rc-az-lz
```


## Create module and add more commands from bundle dir

`kc module create`

`kc module add_command`

Then copy the structure to the module repo and continue working inside the module repo.


## Each module repo has this structure:

```
.../rapid-cloud-custom-modules/
    <repo_home>/
        commands/
            modules/
                <name_of_your_module>
        server/
            custom_server.py
        terraform/
            custom_templates
                <resource>.j2
                <resource>.j2
            modules
                <resource>
                    <file>.tf
                    <file>.tf
```


## Activating 

`kc module activate`

## Tagging (versioning)

- Each tested / ready to be deployed module must be tagged with that module version
- Let me know which tag (version) to include in the next build