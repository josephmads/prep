EnergyHub Coding Sample

At EnergyHub, we have a few main concepts: 

- A Utility partner, who we faciliate energy reduction programs for
- Programs, which we enroll utility customers with qualifying devices into
- Enrollments, which represent an association between a utility customer and smart home devices, like a Nest thermostat
- Devices, like the Nest thermostat referred to above
- Groups, which are collections of devices that we assign to energy reduction events

Sometimes, we need to migrate collections of Enrollments and Devices between Programs.

Your task is to read in files containing lists of dictionarys representing Programs, Enrollments, and Devices, and write out the Enrollments and Devices after they have been "migrated". 

The Data:

There are 3 files you will need to read in, each representing the data you would find in a database for a particular entity

- Programs:

```
    {
        name: "Program 1",
        programId: 1,
        utilityId: 1,
        defaultGroup: 1,
        supportedManufacturers: ["NEST", "ECOBEE", "HONEYWELL"]
    },
```

Each program dictionary contains the program name, the program id, id for the utility the program is assigned to, the default group all devices should be in for the program, and the device manufacturers that are supported for the program

- Enrollments:

```
    {
        firstName: "Jim",
        lastName: "Jimmerson",
        address: "123 Abc Way, Unit 1",
        zipCode: 12345,
        programId: 1,
        devices: [
            {
                manufacturer: "NEST",
                uuid: abc123
            }
            
        ]
    }
```

Enrollments are the record for the customer that is enrolled in a program, their name and contact information, and the devices associated with this customer

- Devices:

```
    {
        manufacturer: "NEST",
        uuid: "abc123",
        group: 1
    }
```

The Device dictionary contains information about the device manufacturer, the uuid for the device, and the group the device is in


The Goal: 

All of our enrollments/devices are currently in `program1`. We would like everything to be migrated to `program2`.

You will write a Python or Javascript script that does the following:
    - associates all enrollments with `program2`
    - assigns devices to the correct default group for their associated program
    - only migrates enrollments that have device manufacturers supported by the target program
    - writes out the outputs to updated `migrated-enrollments.txt` and `migrated-devices.txt` files

Bonus:
- write out the diff of your migration changes to an additional file so we know the exact fields that have been updated
- create a script method that can take the migration diff file and use it to "reverse" the migration


Delivery Instructions:

- Pull this repository
- Checkout a development branch and write your scripts
- Open a PR against the `main` branch with:
    - your scripts
    - instructions in this README on how to run these scripts
- Send a link to the PR back to the EnergyHub recruiting team

## My Script
